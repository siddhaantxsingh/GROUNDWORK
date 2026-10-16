"""Retrieval: BM25, dense, hybrid (RRF / weighted), RM3 query expansion and a
feature-based reranker, over an in-memory `Corpus`.

The `Corpus` is the query-time index. In the service it is rebuilt from
PostgreSQL (the source of truth) at start-up and maintained incrementally;
dense search can alternatively be delegated to pgvector (see store.py).
Metadata filters (tenant, document set) are applied INSIDE every retriever
before top-k selection, never after, so a filter cannot empty a result list
that has matching candidates further down.
"""
from __future__ import annotations

import heapq
import math
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Callable

import numpy as np

from .bm25 import BM25Index
from .embed import Embedder, embed_queries
from .text import tokenize


@dataclass(frozen=True)
class ChunkRecord:
    id: str
    doc_id: str
    doc_name: str
    ordinal: int
    text: str
    page_start: int
    page_end: int
    section: str
    tenant: str = "default"


@dataclass
class Hit:
    chunk: ChunkRecord
    score: float
    sources: dict[str, float] = field(default_factory=dict)  # per-retriever score / rank info


Filter = Callable[[ChunkRecord], bool]


class Corpus:
    def __init__(self, embedder: Embedder | None = None, k1: float = 1.2, b: float = 0.75) -> None:
        self.chunks: dict[str, ChunkRecord] = {}
        self.bm25 = BM25Index(k1, b)
        self.embedder = embedder
        self._ids: list[str] = []
        self._vecs: np.ndarray | None = None
        self._pending: dict[str, np.ndarray] = {}
        self._deleted: set[str] = set()

    def __len__(self) -> int:
        return len(self.chunks)

    def add(self, chunks: list[ChunkRecord], vectors: np.ndarray | None = None) -> None:
        if vectors is None and self.embedder is not None and chunks:
            vectors = self.embedder.embed([embed_text(c) for c in chunks])
        for i, c in enumerate(chunks):
            self.chunks[c.id] = c
            self._deleted.discard(c.id)
            self.bm25.add(c.id, index_text(c))
            if vectors is not None:
                self._pending[c.id] = vectors[i]

    def delete_doc(self, doc_id: str) -> int:
        ids = [cid for cid, c in self.chunks.items() if c.doc_id == doc_id]
        for cid in ids:
            del self.chunks[cid]
            self.bm25.delete(cid)
            self._pending.pop(cid, None)
            self._deleted.add(cid)
        return len(ids)

    def _matrix(self) -> tuple[list[str], np.ndarray | None]:
        """Compact pending inserts and deletions into one dense matrix."""
        if self._pending or self._deleted:
            keep = [(i, cid) for i, cid in enumerate(self._ids) if cid not in self._deleted and cid not in self._pending]
            ids = [cid for _, cid in keep] + list(self._pending)
            parts = []
            if keep and self._vecs is not None:
                parts.append(self._vecs[[i for i, _ in keep]])
            if self._pending:
                parts.append(np.stack(list(self._pending.values())))
            self._vecs = np.concatenate(parts) if parts else None
            self._ids = ids
            self._pending.clear()
            self._deleted.clear()
        return self._ids, self._vecs

    def vectors_for(self, ids: list[str]) -> np.ndarray | None:
        """Stored embeddings of the given chunks (no re-embedding)."""
        all_ids, m = self._matrix()
        if m is None:
            return None
        if getattr(self, "_row_ids", None) is not all_ids:
            self._row = {cid: i for i, cid in enumerate(all_ids)}
            self._row_ids = all_ids
        return m[[self._row[c] for c in ids]]

    def allowed(self, flt: Filter | None) -> set[str] | None:
        if flt is None:
            return None
        return {cid for cid, c in self.chunks.items() if flt(c)}

    # ---------------------------------------------------------------- retrievers

    def search_bm25(self, query: str, k: int, flt: Filter | None = None,
                    weights: dict[str, float] | None = None, terms: list[str] | None = None) -> list[Hit]:
        res = self.bm25.search(query, k, allowed=self.allowed(flt), weights=weights, terms=terms)
        return [Hit(self.chunks[d], s, {"bm25": s}) for d, s in res]

    def search_dense(self, query: str, k: int, flt: Filter | None = None, qvec: np.ndarray | None = None) -> list[Hit]:
        if self.embedder is None:
            return []
        ids, m = self._matrix()
        if m is None or not ids:
            return []
        q = qvec if qvec is not None else embed_queries(self.embedder, [query])[0]
        sims = m @ q
        if flt is not None:
            mask = np.fromiter((flt(self.chunks[c]) for c in ids), dtype=bool, count=len(ids))
            sims = np.where(mask, sims, -np.inf)
        k = min(k, len(ids))
        top = np.argpartition(-sims, k - 1)[:k]
        top = sorted(top, key=lambda i: (-sims[i], ids[i]))
        return [Hit(self.chunks[ids[i]], float(sims[i]), {"dense": float(sims[i])}) for i in top if np.isfinite(sims[i])]


