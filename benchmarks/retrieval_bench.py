"""Reproducible retrieval + generation benchmark on the pystdlib dataset.

Protocol
  1. chunking ablation on the DEV split (BM25, default parameters)
  2. parameter tuning on DEV only (BM25 k1/b, LSA dim, fusion weight, RM3,
     reranker weights)
  3. every configuration reported on the held-out TEST split, with 95 %
     bootstrap CIs and a paired bootstrap p-value against the BM25 baseline
  4. grounded generation (extractive provider) on TEST: abstention,
     groundedness, citation precision, citation hit rate
  5. pgvector HNSW vs exact search: recall@10 and latency (needs PostgreSQL)

usage: python benchmarks/retrieval_bench.py OUT_DIR [--pg URL] [--update-baseline]
"""
from __future__ import annotations

import itertools
import json
import os
import platform
import statistics
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from groundwork.chunking import ChunkSpec  # noqa: E402
from groundwork.evaluation.metrics import mean, paired_bootstrap_pvalue  # noqa: E402
from groundwork.evaluation.retrieval_eval import Dataset, build_corpus, evaluate, unit_id  # noqa: E402
from groundwork.generate import ExtractiveProvider, build_sources, check_grounding  # noqa: E402
from groundwork.retrieve import RerankWeights, RetrievalConfig, retrieve  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "pystdlib"


def env() -> dict:
    sha = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
    import numpy
    import scipy

    return {"git": sha, "python": platform.python_version(), "numpy": numpy.__version__, "scipy": scipy.__version__,
            "cpu": platform.processor() or platform.machine(), "cpus": os.cpu_count(), "date": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}


def summ(res: dict) -> dict:
    s = res["summary"]
    return {k: s[k] for k in ("config", "queries", "mrr@10", "mrr@10_ci95", "recall@1", "recall@5", "recall@10", "recall@10_ci95",
                              "ndcg@10", "ndcg@10_ci95", "latency_ms")}


