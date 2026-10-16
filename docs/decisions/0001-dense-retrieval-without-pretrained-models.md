# ADR 0001 — Dense retrieval without pretrained models

Status: accepted (2026-10-14)

Context: the build environment cannot reach huggingface.co, so no pretrained sentence-embedding model can be downloaded, and inventing results for one is not acceptable.

Decision: ship two dense retrievers that can be built offline — signed feature hashing (no training) and LSA (TF-IDF + truncated SVD fitted per tenant) — behind an `Embedder` protocol. Benchmarks label them precisely. A neural model plugs in by implementing `embed(texts) -> L2-normalised float32 rows`.

Consequences: on the pystdlib benchmark, dense retrieval is weaker than BM25 and fusion gains are small; conclusions about "hybrid retrieval" here do not transfer to neural embedders and are stated that way.

## Update 2026-10-15

Pretrained GGUF models became reachable through Docker Hub (`ai/` namespace). nomic-embed-text-v1.5 is now available as an opt-in embedder (`GW_EMBEDDER=nomic`); LSA and hashing stay the defaults so CI and the default install need no model files. See docs/benchmarks.md, "Real local models".
