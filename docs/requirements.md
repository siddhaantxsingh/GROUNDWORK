# Requirements matrix — Project 10 (Production RAG + Evaluation Engine)

| Requirement | Status | Evidence |
|---|---|---|
| Document ingestion | VERIFIED | `ingest.py`; `test_core.py` parsing tests; API upload tests |
| Structured parsing (sections, pages) | VERIFIED | Markdown/HTML sections, PDF pages; `test_a4`, `test_a5`, `test_pdf_page_numbers_are_preserved` |
| Chunking strategies | VERIFIED | structure / sentence / fixed; property tests; ablation in docs/benchmarks.md |
| Embedding pipelines | VERIFIED | LSA + hashing (default) with atomic refit; opt-in nomic-embed-text-v1.5 via llama.cpp with query/document prefixes and re-embed on model switch (`test_model_hooks.py`, `test_local_models.py`, `docs/evidence/2026-10-15/pytest-localmodel.log`) |
| BM25 | VERIFIED | from scratch; formula and delete-equivalence tests |
| Dense retrieval | VERIFIED | LSA/hashing on the full corpus; nomic on a 31-document sub-corpus (NDCG@10 0.683 vs LSA 0.505), `benchmarks/results/2026-10-15-neural/retrieval.json` |
| Hybrid retrieval | VERIFIED | RRF + weighted fusion; measured on test split |
| Reciprocal rank fusion | VERIFIED | `test_rrf_and_weighted_fusion`; benchmark |
| Reranking | VERIFIED (feature reranker); PARTIAL (neural) | feature reranker benchmarked; Qwen3-Reranker-0.6B implemented and unit-tested, quality NOT MEASURED (too slow on the shared CPU) |
| Query rewriting | VERIFIED | RM3; benchmark |
| Citation grounding | VERIFIED | per-sentence citations + validation; D1/D2 regressions |
| Page-level references | VERIFIED | page-bounded chunks; API test returns `pages: [2, 2]` for a PDF |
| Evaluation datasets | VERIFIED (one dataset) | pystdlib known-item, 634 queries, dev/test split |
| Retrieval regression tests | VERIFIED | `tests/test_regression.py` vs `benchmarks/baseline.json` |
| Groundedness evaluation | VERIFIED (lexical proxy) | `check_grounding`; NLI not implemented |
| Citation correctness | VERIFIED | citation precision + relevant-section citation rate |
| Latency / cost tracking | VERIFIED | per-stage timings, query_log, `/v1/usage`; cost computed from provider token usage (mock-tested) |
| Provider abstraction | VERIFIED (local LLM); mock only (OpenAI-compatible) | `LlamaCppProvider` with Qwen2.5-0.5B and SmolLM2-360M benchmarked (`generation.json`); grounding enforcement `GroundedProvider` |
| Prompt-injection testing | VERIFIED | unit tests + `injection_bench.py` (known 200/200 excluded; paraphrased 0/200); against Qwen2.5-0.5B: 6/10 known attacks succeed with prompt defences only, 0/10 with all defences (`injection.json`) |
| Recall@K, MRR, NDCG | VERIFIED | `metrics.py` tests; benchmark with CIs |
| Citation precision/recall | VERIFIED | benchmark (recall measured as relevant-section citation rate, single relevant unit) |
| Answer relevance | VERIFIED (embedding proxy) | `evaluation/generation_eval.py`: nomic question–answer cosine + query-term coverage; reported per provider |
| Hallucination rate | VERIFIED (lexical proxy) | unsupported-sentence rate of raw LLM output: 85 % (Qwen2.5-0.5B), 100 % (SmolLM2-360M), 20 queries |
| Separate retrieval vs generation evaluation | VERIFIED | separate sections of the benchmark |
| PostgreSQL + pgvector | VERIFIED | integration tests on PostgreSQL 16.15 + pgvector 0.6.0 |
| Redis | VERIFIED | cache + rate limit tests, outage degradation test |
| FastAPI service | VERIFIED | `test_api.py`, `scripts/demo.sh` log |
| CI | VERIFIED | `../.github/workflows/groundwork.yml` green on GitHub Actions (run 38478453668) |
| Container deployment | PARTIAL | default image built and smoke-tested (`docs/evidence/2026-10-15/docker-build.log`, `docker-smoke-default.log`); compose and the `LOCAL_MODELS=1` image not run |
| LICENSE | BLOCKED | owner decision |
