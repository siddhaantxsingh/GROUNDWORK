"""Service engine: ties parsing, chunking, embedding, PostgreSQL and the
in-memory query index together, per tenant.

Concurrency model: one process; database access and index mutation are
serialized by a lock (psycopg connections are not shareable across threads).
Retrieval runs under the lock (it is fast, in memory); answer generation,
which may be a slow HTTP call, runs OUTSIDE the lock, so one slow provider
call does not block other tenants, uploads or health checks. Horizontal
scaling would need a shared index (pgvector HNSW search exists in
`Store.ann_search` and is benchmarked, but the query path uses the
in-memory matrix).

Embedding lifecycle per tenant (the `embedders` row is authoritative):
  * no saved model -> signed hashing embedder (no state)
  * once the tenant has >= `lsa_min_chunks` chunks, LSA is fitted on them;
    refitted whenever the corpus has doubled since the last fit
  * a fit saves the model AND re-embeds every chunk in the SAME transaction
    as the ingest that triggered it, so stored vectors always belong to the
    saved model; on restart the saved model is loaded whatever the current
    chunk count is (deletions never switch the space back)
  * with a fixed pretrained embedder configured (`EngineConfig.embedder`,
    e.g. nomic-embed-text through llama.cpp) there is no fitting; if the
    stored vectors belong to another space they are all re-embedded in one
    transaction when the tenant is loaded, and the row records the model
Vectors are zero-padded to the configured dimension so the pgvector column
type never changes.
"""
from __future__ import annotations

import hashlib
import json
import threading
import time
from dataclasses import dataclass, field

import numpy as np

from .chunking import ChunkSpec, chunk_blocks
from .embed import HashingEmbedder, LSAEmbedder
from .generate import ExtractiveProvider, InjectionPolicy, Provider, answer_json, build_sources, check_grounding
from .ingest import parse
from .retrieve import ChunkRecord, Corpus, RetrievalConfig, embed_text, retrieve
from .store import Store, deserialize_lsa, serialize_lsa


class PaddedEmbedder:
    """Zero-pads (or rejects) vectors to a fixed dimension; cosine unchanged."""

    def __init__(self, inner, dim: int) -> None:
        if inner.dim > dim:
            raise ValueError(f"embedder dim {inner.dim} exceeds configured dim {dim}")
        self.inner, self.dim = inner, dim
        self.name = inner.name

    def embed(self, texts):
        return self._pad(self.inner.embed(texts))

    def embed_query(self, texts):
        from .embed import embed_queries

        return self._pad(embed_queries(self.inner, texts))

    def _pad(self, v):
        if v.shape[1] == self.dim:
            return v
        out = np.zeros((v.shape[0], self.dim), dtype=np.float32)
        out[:, : v.shape[1]] = v
        return out


@dataclass
class TenantIndex:
    corpus: Corpus
    fitted_size: int = 0
    version: int = 0


@dataclass
class EngineConfig:
    dim: int = 256
    chunking: ChunkSpec = field(default_factory=ChunkSpec)
    lsa_min_chunks: int = 50
    retrieval: RetrievalConfig = field(default_factory=lambda: RetrievalConfig(mode="bm25", rerank=True))
    injection_policy: InjectionPolicy = InjectionPolicy.EXCLUDE
    grounding_threshold: float = 0.7
    # Optional fixed (pretrained) embedder shared by all tenants, e.g.
    # local_models.NomicEmbedder. None = hashing -> per-tenant LSA lifecycle.
    embedder: object | None = None


