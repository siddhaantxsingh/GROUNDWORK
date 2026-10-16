# Owner actions

Steps only the owner can do. Each lists the command, what to expect and what to save.

1. **Re-run the neural benchmark on an idle machine (full corpus).**
   `pip install -e '.[local]' && python scripts/fetch_models.py && python benchmarks/neural_bench.py benchmarks/results/<date>-full retrieval --every 1 --vector-cache /tmp/gw-vc`
   Expect: `retrieval.json` with all 316 test queries; embedding 3401 chunks takes minutes on an idle 4-core CPU (hours on the shared one used here). Save the JSON and `uptime` output, then update docs/benchmarks.md.
2. **Measure the Qwen3 reranker.** Same command with `--rerank-n 100`. Expect a `reranker_subset` block in the JSON. Save it.
3. **Try a larger LLM** (e.g. `python scripts/fetch_models.py ai/qwen2.5:3B-F16` then `GW_LLM_GGUF=/home/user/models/qwen2.5-3B-F16.gguf`) and re-run the `generation` part. Save `generation.json`.
4. **Run the compose stack** once on a machine with disk to spare: `POSTGRES_PASSWORD=... GW_API_KEYS="acme:<24+ chars>" docker compose up --build`, then the curl commands in docs/deployment.md. Save the output.
5. **Choose a licence** for the repository.
