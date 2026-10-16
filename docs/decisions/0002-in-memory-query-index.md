# ADR 0002 — PostgreSQL as source of truth, in-memory query index

Status: accepted (2026-10-14)

Decision: documents, chunks and embeddings live in PostgreSQL (pgvector column + HNSW index). The BM25 inverted index and the dense matrix used at query time are rebuilt from PostgreSQL per tenant on first use and maintained incrementally on ingest/delete.

Why: BM25 with incremental deletes, RM3 and the reranker need term statistics that PostgreSQL full-text search does not expose in the needed form; keeping them in process makes the algorithms explicit and testable. pgvector's HNSW is kept for dense search at scale and benchmarked against exact search.

Consequences: start-up cost and memory grow with the corpus; multi-process deployments need a shared index (future work).