class Engine:
    def __init__(self, store: Store, cfg: EngineConfig | None = None, provider: Provider | None = None, cache=None) -> None:
        self.store, self.cfg = store, cfg or EngineConfig()
        self.provider = provider or ExtractiveProvider()
        self.cache = cache
        self.lock = threading.RLock()
        self.tenants: dict[str, TenantIndex] = {}

    # ---------------------------------------------------------------- index lifecycle

    def load_tenant(self, tenant: str) -> TenantIndex:
        with self.lock:
            if tenant in self.tenants:
                return self.tenants[tenant]
            recs, vecs = self.store.load_chunks(tenant)
            saved = self.store.load_embedder(tenant)
            fixed = self.cfg.embedder
            if fixed is not None:
                emb = PaddedEmbedder(fixed, self.cfg.dim)
                fitted = 0
                if saved is None or saved[0] != emb.name:
                    # Stored vectors belong to another space (LSA / hashing /
                    # another model): re-embed every chunk in one transaction.
                    vecs = emb.embed([embed_text(r) for r in recs]) if recs else None
                    with self.store.conn.transaction():
                        if recs:
                            self.store.update_embeddings([r.id for r in recs], vecs)
                        self.store.save_embedder(tenant, emb.name, b"")
            elif saved and saved[0].startswith("lsa"):
                emb = PaddedEmbedder(deserialize_lsa(saved[1]), self.cfg.dim)
                fitted = max(len(recs), 1)
            else:
                emb = PaddedEmbedder(HashingEmbedder(self.cfg.dim), self.cfg.dim)
                fitted = 0
                if saved:  # vectors from a fixed model that is no longer configured
                    vecs = emb.embed([embed_text(r) for r in recs]) if recs else None
                    with self.store.conn.transaction():
                        if recs:
                            self.store.update_embeddings([r.id for r in recs], vecs)
                        self.store.conn.execute("DELETE FROM embedders WHERE tenant = %s", (tenant,))
            corpus = Corpus(emb)
            if recs:
                if vecs is None:  # rows written without vectors (should not happen): re-embed
                    vecs = emb.embed([embed_text(r) for r in recs])
                corpus.add(recs, vecs)
            ti = TenantIndex(corpus, fitted)
            self.tenants[tenant] = ti
            return ti

    def _plan_refit(self, ti: TenantIndex, recs: list[ChunkRecord]):
        """Decide whether the corpus (existing + new `recs`) needs an LSA
        (re)fit. Returns (embedder, all_records, vectors) or None. Pure: no
        database or index side effects."""
        if self.cfg.embedder is not None:
            return None  # a pretrained embedder is never refitted
        allrecs = list(ti.corpus.chunks.values()) + recs
        n = len(allrecs)
        if n < self.cfg.lsa_min_chunks or (ti.fitted_size and n < 2 * ti.fitted_size):
            return None
        texts = [embed_text(r) for r in allrecs]
        lsa = LSAEmbedder(dim=self.cfg.dim).fit(texts)
        emb = PaddedEmbedder(lsa, self.cfg.dim)
        return lsa, emb, allrecs, emb.embed(texts)

    def _bump(self, tenant: str, ti: TenantIndex) -> None:
        ti.version += 1
        if self.cache is not None:
            self.cache.invalidate(tenant)

    # ---------------------------------------------------------------- operations

    def ingest(self, tenant: str, filename: str, data: bytes, media_type: str | None = None) -> dict:
        doc = parse(filename, data, media_type)
        chunks = chunk_blocks(doc.blocks, self.cfg.chunking)
        if not chunks:
            raise ValueError("document contains no extractable text")
        with self.lock:
            ti = self.load_tenant(tenant)
            rows = [(c.ordinal, c.text, c.page_start, c.page_end, c.section) for c in chunks]
            tmp = [ChunkRecord("", "", filename, c.ordinal, c.text, c.page_start, c.page_end, c.section, tenant) for c in chunks]
            vecs = ti.corpus.embedder.embed([embed_text(r) for r in tmp])
            refit = None
            committed = False
            try:
                # Document, chunks, and (if triggered) the new model plus the
                # re-embedding of every chunk: ONE transaction.
                with self.store.conn.transaction():
                    sd = self.store.insert_document(tenant, doc.title or filename, doc.media_type, doc.sha256, doc.page_count,
                                                    self.cfg.chunking.__dict__, rows, vecs, doc.meta)
                    if sd.created:
                        recs = [ChunkRecord(f"{sd.id}:{c.ordinal}", sd.id, sd.name, c.ordinal, c.text, c.page_start, c.page_end,
                                            c.section, tenant) for c in chunks]
                        refit = self._plan_refit(ti, recs)
                        if refit:
                            lsa, emb, allrecs, allvecs = refit
                            self.store.save_embedder(tenant, lsa.name, serialize_lsa(lsa))
                            self.store.update_embeddings([r.id for r in allrecs], allvecs)
                committed = True
            finally:
                if committed and sd.created:
                    # In-memory state changes only after the commit.
                    if refit:
                        _, emb, allrecs, allvecs = refit
                        corpus = Corpus(emb)
                        corpus.add(allrecs, allvecs)
                        ti.corpus, ti.fitted_size = corpus, len(allrecs)
                    else:
                        ti.corpus.add(recs, vecs)
                    self._bump(tenant, ti)
            return {"id": sd.id, "name": sd.name, "media_type": sd.media_type, "pages": sd.page_count,
                    "chunks": len(chunks), "created": sd.created, "empty_pages": doc.meta.get("empty_pages", [])}

    def delete(self, tenant: str, doc_id: str) -> bool:
        with self.lock:
            ok = self.store.delete_document(tenant, doc_id)
            if ok:
                ti = self.load_tenant(tenant)
                ti.corpus.delete_doc(doc_id)
                self._bump(tenant, ti)
            return ok

    def query(self, tenant: str, query: str, k: int = 5, generate: bool = True, cfg: RetrievalConfig | None = None,
              doc_ids: list[str] | None = None) -> dict:
        query = query.strip()
        if not query:
            raise ValueError("empty query")
        cfg = cfg or self.cfg.retrieval
        t0 = time.perf_counter()
        with self.lock:
            ti = self.load_tenant(tenant)
            ckey = None
            if self.cache is not None:
                ckey = hashlib.sha256(json.dumps([query, k, generate, cfg.label(), sorted(doc_ids or []), ti.version]).encode()).hexdigest()
                hit = self.cache.get(tenant, ckey)
                if hit is not None:
                    hit["cached"] = True
                    self.store.log_query(tenant, "cached:" + cfg.label(), hit.get("provider"),
                                         (time.perf_counter() - t0) * 1e3, {}, hit.get("abstained"),
                                         (hit.get("grounding") or {}).get("groundedness"))
                    return hit
            allow = set(doc_ids) if doc_ids else None
            flt = (lambda c: c.doc_id in allow) if allow else None
            timings: dict = {}
            hits = retrieve(ti.corpus, query, k, cfg, flt=flt, timings=timings)
            version_at_retrieval = ti.version
        out: dict = {"query": query, "retrieval": cfg.label(), "timings_ms": timings,
                     "hits": [{"chunk_id": h.chunk.id, "document": h.chunk.doc_name, "doc_id": h.chunk.doc_id,
                               "pages": [h.chunk.page_start, h.chunk.page_end], "section": h.chunk.section,
                               "score": round(h.score, 6), "excerpt": h.chunk.text[:300]} for h in hits]}
        g = None
        if generate:
            # Outside the lock: a provider call may take seconds.
            tg = time.perf_counter()
            sources, excluded = build_sources(hits, self.cfg.injection_policy)
            ans = self.provider.generate(query, sources)
            ans.excluded_sources = excluded
            g = check_grounding(ans, self.cfg.grounding_threshold)
            out.update(answer_json(ans, g))
            timings["generate_ms"] = (time.perf_counter() - tg) * 1e3
        total = (time.perf_counter() - t0) * 1e3
        timings["request_ms"] = total
        out["cached"] = False
        with self.lock:
            self.store.log_query(tenant, cfg.label(), self.provider.name if generate else None, total,
                                 out.get("usage", {}), out.get("abstained"), g.groundedness if g else None)
            # Only cache if the index did not change while generating.
            if ckey is not None and ti.version == version_at_retrieval:
                self.cache.put(tenant, ckey, out)
        return out
