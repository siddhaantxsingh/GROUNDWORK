# Groundwork

Groundwork is a retrieval and grounded-answer engine. Its main focus is measuring retrieval quality and citation grounding, not just serving answers. It ingests Markdown, HTML, text and PDF (with page numbers). It retrieves with BM25 (written from scratch), dense vectors (pgvector) or a hybrid of the two. It returns answers whose every sentence cites a source chunk, by document, page and section, and it checks each citation. It also ships with a reproducible evaluation harness, a regression gate, and an adversarial review of its own defects.

**Status:**
- **Done:** the core engine and service, verified locally. 81 tests pass against real PostgreSQL + pgvector and Redis (CI runs them on GitHub Actions). 5 more opt-in tests load real models (passed locally).
- **New (2026-10-15):** opt-in local models through llama.cpp on CPU: nomic-embed-text-v1.5 embeddings, a Qwen2.5-0.5B / SmolLM2 answer provider, and a Qwen3 reranker. Benchmarked on a sub-corpus; see [Real local models](docs/benchmarks.md#real-local-models-2026-10-15).
- **Not done:** not deployed; no real users; the neural reranker's quality was not measured (too slow on the shared CPU).

## What it does

```
upload ──► parse (page/section aware) ──► chunk (never crosses a page) ──► embed ──► PostgreSQL + pgvector (one transaction)
query  ──► [RM3 expansion] ──► BM25 ∥ dense ──► RRF / weighted fusion ──► [feature reranker]
       ──► injection scan + source fencing ──► provider (extractive | local llama.cpp | OpenAI-compatible) ──► grounding check / enforcement ──► answer + citations
```

- **Multi-tenant HTTP API (FastAPI).** API keys map to tenants. Endpoints:
  - upload, list and delete documents (deleting a document removes its data from the database);
  - query;
  - usage accounting (latency, tokens, cost);
  - health, and Prometheus metrics.
- **Redis.** Used for a query cache, invalidated per tenant on every change, and for rate limits. Both degrade safely when Redis is down.
- **Evaluation.**
  - Retrieval metrics: Recall@K, MRR, NDCG, with bootstrap confidence intervals and paired tests.
  - Generation metrics: groundedness, citation precision, abstention rate, and whether the answer cites the relevant section.
  - Prompt-injection robustness.
  - Latency percentiles.
  - Retrieval and generation are evaluated separately. No LLM judge is used.

## Core algorithms (implemented here, not wrapped)

| Area | Implementation |
|---|---|
| Lexical retrieval | Inverted index with Okapi BM25 (Lucene IDF). Supports incremental add and delete; a property test checks that deleting a document gives the same scores as never adding it. |
| Dense retrieval | LSA (TF-IDF + truncated SVD, fitted per tenant) or signed feature hashing by default; opt-in nomic-embed-text-v1.5 (with its `search_query:` / `search_document:` prefixes) through llama.cpp. pgvector HNSW is benchmarked against exact search. |
| Fusion | Reciprocal rank fusion, and min-max weighted fusion. Metadata filters are applied before top-k. |
| Query rewriting | RM3 pseudo-relevance feedback (relevance model interpolated with the original query). |
| Reranking | Linear model over first-stage score, query-term coverage, minimal covering window (proximity), heading match and dense similarity, tuned on dev. Opt-in Qwen3-Reranker-0.6B (P(yes) of its judge prompt) over the top k. |
| Grounding | Each answer sentence carries citations. Each citation is checked for lexical support of its sentence; uncited, unsupported and wrongly cited sentences are reported. For LLM output, enforcement removes unsupported sentences (and abstains if none are left). |
| Safety | Injection scanner (after NFKC normalisation and removal of zero-width characters). Untrusted sources are fenced so delimiter look-alikes can't escape. Output is sanitised so links and images can't exfiltrate data. |

## Results (pystdlib test split, 316 queries — full tables in [docs/benchmarks.md](docs/benchmarks.md))

| Configuration | NDCG@10 [95 % CI] | MRR@10 | Recall@10 |
|---|---|---|---|
| BM25, default parameters | 0.470 [0.429, 0.512] | 0.404 | 0.677 |
| BM25, tuned on dev | 0.528 [0.483, 0.571] | 0.472 | 0.703 |
| BM25 + RM3 | 0.549 [0.507, 0.590] | 0.484 | **0.753** |
| BM25 + reranker | **0.550** [0.506, 0.592] | **0.494** | 0.725 |
| Dense LSA-384 | 0.351 [0.311, 0.390] | 0.283 | 0.570 |
| Hybrid (RRF) | 0.464 [0.422, 0.504] | 0.389 | 0.703 |

What the results show:

- On this dataset, tuned BM25 with RM3 or the reranker is best. The confidence intervals of the top configurations overlap.
- The offline dense retrievers are weak, and RRF with them does not help. That conclusion does not transfer to neural embedders.
- The extractive answer provider (over BM25 + reranker):
  - abstains on 6.0 % of test queries;
  - cites the labelled relevant section in 42 % of the answers it gives;
  - takes 5.8 ms end to end at the median.
- pgvector HNSW reaches recall@10 of at least 0.993 against exact search at `ef_search` ≥ 40.
- Prompt injection:
  - known-style injections were all kept out of the context (200/200);
  - **paraphrased injections were not detected at all (0/200)** and reached 6 % of extractive answers;
  - the detector is defence in depth, not a security boundary.

The dataset was built automatically from CPython standard-library docstrings ([how](docs/benchmarks.md#dataset-pystdlib-known-item-retrieval)). It is checked in, so results do not depend on the local Python version.

## Real local models (opt-in)

Results on a 31-document sub-corpus (80 test queries) of the same dataset, on a shared, overloaded 4 vCPU machine ([details](docs/benchmarks.md#real-local-models-2026-10-15)):

| Configuration | NDCG@10 | Recall@10 |
|---|---|---|
| BM25 (tuned) | 0.627 | 0.825 |
| dense LSA-384 | 0.505 | 0.775 |
| dense nomic-embed-text-v1.5 | 0.683 | 0.925 |
| hybrid RRF (nomic) | 0.700 | 0.913 |
| hybrid (nomic) + feature reranker | **0.710** | 0.913 |

- Neural embeddings help, and fusing them with BM25 is significantly better than BM25 alone (p = 0.005). Query embedding was slow on the busy machine (median about 3.5 s).
- **Small LLMs wrote poorly grounded answers:** only 15 % of Qwen2.5-0.5B's sentences were supported by their citations (SmolLM2-360M: 0 %). With grounding enforcement every shown sentence is supported, but Qwen then abstains on 65 % of queries. The extractive provider remains the better default.
- Prompt injection (10 queries per family): fencing and the system prompt alone did not stop Qwen2.5-0.5B (6/10 known-style attacks succeeded); with all defences 0/10 in both families.

```bash
pip install -e '.[local]'                    # llama-cpp-python, builds llama.cpp (CPU)
python scripts/fetch_models.py               # GGUF files from Docker Hub ai/ into /home/user/models (GW_MODEL_DIR)
GW_RUN_LOCAL_MODELS=1 pytest tests/test_local_models.py
GW_DIM=768 GW_EMBEDDER=nomic GW_LLM_PROVIDER=llamacpp python -m groundwork serve   # see groundwork/config.py
```

## Build, test, run

```bash
pip install -e '.[dev]'                      # Python ≥ 3.11
# PostgreSQL with pgvector on 127.0.0.1:5432 (user postgres), Redis on 6379
pytest                                       # 81 tests (+5 opt-in local-model tests, skipped by default)
./scripts/demo.sh                            # real server: upload, grounded Q&A with page refs, abstention
python -m groundwork serve --port 8080       # see docs/deployment.md for configuration
python benchmarks/retrieval_bench.py OUT --pg postgresql://postgres@127.0.0.1:5432/postgres
```

## Engineering trade-offs

- **PostgreSQL is the source of truth; the query index is in memory.** This makes BM25, RM3 and the reranker explicit and fast. The cost is start-up time, memory, and one process per index ([ADR 0002](docs/decisions/0002-in-memory-query-index.md)).
- **Offline embedders by default, neural models opt-in** ([ADR 0001](docs/decisions/0001-dense-retrieval-without-pretrained-models.md)).
- **Deterministic evaluation; model judges never count as ground truth** ([ADR 0003](docs/decisions/0003-deterministic-evaluation.md)).
- **Chunks never cross a page**, so a citation always names exactly one page. The cost is a little extra fragmentation.
- **A lexical grounding check** instead of an NLI model: cheap and deterministic, but weaker ([limitations](docs/limitations.md)).

## Security assumptions

API keys are secrets that clients handle correctly. A tenant boundary corresponds to one API key. Retrieved documents are untrusted. The service runs behind TLS termination. See the threat model and measured limits in [docs/security.md](docs/security.md).

## Quality evidence

- [docs/testing.md](docs/testing.md): test inventory. The latest test log is in `test-logs/`.
- [docs/audit.md](docs/audit.md): 13 defects found by the benchmark, by an independent adversarial review, and by a downstream browser test (2 high, 8 medium or low-medium, 3 low). Each is fixed and has a regression test that fails on the old code.
- `tests/test_regression.py`: the retrieval-quality gate against `benchmarks/baseline.json`.

## Known limitations

These are summarised here; the full list is in [docs/limitations.md](docs/limitations.md).

- Neural results come from a 31-document sub-corpus and 20 generation queries on an overloaded shared CPU; latencies are pessimistic and noisy.
- The Qwen3 neural reranker works but its quality on the dataset was not measured (too slow here).
- The small LLMs tested (0.5B and 360M) are weak; the OpenAI-compatible provider is still tested only with a mock.
- Groundedness is a lexical proxy; injection detection is pattern-based.
- One known-item dataset; no multi-hop evaluation. Single process. No real users; not deployed.

## Roadmap

1. Re-run the neural benchmarks on the full corpus and measure the Qwen3 reranker on an idle machine.
2. Evaluate a larger LLM (e.g. Qwen2.5-3B or a hosted model) and add an NLI-based support model.
3. Add a second dataset with multi-hop and unanswerable questions.
4. Shared index across replicas, and pgvector on the query path.
5. Add a model-based injection classifier alongside the patterns, evaluated on a held-out paraphrase set.

## Scorecard (2026-10-15, self-assessed)

| Dimension | Score | Why not higher |
|---|---|---|
| Fresher-portfolio strength | 8/10 | Strong evaluation story, but one dataset and no real users. |
| Engineering maturity | 7/10 | Good tests and CI, but single process and a lexical grounding check. |
| Deployment readiness | 5/10 | Docker image built and smoke-tested; never deployed, no TLS or operations runbook exercised. |
| Completion of intended scope | 7/10 | Neural embedder and LLM evaluated only on a sub-corpus; neural reranker quality not measured. |

License: not yet chosen by the owner.
