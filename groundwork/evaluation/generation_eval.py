"""Generation evaluation: deterministic metrics only (no LLM judge, ADR 0003).

Per answered query:
  groundedness          supported sentences / sentences (lexical support proxy, generate.check_grounding)
  citation_precision    citations whose source supports the sentence / all citations
  cites_relevant        the answer cites a chunk from the labelled relevant section ("citation correctness")
  answer_relevance      cosine similarity between the question (search_query:) and the answer text with
                        citation markers removed (search_document:), using an embedding model. A semantic
                        proxy, not a human judgement. Reported only when an embedder is given.
  query_term_coverage   share of the question's content terms that appear in the answer (lexical relevance)
Per query: abstained, latency, tokens.
"""
from __future__ import annotations

import re
import statistics
import time

import numpy as np

from ..embed import embed_queries
from ..generate import _CITE, build_sources, check_grounding
from ..retrieve import retrieve
from ..text import tokenize
from .metrics import bootstrap_ci, mean
from .retrieval_eval import unit_id

_WS = re.compile(r"\s+")


def strip_citations(text: str) -> str:
    return _WS.sub(" ", _CITE.sub("", text)).strip()


def answer_relevance(embedder, questions: list[str], answers: list[str]) -> list[float]:
    if not questions:
        return []
    q = embed_queries(embedder, questions)
    a = embedder.embed([strip_citations(x) for x in answers])
    return [float(x) for x in np.sum(q * a, axis=1)]


def query_term_coverage(question: str, answer: str) -> float:
    q = set(tokenize(question))
    return len(q & set(tokenize(strip_citations(answer)))) / len(q) if q else 0.0


def pct(xs: list[float], p: float) -> float:
    s = sorted(xs)
    return s[int(p * (len(s) - 1))] if s else float("nan")


def evaluate_generation(corpus, ds, queries: list[dict], cfg, provider, k: int = 5, max_sources: int = 4,
                        relevance_embedder=None, keep_answers: bool = True) -> dict:
    rows = []
    for q in queries:
        rel = set(ds.qrels[q["id"]])
        t0 = time.perf_counter()
        hits = retrieve(corpus, q["text"], k, cfg)
        t1 = time.perf_counter()
        sources, excluded = build_sources(hits, max_sources=max_sources)
        ans = provider.generate(q["text"], sources)
        t2 = time.perf_counter()
        g = check_grounding(ans)
        cited = {unit_id(s.doc_id, s.section) for ns in ans.citations.values() for n in ns for s in sources if s.n == n}
        retrieved_rel = any(unit_id(h.chunk.doc_id, h.chunk.section) in rel for h in hits)
        row = {"id": q["id"], "abstained": ans.abstained, "retrieve_ms": (t1 - t0) * 1e3, "generate_ms": (t2 - t1) * 1e3,
               "total_ms": (t2 - t0) * 1e3, "tokens_in": ans.usage.get("tokens_in", 0), "tokens_out": ans.usage.get("tokens_out", 0),
               "relevant_in_context": retrieved_rel}
        if not ans.abstained:
            row.update(groundedness=g.groundedness, citation_precision=g.citation_precision, sentences=g.sentences,
                       uncited=g.uncited, cites_relevant=bool(cited & rel),
                       query_term_coverage=query_term_coverage(q["text"], ans.text))
        raw = ans.usage.get("raw_grounding")
        if raw is not None:
            row["raw_groundedness"] = raw["groundedness"]
            row["raw_citation_precision"] = raw["citation_precision"]
            row["dropped_sentences"] = ans.usage.get("dropped_sentences", 0)
            row["auto_attributed"] = ans.usage.get("auto_attributed_sentences", 0)
        row["question"] = q["text"]
        row["answer"] = ans.text
        if keep_answers:
            if "raw_answer" in ans.usage:
                row["raw_answer"] = ans.usage["raw_answer"]
        rows.append(row)
    answered = [r for r in rows if not r["abstained"]]
    if relevance_embedder is not None and answered:
        rel_scores = answer_relevance(relevance_embedder, [r["question"] for r in answered], [r["answer"] for r in answered])
        for r, s in zip(answered, rel_scores):
            r["answer_relevance"] = s
    n = len(rows)

    def m(key, src=answered):
        vals = [r[key] for r in src if r.get(key) is not None]
        if not vals:
            return None
        lo, hi = bootstrap_ci([float(v) for v in vals])
        return {"mean": round(mean([float(v) for v in vals]), 4), "ci95": [round(lo, 4), round(hi, 4)], "n": len(vals)}

    gen = [r["generate_ms"] for r in rows]
    tot = [r["total_ms"] for r in rows]
    summary = {
        "provider": provider.name, "retrieval": cfg.label(), "queries": n, "answered": len(answered),
        "abstention_rate": round(1 - len(answered) / n, 4) if n else None,
        "relevant_section_in_context": round(mean([float(r["relevant_in_context"]) for r in rows]), 4) if rows else None,
        "groundedness": m("groundedness"), "citation_precision": m("citation_precision"),
        "citation_correctness_cites_relevant": m("cites_relevant"),
        "citation_correctness_over_all_queries": round(sum(bool(r.get("cites_relevant")) for r in rows) / n, 4) if n else None,
        "answer_relevance_embedding": m("answer_relevance"), "query_term_coverage": m("query_term_coverage"),
        "raw_groundedness_before_enforcement": m("raw_groundedness", rows),
        "raw_citation_precision_before_enforcement": m("raw_citation_precision", rows),
        "generate_ms": {"p50": round(statistics.median(gen), 1), "p95": round(pct(gen, 0.95), 1), "mean": round(mean(gen), 1)} if gen else None,
        "end_to_end_ms": {"p50": round(statistics.median(tot), 1), "p95": round(pct(tot, 0.95), 1)} if tot else None,
        "tokens_in_mean": round(mean([r["tokens_in"] for r in rows]), 1) if rows else None,
        "tokens_out_mean": round(mean([r["tokens_out"] for r in rows]), 1) if rows else None,
    }
    return {"summary": summary, "per_query": rows}