def main(out: Path, pg: str | None, update_baseline: bool) -> None:
    out.mkdir(parents=True, exist_ok=True)
    ds = Dataset.load(DATA)
    log = {"env": env(), "dataset": json.loads((DATA / "manifest.json").read_text())}

    # 1. chunking ablation (dev, BM25 defaults)
    ablation = []
    specs = [ChunkSpec("structure", 200, 0), ChunkSpec("structure", 100, 0), ChunkSpec("sentence", 200, 0),
             ChunkSpec("fixed", 200, 40), ChunkSpec("fixed", 100, 20)]
    for spec in specs:
        corpus, st = build_corpus(ds, spec, embedder=None)
        r = evaluate(corpus, ds, RetrievalConfig("bm25"), "dev")["summary"]
        ablation.append({"chunking": f"{spec.strategy}-{spec.size}/{spec.overlap}", "chunks": st["chunks"],
                         "mrr@10": r["mrr@10"], "recall@10": r["recall@10"], "ndcg@10": r["ndcg@10"]})
        print("ablation", ablation[-1], flush=True)
    log["chunking_ablation_dev"] = ablation
    best_spec = specs[max(range(len(specs)), key=lambda i: ablation[i]["ndcg@10"])]

    # 2. tuning on dev
    tuning = {}
    corpus, st = build_corpus(ds, best_spec, embedder=None)
    grid = []
    for k1, b in itertools.product([0.6, 0.9, 1.2, 1.5, 2.0], [0.3, 0.5, 0.75, 0.9]):
        corpus.bm25.k1, corpus.bm25.b = k1, b
        r = evaluate(corpus, ds, RetrievalConfig("bm25"), "dev")["summary"]
        grid.append({"k1": k1, "b": b, "ndcg@10": r["ndcg@10"]})
    best_bm25 = max(grid, key=lambda g: (g["ndcg@10"], -abs(g["k1"] - 1.2)))
    tuning["bm25_grid"] = grid
    tuning["bm25_best"] = best_bm25
    print("bm25 best", best_bm25, flush=True)

    dims = []
    for dim in (128, 256, 384):
        c, _ = build_corpus(ds, best_spec, embedder="lsa", dim=dim)
        r = evaluate(c, ds, RetrievalConfig("dense"), "dev")["summary"]
        dims.append({"dim": dim, "ndcg@10": r["ndcg@10"]})
    best_dim = max(dims, key=lambda d: d["ndcg@10"])["dim"]
    tuning["lsa_dim"] = dims
    print("lsa dims", dims, flush=True)

    lsa, st_lsa = build_corpus(ds, best_spec, embedder="lsa", dim=best_dim)
    lsa.bm25.k1, lsa.bm25.b = best_bm25["k1"], best_bm25["b"]
    hashing, _ = build_corpus(ds, best_spec, embedder="hashing", dim=384)
    hashing.bm25.k1, hashing.bm25.b = best_bm25["k1"], best_bm25["b"]
    log["index_build"] = {"lsa": st_lsa}

    fw = []
    for w in (0.1, 0.2, 0.3, 0.5):
        r = evaluate(lsa, ds, RetrievalConfig("hybrid", fusion="weighted", dense_weight=w), "dev")["summary"]
        fw.append({"dense_weight": w, "ndcg@10": r["ndcg@10"]})
    best_w = max(fw, key=lambda x: x["ndcg@10"])["dense_weight"]
    tuning["fusion_weight"] = fw

    rr = []
    for cov, prox, head, dense in itertools.product([0.0, 0.5], [0.0, 0.3], [0.0, 0.4, 0.8], [0.0, 0.5]):
        w = RerankWeights(1.0, cov, prox, head, dense)
        r = evaluate(lsa, ds, RetrievalConfig("bm25", rerank=True, rerank_weights=w), "dev")["summary"]
        rr.append({"weights": w.__dict__, "ndcg@10": r["ndcg@10"]})
    best_rr = RerankWeights(**max(rr, key=lambda x: x["ndcg@10"])["weights"])
    tuning["rerank"] = rr
    tuning["rerank_best"] = best_rr.__dict__
    log["tuning_dev"] = tuning
    print("rerank best", best_rr, flush=True)

    # 3. test split
    configs = [
        ("bm25 (default k1=1.2,b=0.75)", None, RetrievalConfig("bm25")),
        ("bm25 (tuned)", "lsa", RetrievalConfig("bm25")),
        ("dense hashing-384", "hashing", RetrievalConfig("dense")),
        (f"dense lsa-{best_dim}", "lsa", RetrievalConfig("dense")),
        ("hybrid rrf", "lsa", RetrievalConfig("hybrid")),
        (f"hybrid weighted w={best_w}", "lsa", RetrievalConfig("hybrid", fusion="weighted", dense_weight=best_w)),
        ("bm25 + rm3", "lsa", RetrievalConfig("bm25", rewrite="rm3")),
        ("bm25 + rerank (tuned)", "lsa", RetrievalConfig("bm25", rerank=True, rerank_weights=best_rr)),
        (f"hybrid weighted + rerank", "lsa", RetrievalConfig("hybrid", fusion="weighted", dense_weight=best_w, rerank=True, rerank_weights=best_rr)),
    ]
    default_corpus, _ = build_corpus(ds, best_spec, embedder=None)
    corpora = {None: default_corpus, "lsa": lsa, "hashing": hashing}
    results, per_q = [], {}
    for name, cname, cfg in configs:
        res = evaluate(corpora[cname], ds, cfg, "test")
        per_q[name] = res["per_query"]
        row = summ(res)
        row["name"] = name
        results.append(row)
        print("test", name, row["ndcg@10"], row["mrr@10"], row["recall@10"], flush=True)
    base = [q["ndcg@10"] for q in per_q[configs[0][0]]]
    for row in results:
        mine = [q["ndcg@10"] for q in per_q[row["name"]]]
        row["p_vs_bm25_default_ndcg@10"] = round(paired_bootstrap_pvalue(mine, base), 4) if row["name"] != configs[0][0] else None
    log["test_results"] = results

    # 4. generation on test (extractive provider over the best retrieval config)
    best = max(results, key=lambda r: r["ndcg@10"])
    best_cfg = dict((n, c) for n, _, c in configs)[best["name"]]
    best_corpus = corpora[dict((n, cn) for n, cn, _ in configs)[best["name"]]]
    prov = ExtractiveProvider()
    gen = {"abstained": 0, "answered": 0, "grounded": [], "cit_precision": [], "cites_relevant": 0, "latency_ms": []}
    for q in ds.split("test"):
        rel = set(ds.qrels[q["id"]])
        t0 = time.perf_counter()
        hits = retrieve(best_corpus, q["text"], 5, best_cfg)
        sources, _ = build_sources(hits)
        ans = prov.generate(q["text"], sources)
        g = check_grounding(ans)
        gen["latency_ms"].append((time.perf_counter() - t0) * 1e3)
        if ans.abstained:
            gen["abstained"] += 1
            continue
        gen["answered"] += 1
        gen["grounded"].append(g.groundedness)
        gen["cit_precision"].append(g.citation_precision)
        cited = {unit_id(s.doc_id, s.section) for i, ns in ans.citations.items() for n in ns for s in sources if s.n == n}
        gen["cites_relevant"] += bool(cited & rel)
    n = gen["abstained"] + gen["answered"]
    lat = sorted(gen["latency_ms"])
    log["generation_test"] = {
        "provider": prov.name, "retrieval": best["name"], "queries": n,
        "abstention_rate": round(gen["abstained"] / n, 4),
        "groundedness_mean_answered": round(mean(gen["grounded"]), 4),
        "citation_precision_mean_answered": round(mean(gen["cit_precision"]), 4),
        "answers_citing_relevant_section": round(gen["cites_relevant"] / max(1, gen["answered"]), 4),
        "end_to_end_latency_ms": {"p50": round(statistics.median(lat), 2), "p95": round(lat[int(0.95 * (len(lat) - 1))], 2),
                                  "p99": round(lat[int(0.99 * (len(lat) - 1))], 2)},
        "note": "groundedness/citation precision use the lexical support proxy in generate.support_score, not an NLI model",
    }
    print("generation", log["generation_test"], flush=True)

    # 5. pgvector ANN vs exact
    if pg:
        log["pgvector"] = pgvector_bench(pg, lsa, ds, best_dim)
        print("pgvector", log["pgvector"], flush=True)

    (out / "retrieval_bench.json").write_text(json.dumps(log, indent=2))
    if update_baseline:
        bl = {r["name"]: {"ndcg@10": r["ndcg@10"], "mrr@10": r["mrr@10"], "recall@10": r["recall@10"]} for r in results}
        bl["_protocol"] = {"chunking": best_spec.__dict__, "bm25": best_bm25, "lsa_dim": best_dim, "fusion_weight": best_w,
                           "rerank": best_rr.__dict__, "split": "test", "source_run": str(out)}
        (ROOT / "benchmarks" / "baseline.json").write_text(json.dumps(bl, indent=2))


