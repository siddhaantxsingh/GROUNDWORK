# Changelog

## 0.1.0 — 2026-10-14
- Ingestion (Markdown, HTML, text, PDF with page numbers), three chunking strategies.
- BM25 (from scratch), LSA and hashing embeddings, pgvector storage, RRF and weighted fusion, RM3, feature reranker.
- Extractive grounded answers with citations; OpenAI-compatible provider (mock-tested only); grounding validation.
- Prompt-injection scanner, source fencing, output sanitiser.
- Multi-tenant FastAPI service with API keys, Redis cache and rate limiting, metrics, usage accounting.
- pystdlib evaluation dataset, retrieval/generation/injection benchmarks, regression gate.
- 13 defects found by the benchmark, an adversarial audit and a downstream browser test, fixed with regression tests (docs/audit.md).
