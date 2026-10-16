"""Command line: `python -m groundwork <command>`

  serve [--host H] [--port P]          run the HTTP API (env: GW_DATABASE_URL, GW_API_KEYS, GW_REDIS_URL;
                                       optional local models: see groundwork/config.py)
  migrate                              create / check the schema
  ingest TENANT PATH...                ingest files or directories into a tenant
  query TENANT "question"              ask a question (prints JSON)
  eval-retrieval DATASET [--split S] [--mode bm25|dense|hybrid] [--rerank] [--save]
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path


def _engine():
    from .engine import Engine, EngineConfig
    from .store import Store, connect, migrate

    conn = connect(os.environ["GW_DATABASE_URL"])
    from .config import apply_to_engine_config, provider_from_env

    cfg = apply_to_engine_config(EngineConfig(dim=int(os.environ.get("GW_DIM", "256"))))
    migrate(conn, cfg.dim)
    return Engine(Store(conn), cfg, provider=provider_from_env())


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    cmd, args = argv[0], argv[1:]
    if cmd == "serve":
        import uvicorn

        from .api import create_app

        host = args[args.index("--host") + 1] if "--host" in args else "127.0.0.1"
        port = int(args[args.index("--port") + 1]) if "--port" in args else 8080
        uvicorn.run(create_app(), host=host, port=port, log_level="info")
        return 0
    if cmd == "migrate":
        _engine()
        print("schema ok")
        return 0
    if cmd == "ingest":
        eng = _engine()
        tenant, paths = args[0], [Path(p) for p in args[1:]]
        files = [f for p in paths for f in (sorted(p.rglob("*")) if p.is_dir() else [p]) if f.is_file()]
        for f in files:
            try:
                info = eng.ingest(tenant, f.name, f.read_bytes())
                print(json.dumps({"file": str(f), **info}))
            except ValueError as e:
                print(json.dumps({"file": str(f), "error": str(e)}), file=sys.stderr)
        return 0
    if cmd == "query":
        print(json.dumps(_engine().query(args[0], args[1]), indent=2))
        return 0
    if cmd == "eval-retrieval":
        from .chunking import ChunkSpec
        from .evaluation.retrieval_eval import Dataset, build_corpus, evaluate
        from .retrieve import RetrievalConfig

        ds = Dataset.load(args[0])
        split = args[args.index("--split") + 1] if "--split" in args else "dev"
        mode = args[args.index("--mode") + 1] if "--mode" in args else "bm25"
        corpus, _ = build_corpus(ds, ChunkSpec("structure", 100, 0), embedder="lsa" if mode != "bm25" else None, dim=384)
        res = evaluate(corpus, ds, RetrievalConfig(mode, rerank="--rerank" in args), split)
        print(json.dumps(res["summary"], indent=2))
        if "--save" in args:
            from .store import Store, connect

            rid = Store(connect(os.environ["GW_DATABASE_URL"])).save_eval_run(str(ds.root), {"mode": mode, "split": split},
                                                                               res["summary"], res["per_query"])
            print(f"saved eval run {rid}")
        return 0
    print(f"unknown command {cmd!r}\n{__doc__}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
