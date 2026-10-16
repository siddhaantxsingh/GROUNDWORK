# Testing

`pytest` (PostgreSQL with pgvector on 127.0.0.1:5432 and Redis on 6379 db 15 required; each test creates and drops its own database).

| File | What it covers | Kind |
|---|---|---|
| `test_core.py` | tokenizer/stemmer, Markdown/HTML/PDF parsing with page numbers, bad inputs, chunking (no word lost, page-bounded, never crossing sections), BM25 against the formula, delete ≡ never-added, deterministic ties, filters before top-k, dense vs brute force, LSA determinism, RRF/weighted fusion, RM3, metrics | unit + property (Hypothesis) |
| `test_generation_safety.py` | extractive answers, abstention, fabricated/wrong/uncited sentence detection, joint citations, OpenAI-compatible provider via mock transport (fencing, key handling, cost, invalid citations), injection detector on a labelled set, context exclusion, fence spoofing, output sanitising, D1/D2 regressions | unit |
| `test_api.py` | real PostgreSQL + Redis: upload → grounded answer with page reference, idempotent re-upload, tenant isolation, delete + cache invalidation, auth/401, rate limit/429, 413/422 limits, Redis outage degradation, restart persistence, atomic ingest under failure, LSA refit consistency and pgvector agreement, injected document exclusion, usage/metrics | integration + fault injection |
| `test_audit_regressions.py` | A1–A9 audit findings | regression |
| `test_regression.py` | retrieval quality on the pystdlib test split must not drop more than 0.01 below `benchmarks/baseline.json` | quality gate |

Latest local run: `test-logs/pytest-2026-10-14.txt`.
