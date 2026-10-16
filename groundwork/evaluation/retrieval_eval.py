"""Retrieval evaluation over a dataset directory (docs/ + queries.jsonl +
qrels.jsonl). Relevance is labelled at (document, section) level; chunk
rankings are mapped to their section and de-duplicated before scoring, so
every chunking strategy is scored on the same units.
"""
from __future__ import annotations

import hashlib
import json
import statistics
import time
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from ..chunking import ChunkSpec, chunk_blocks
from ..embed import HashingEmbedder, LSAEmbedder
from ..ingest import parse
from ..retrieve import ChunkRecord, Corpus, RetrievalConfig, retrieve
from .metrics import bootstrap_ci, dedupe_ranking, mean, ndcg_at_k, reciprocal_rank, recall_at_k


@dataclass
class Dataset:
    root: Path
    queries: list[dict]
    qrels: dict[str, dict[str, float]]  # query id -> unit -> gain

    @classmethod
    def load(cls, root: str | Path) -> "Dataset":
        root = Path(root)
        queries = [json.loads(l) for l in (root / "queries.jsonl").read_text().splitlines() if l.strip()]
        qrels: dict[str, dict[str, float]] = {}
        for l in (root / "qrels.jsonl").read_text().splitlines():
            if l.strip():
                r = json.loads(l)
                qrels.setdefault(r["query_id"], {})[unit_id(r["doc"], r.get("section", ""))] = float(r.get("relevance", 1))
        return cls(root, queries, qrels)

    def split(self, name: str) -> list[dict]:
        return [q for q in self.queries if name in ("all", q.get("split"))]


def unit_id(doc: str, section: str) -> str:
    return f"{doc}#{section}"


def build_corpus(ds: Dataset, spec: ChunkSpec, embedder="lsa", dim: int = 256,
                 vector_cache: str | Path | None = None) -> tuple[Corpus, dict]:
    """`embedder`: None, "lsa", "hashing", or an embedder object (e.g. a
    local_models.NomicEmbedder). For an object, chunk vectors can be cached
    in `vector_cache` (an .npz keyed by model name and chunk-text hash) so
    repeated benchmark runs do not re-embed the corpus."""
    t0 = time.perf_counter()
    records: list[ChunkRecord] = []
    for path in sorted((ds.root / "docs").iterdir()):
        doc = parse(path.name, path.read_bytes())
        for c in chunk_blocks(doc.blocks, spec):
            records.append(ChunkRecord(f"{path.name}:{c.ordinal}", path.name, path.name, c.ordinal, c.text,
                                       c.page_start, c.page_end, c.section))
    t1 = time.perf_counter()
    emb = None
    if embedder == "lsa":
        from ..retrieve import embed_text

        emb = LSAEmbedder(dim=dim).fit([embed_text(r) for r in records])
    elif embedder == "hashing":
        emb = HashingEmbedder(dim)
    elif embedder is not None:
        emb = embedder
    t2 = time.perf_counter()
    corpus = Corpus(emb)
    vecs = None
    if emb is not None and not isinstance(embedder, str):
        from ..retrieve import embed_text

        texts = [embed_text(r) for r in records]
        key = hashlib.sha256(json.dumps([emb.name, texts]).encode()).hexdigest()[:16]
        path = Path(vector_cache) / f"{emb.name}-{key}.npy" if vector_cache else None
        if path is not None and path.exists():
            vecs = np.load(path)
        else:
            vecs = emb.embed(texts)
            if path is not None:
                path.parent.mkdir(parents=True, exist_ok=True)
                np.save(path, vecs)
    corpus.add(records, vecs)
    t3 = time.perf_counter()
    stats = {"chunks": len(records), "parse_chunk_s": t1 - t0, "embedder_fit_s": t2 - t1, "index_s": t3 - t2,
             "embedder": emb.name if emb else None, "chunking": spec.__dict__}
    return corpus, stats


def evaluate(corpus: Corpus, ds: Dataset, cfg: RetrievalConfig, split: str = "dev", ks=(1, 5, 10, 20)) -> dict:
    per_query = []
    lat = []
    for q in ds.split(split):
        gains = ds.qrels.get(q["id"], {})
        if not gains:
            continue
        timings: dict = {}
        hits = retrieve(corpus, q["text"], max(ks) * 5, cfg, timings=timings)
        lat.append(timings["total_ms"])
        ranking = dedupe_ranking(unit_id(h.chunk.doc_id, h.chunk.section) for h in hits)
        rel = {u for u, g in gains.items() if g > 0}
        row = {"id": q["id"], "rr": reciprocal_rank(ranking, rel, 10)}
        for k in ks:
            row[f"recall@{k}"] = recall_at_k(ranking, rel, k)
            row[f"ndcg@{k}"] = ndcg_at_k(ranking, gains, k)
        per_query.append(row)
    summary = {"config": cfg.label(), "split": split, "queries": len(per_query)}
    for key in [k for k in per_query[0] if k != "id"] if per_query else []:
        vals = [r[key] for r in per_query]
        name = "mrr@10" if key == "rr" else key
        summary[name] = round(mean(vals), 4)
        if key in ("rr", "recall@10", "ndcg@10"):
            lo, hi = bootstrap_ci(vals)
            summary[f"{name}_ci95"] = [round(lo, 4), round(hi, 4)]
    if lat:
        lat_sorted = sorted(lat)
        summary["latency_ms"] = {"p50": round(statistics.median(lat), 2),
                                 "p95": round(lat_sorted[int(0.95 * (len(lat) - 1))], 2),
                                 "p99": round(lat_sorted[int(0.99 * (len(lat) - 1))], 2)}
    return {"summary": summary, "per_query": per_query}