def pgvector_bench(url: str, corpus, ds, dim: int) -> dict:
    import uuid

    import numpy as np
    import psycopg
    from pgvector.psycopg import register_vector

    name = "gw_bench_" + uuid.uuid4().hex[:8]
    with psycopg.connect(url, autocommit=True) as a:
        a.execute(f"CREATE DATABASE {name}")
    try:
        with psycopg.connect(url.rsplit("/", 1)[0] + "/" + name, autocommit=True) as c:
            c.execute("CREATE EXTENSION vector")
            register_vector(c)
            ids, m = corpus._matrix()
            c.execute(f"CREATE TABLE v (id text PRIMARY KEY, e vector({m.shape[1]}))")
            with c.cursor() as cur:
                cur.executemany("INSERT INTO v VALUES (%s, %s)", [(i, m[k]) for k, i in enumerate(ids)])
            t0 = time.perf_counter()
            c.execute("CREATE INDEX ON v USING hnsw (e vector_cosine_ops) WITH (m = 16, ef_construction = 64)")
            build_s = time.perf_counter() - t0
            out = {"vectors": len(ids), "dim": int(m.shape[1]), "hnsw_build_s": round(build_s, 3), "runs": []}
            qs = [q["text"] for q in ds.split("test")]
            qv = corpus.embedder.embed(qs)
            exact = [set(np.array(ids)[np.argsort(-(m @ q))[:10]]) for q in qv]
            for ef in (10, 40, 100, 200):
                c.execute(f"SET hnsw.ef_search = {ef}")
                lat, rec = [], []
                for q, ex in zip(qv, exact):
                    t = time.perf_counter()
                    got = {r[0] for r in c.execute("SELECT id FROM v ORDER BY e <=> %s LIMIT 10", (q,)).fetchall()}
                    lat.append((time.perf_counter() - t) * 1e3)
                    rec.append(len(got & ex) / 10)
                lat.sort()
                out["runs"].append({"ef_search": ef, "recall@10_vs_exact": round(mean(rec), 4),
                                    "p50_ms": round(statistics.median(lat), 3), "p95_ms": round(lat[int(0.95 * (len(lat) - 1))], 3)})
            # exact scan for reference (sequential scan, index disabled)
            c.execute("SET enable_indexscan = off")
            lat = []
            for q in qv[:100]:
                t = time.perf_counter()
                c.execute("SELECT id FROM v ORDER BY e <=> %s LIMIT 10", (q,)).fetchall()
                lat.append((time.perf_counter() - t) * 1e3)
            out["exact_seqscan_p50_ms"] = round(statistics.median(lat), 3)
            return out
    finally:
        with psycopg.connect(url, autocommit=True) as a:
            a.execute(f"DROP DATABASE IF EXISTS {name} WITH (FORCE)")


if __name__ == "__main__":
    args = sys.argv[1:]
    pg = args[args.index("--pg") + 1] if "--pg" in args else None
    main(Path(args[0]), pg, "--update-baseline" in args)