# Text used for indexing: the section heading carries strong signal (names,
# signatures), so it is indexed with the body. Citations still point at the
# chunk text itself.
def index_text(c: ChunkRecord) -> str:
    return f"{c.section.split(' > ')[-1]}\n{c.text}" if c.section else c.text


def embed_text(c: ChunkRecord) -> str:
    return index_text(c)


# ------------------------------------------------------------------ fusion


def rrf(lists: list[list[Hit]], k: int, k_rrf: int = 60, names: list[str] | None = None) -> list[Hit]:
    """Reciprocal rank fusion: score(d) = sum_i 1 / (k_rrf + rank_i(d))."""
    acc: dict[str, float] = defaultdict(float)
    by_id: dict[str, Hit] = {}
    info: dict[str, dict] = defaultdict(dict)
    for li, lst in enumerate(lists):
        name = names[li] if names else f"r{li}"
        for rank, h in enumerate(lst, start=1):
            acc[h.chunk.id] += 1.0 / (k_rrf + rank)
            by_id.setdefault(h.chunk.id, h)
            info[h.chunk.id][f"{name}_rank"] = rank
    out = heapq.nsmallest(k, acc.items(), key=lambda x: (-x[1], x[0]))
    return [Hit(by_id[c].chunk, s, info[c]) for c, s in out]


def weighted_fusion(lists: list[list[Hit]], weights: list[float], k: int) -> list[Hit]:
    """Convex combination of min-max normalised scores (missing = 0)."""
    acc: dict[str, float] = defaultdict(float)
    by_id: dict[str, Hit] = {}
    for lst, w in zip(lists, weights):
        if not lst:
            continue
        hi, lo = max(h.score for h in lst), min(h.score for h in lst)
        span = hi - lo or 1.0
        for h in lst:
            acc[h.chunk.id] += w * (h.score - lo) / span
            by_id.setdefault(h.chunk.id, h)
    out = heapq.nsmallest(k, acc.items(), key=lambda x: (-x[1], x[0]))
    return [Hit(by_id[c].chunk, s, {"fused": s}) for c, s in out]


# ------------------------------------------------------------------ query rewriting


