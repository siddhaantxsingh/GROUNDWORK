"""Retrieval-quality regression gate.

Re-runs selected configurations on the pystdlib TEST split with the tuned
protocol recorded in benchmarks/baseline.json and fails if quality drops by
more than the tolerance. The dataset is checked in (data/pystdlib), so the
gate does not depend on the local Python version.
"""
import json
from pathlib import Path

import pytest

from groundwork.chunking import ChunkSpec
from groundwork.evaluation.retrieval_eval import Dataset, build_corpus, evaluate
from groundwork.retrieve import RerankWeights, RetrievalConfig

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "benchmarks" / "baseline.json"
TOLERANCE = 0.01


@pytest.fixture(scope="module")
def setup():
    if not BASELINE.exists():
        pytest.skip("no baseline recorded")
    bl = json.loads(BASELINE.read_text())
    p = bl["_protocol"]
    ds = Dataset.load(ROOT / "data" / "pystdlib")
    corpus, _ = build_corpus(ds, ChunkSpec(**p["chunking"]), embedder="lsa", dim=p["lsa_dim"])
    corpus.bm25.k1, corpus.bm25.b = p["bm25"]["k1"], p["bm25"]["b"]
    return bl, p, ds, corpus


@pytest.mark.parametrize("name,make", [
    ("bm25 (tuned)", lambda p: RetrievalConfig("bm25")),
    ("bm25 + rm3", lambda p: RetrievalConfig("bm25", rewrite="rm3")),
    ("bm25 + rerank (tuned)", lambda p: RetrievalConfig("bm25", rerank=True, rerank_weights=RerankWeights(**p["rerank"]))),
])
def test_no_quality_regression(setup, name, make):
    bl, p, ds, corpus = setup
    got = evaluate(corpus, ds, make(p), "test")["summary"]
    for metric in ("ndcg@10", "mrr@10", "recall@10"):
        assert got[metric] >= bl[name][metric] - TOLERANCE, f"{name} {metric}: {got[metric]} < baseline {bl[name][metric]}"