def rm3_expand(corpus: Corpus, query: str, fb_docs: int = 10, fb_terms: int = 10, orig_weight: float = 0.6,
               flt: Filter | None = None) -> tuple[list[str], dict[str, float]]:
    """RM3 pseudo-relevance feedback (Lavrenko & Croft relevance model,
    interpolated with the original query). Returns (terms, weights) for a
    weighted BM25 query. Expansion terms come only from the top `fb_docs`
    feedback chunks; with no feedback the original query is returned."""
    q = tokenize(query)
    if not q:
        return q, {}
    fb = corpus.search_bm25(query, fb_docs, flt)
    if not fb:
        return q, {t: 1.0 for t in q}
    rel: dict[str, float] = defaultdict(float)
    z = sum(math.exp(h.score - fb[0].score) for h in fb)
    for h in fb:
        pd = math.exp(h.score - fb[0].score) / z  # P(d|q) ~ softmax of BM25 scores
        tv = corpus.bm25.term_vector(h.chunk.id)
        dl = sum(tv.values()) or 1
        for t, c in tv.items():
            rel[t] += pd * c / dl
    exp_terms = heapq.nlargest(fb_terms, rel.items(), key=lambda x: (x[1], x[0]))
    qn = Counter(q)
    weights: dict[str, float] = defaultdict(float)
    for t, c in qn.items():
        weights[t] += orig_weight * c / len(q)
    tot = sum(w for _, w in exp_terms) or 1.0
    for t, w in exp_terms:
        weights[t] += (1 - orig_weight) * w / tot
    # Scale so original terms keep weight ~1 (BM25 weights multiply idf).
    scale = 1.0 / max(weights.values())
    weights = {t: w * scale for t, w in weights.items()}
    return list(weights), weights


# ------------------------------------------------------------------ reranking


def _min_span(positions: list[list[int]]) -> int | None:
    """Smallest window containing at least one position from every list."""
    if not positions or any(not p for p in positions):
        return None
    heap = [(p[0], i, 0) for i, p in enumerate(positions)]
    heapq.heapify(heap)
    hi = max(p[0] for p in positions)
    best = hi - heap[0][0]
    while True:
        lo, i, j = heapq.heappop(heap)
        best = min(best, hi - lo)
        if j + 1 >= len(positions[i]):
            return best
        nxt = positions[i][j + 1]
        hi = max(hi, nxt)
        heapq.heappush(heap, (nxt, i, j + 1))


@dataclass
class RerankWeights:
    first_stage: float = 1.0
    coverage: float = 0.5
    proximity: float = 0.3
    heading: float = 0.4
    dense: float = 0.5


def rerank(corpus: Corpus, query: str, hits: list[Hit], k: int, w: RerankWeights = RerankWeights(),
           qvec: np.ndarray | None = None) -> list[Hit]:
    """Second-stage reranking with hand-designed features combined linearly
    (weights tuned on the dev split; see benchmarks/). Features:
      first_stage  min-max normalised first-stage score
      coverage     share of distinct query terms present in the chunk
      proximity    1 / (1 + smallest window covering all present query terms / 10)
      heading      share of query terms in the section heading
      dense        cosine similarity to the query (if an embedder exists)
    This is not a neural cross-encoder (none is available offline)."""
    if not hits:
        return []
    qterms = list(dict.fromkeys(tokenize(query)))
    hi, lo = max(h.score for h in hits), min(h.score for h in hits)
    span = hi - lo or 1.0
    dense_sims: dict[str, float] = {}
    if w.dense and corpus.embedder is not None:
        q = qvec if qvec is not None else embed_queries(corpus.embedder, [query])[0]
        vecs = corpus.vectors_for([h.chunk.id for h in hits])
        dense_sims = {h.chunk.id: float(v @ q) for h, v in zip(hits, vecs)}
    out = []
    for h in hits:
        toks = tokenize(h.chunk.text)
        pos: dict[str, list[int]] = defaultdict(list)
        for i, t in enumerate(toks):
            pos[t].append(i)
        present = [t for t in qterms if t in pos]
        coverage = len(present) / len(qterms) if qterms else 0.0
        msp = _min_span([pos[t] for t in present]) if len(present) > 1 else None
        proximity = 1.0 / (1.0 + msp / 10.0) if msp is not None else (1.0 if present else 0.0)
        head = set(tokenize(h.chunk.section.split(" > ")[-1])) if h.chunk.section else set()
        heading = len([t for t in qterms if t in head]) / len(qterms) if qterms else 0.0
        s = (w.first_stage * (h.score - lo) / span + w.coverage * coverage + w.proximity * proximity
             + w.heading * heading + w.dense * dense_sims.get(h.chunk.id, 0.0))
        out.append(Hit(h.chunk, s, {**h.sources, "coverage": coverage, "proximity": proximity, "heading": heading,
                                     "dense_sim": dense_sims.get(h.chunk.id, 0.0)}))
    out.sort(key=lambda x: (-x.score, x.chunk.id))
    return out[:k]


def model_rerank(model, query: str, hits: list[Hit], depth: int) -> list[Hit]:
    """Rescore the top `depth` hits with a neural reranker; hits below the
    depth keep their order after the reranked ones."""
    head, tail = hits[:depth], hits[depth:]
    scores = model.score(query, [index_text(h.chunk) for h in head])
    order = sorted(range(len(head)), key=lambda i: (-scores[i], i))
    return [Hit(head[i].chunk, scores[i], {**head[i].sources, "first_stage_rank": i + 1, "model_score": scores[i]})
            for i in order] + tail


# ------------------------------------------------------------------ pipeline


@dataclass
class RetrievalConfig:
    mode: str = "hybrid"          # bm25 | dense | hybrid
    fusion: str = "rrf"           # rrf | weighted
    dense_weight: float = 0.5     # weighted fusion only
    rewrite: str = "none"         # none | rm3
    rerank: bool = False
    candidates: int = 100         # first-stage depth per retriever
    rerank_weights: RerankWeights = field(default_factory=RerankWeights)
    # Optional neural reranker (e.g. local_models.Qwen3Reranker): any object
    # with `name` and `score(query, texts) -> list[float]`. It rescores the
    # top `model_rerank_depth` hits after fusion / feature reranking.
    model_reranker: object | None = None
    model_rerank_depth: int = 20

    def label(self) -> str:
        parts = [self.mode]
        if self.mode == "hybrid":
            parts.append(self.fusion if self.fusion == "rrf" else f"w{self.dense_weight}")
        if self.rewrite != "none":
            parts.append(self.rewrite)
        if self.rerank:
            parts.append("rerank")
        if self.model_reranker is not None:
            parts.append(f"{getattr(self.model_reranker, 'name', 'model')}@{self.model_rerank_depth}")
        return "+".join(parts)


def retrieve(corpus: Corpus, query: str, k: int, cfg: RetrievalConfig, flt: Filter | None = None,
             timings: dict | None = None) -> list[Hit]:
    import time

    t0 = time.perf_counter()
    terms = weights = None
    if cfg.rewrite == "rm3":
        terms, weights = rm3_expand(corpus, query, flt=flt)
    t1 = time.perf_counter()
    depth = max(k, cfg.candidates)
    lists, names = [], []
    qvec = None
    if cfg.mode in ("bm25", "hybrid"):
        lists.append(corpus.search_bm25(query, depth, flt, weights=weights, terms=terms))
        names.append("bm25")
    t2 = time.perf_counter()
    if cfg.mode in ("dense", "hybrid") and corpus.embedder is not None:
        qvec = embed_queries(corpus.embedder, [query])[0]
        lists.append(corpus.search_dense(query, depth, flt, qvec=qvec))
        names.append("dense")
    t3 = time.perf_counter()
    if cfg.mode == "hybrid" and len(lists) == 2:
        hits = rrf(lists, depth, names=names) if cfg.fusion == "rrf" else weighted_fusion(lists, [1 - cfg.dense_weight, cfg.dense_weight], depth)
    else:
        hits = lists[0] if lists else []
    if cfg.rerank:
        hits = rerank(corpus, query, hits, max(k, cfg.model_rerank_depth) if cfg.model_reranker else k,
                      cfg.rerank_weights, qvec=qvec)
    if cfg.model_reranker is not None and hits:
        hits = model_rerank(cfg.model_reranker, query, hits, cfg.model_rerank_depth)
    t4 = time.perf_counter()
    if timings is not None:
        timings.update(rewrite_ms=(t1 - t0) * 1e3, bm25_ms=(t2 - t1) * 1e3, dense_ms=(t3 - t2) * 1e3,
                       fuse_rerank_ms=(t4 - t3) * 1e3, total_ms=(t4 - t0) * 1e3)
    return hits[:k]
