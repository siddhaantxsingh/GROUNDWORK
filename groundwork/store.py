"""PostgreSQL + pgvector persistence (the source of truth).

Schema (created idempotently by `migrate`):
  documents   one row per ingested file; UNIQUE (tenant, sha256) makes
              ingestion idempotent (re-uploading the same bytes is a no-op)
  chunks      chunk text, provenance (pages, section) and the embedding
              (pgvector), ON DELETE CASCADE from documents
  embedders   serialized embedding model per tenant (LSA components), so a
              restart folds new queries into the same space
  eval_runs   evaluation results (config, summary, per-query rows)
  query_log   per-query latency / provider / token / cost accounting

Ingestion of a document (row + all chunks + embeddings) is one transaction:
a crash leaves either nothing or the complete document.
"""
from __future__ import annotations

import io
import json
import uuid
from dataclasses import dataclass

import numpy as np
import psycopg
from pgvector.psycopg import register_vector

from .retrieve import ChunkRecord

SCHEMA_VERSION = 1


def migrate(conn: psycopg.Connection, dim: int) -> None:
    with conn.transaction():
        conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
        conn.execute("CREATE TABLE IF NOT EXISTS schema_meta (key text PRIMARY KEY, value text NOT NULL)")
        row = conn.execute("SELECT value FROM schema_meta WHERE key = 'dim'").fetchone()
        if row and int(row[0]) != dim:
            raise RuntimeError(f"database was created for embedding dim {row[0]}, configured dim is {dim}; run reindex --dim")
        conn.execute(f"""
            CREATE TABLE IF NOT EXISTS documents (
              id uuid PRIMARY KEY,
              tenant text NOT NULL,
              name text NOT NULL,
              media_type text NOT NULL,
              sha256 text NOT NULL,
              page_count int NOT NULL,
              chunking jsonb NOT NULL,
              meta jsonb NOT NULL DEFAULT '{{}}',
              created_at timestamptz NOT NULL DEFAULT now(),
              UNIQUE (tenant, sha256)
            );
            CREATE TABLE IF NOT EXISTS chunks (
              id text PRIMARY KEY,
              doc_id uuid NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
              tenant text NOT NULL,
              ordinal int NOT NULL,
              text text NOT NULL,
              page_start int NOT NULL,
              page_end int NOT NULL,
              section text NOT NULL,
              embedding vector({dim})
            );
            CREATE INDEX IF NOT EXISTS chunks_doc ON chunks (doc_id);
            CREATE INDEX IF NOT EXISTS chunks_tenant ON chunks (tenant);
            CREATE INDEX IF NOT EXISTS chunks_embedding_hnsw ON chunks USING hnsw (embedding vector_cosine_ops);
            CREATE TABLE IF NOT EXISTS embedders (
              tenant text PRIMARY KEY,
              name text NOT NULL,
              model bytea NOT NULL,
              updated_at timestamptz NOT NULL DEFAULT now()
            );
            CREATE TABLE IF NOT EXISTS eval_runs (
              id uuid PRIMARY KEY,
              created_at timestamptz NOT NULL DEFAULT now(),
              dataset text NOT NULL,
              config jsonb NOT NULL,
              summary jsonb NOT NULL,
              per_query jsonb NOT NULL
            );
            CREATE TABLE IF NOT EXISTS query_log (
              id bigserial PRIMARY KEY,
              tenant text NOT NULL,
              created_at timestamptz NOT NULL DEFAULT now(),
              mode text NOT NULL,
              provider text,
              latency_ms double precision NOT NULL,
              tokens_in int NOT NULL DEFAULT 0,
              tokens_out int NOT NULL DEFAULT 0,
              cost_usd double precision NOT NULL DEFAULT 0,
              abstained boolean,
              groundedness double precision
            );
        """)
        conn.execute("INSERT INTO schema_meta VALUES ('dim', %s) ON CONFLICT (key) DO NOTHING", (str(dim),))
        conn.execute("INSERT INTO schema_meta VALUES ('version', %s) ON CONFLICT (key) DO NOTHING", (str(SCHEMA_VERSION),))


def connect(url: str) -> psycopg.Connection:
    conn = psycopg.connect(url, autocommit=True)
    conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
    register_vector(conn)
    return conn


@dataclass
class StoredDocument:
    id: str
    tenant: str
    name: str
    media_type: str
    sha256: str
    page_count: int
    created: bool  # False when the same bytes were already ingested


class Store:
    def __init__(self, conn: psycopg.Connection) -> None:
        self.conn = conn

    def insert_document(self, tenant: str, name: str, media_type: str, sha256: str, page_count: int,
                        chunking: dict, chunks: list[tuple], vectors: np.ndarray | None, meta: dict | None = None) -> StoredDocument:
        """`chunks` = [(ordinal, text, page_start, page_end, section)]. Atomic."""
        with self.conn.transaction():
            row = self.conn.execute("SELECT id, name, media_type, page_count FROM documents WHERE tenant = %s AND sha256 = %s",
                                    (tenant, sha256)).fetchone()
            if row:
                return StoredDocument(str(row[0]), tenant, row[1], row[2], sha256, row[3], False)
            doc_id = str(uuid.uuid4())
            self.conn.execute(
                "INSERT INTO documents (id, tenant, name, media_type, sha256, page_count, chunking, meta) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                (doc_id, tenant, name, media_type, sha256, page_count, json.dumps(chunking), json.dumps(meta or {})))
            with self.conn.cursor() as cur:
                cur.executemany(
                    "INSERT INTO chunks (id, doc_id, tenant, ordinal, text, page_start, page_end, section, embedding) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    [(f"{doc_id}:{o}", doc_id, tenant, o, t, ps, pe, sec, vectors[i] if vectors is not None else None)
                     for i, (o, t, ps, pe, sec) in enumerate(chunks)])
            return StoredDocument(doc_id, tenant, name, media_type, sha256, page_count, True)

    def delete_document(self, tenant: str, doc_id: str) -> bool:
        try:
            uuid.UUID(doc_id)
        except ValueError:
            return False
        with self.conn.transaction():
            r = self.conn.execute("DELETE FROM documents WHERE id = %s AND tenant = %s", (doc_id, tenant))
            return r.rowcount == 1

    def list_documents(self, tenant: str) -> list[dict]:
        rows = self.conn.execute(
            "SELECT d.id, d.name, d.media_type, d.page_count, d.created_at, count(c.id) FROM documents d LEFT JOIN chunks c ON c.doc_id = d.id "
            "WHERE d.tenant = %s GROUP BY d.id ORDER BY d.created_at", (tenant,)).fetchall()
        return [{"id": str(r[0]), "name": r[1], "media_type": r[2], "pages": r[3], "created_at": r[4].isoformat(), "chunks": r[5]} for r in rows]

    def load_chunks(self, tenant: str | None = None) -> tuple[list[ChunkRecord], np.ndarray | None]:
        q = ("SELECT c.id, c.doc_id, d.name, c.ordinal, c.text, c.page_start, c.page_end, c.section, c.tenant, c.embedding "
             "FROM chunks c JOIN documents d ON d.id = c.doc_id")
        rows = self.conn.execute(q + (" WHERE c.tenant = %s" if tenant else "") + " ORDER BY c.id", (tenant,) if tenant else ()).fetchall()
        recs = [ChunkRecord(r[0], str(r[1]), r[2], r[3], r[4], r[5], r[6], r[7], r[8]) for r in rows]
        vecs = [r[9] for r in rows]
        if not rows or any(v is None for v in vecs):
            return recs, None
        return recs, np.stack([np.asarray(v.to_numpy() if hasattr(v, "to_numpy") else v, dtype=np.float32) for v in vecs])

    def update_embeddings(self, ids: list[str], vectors: np.ndarray) -> None:
        with self.conn.transaction(), self.conn.cursor() as cur:
            cur.executemany("UPDATE chunks SET embedding = %s WHERE id = %s", [(vectors[i], cid) for i, cid in enumerate(ids)])

    def ann_search(self, tenant: str, qvec: np.ndarray, k: int, ef_search: int = 100) -> list[tuple[str, float]]:
        """pgvector HNSW search. pgvector 0.6 applies the tenant filter AFTER
        the index scan, so a selective filter can return fewer than k rows;
        ef_search is raised to at least 4k to reduce that (see docs)."""
        with self.conn.transaction():
            self.conn.execute(f"SET LOCAL hnsw.ef_search = {int(max(ef_search, 4 * k))}")
            rows = self.conn.execute(
                "SELECT id, 1 - (embedding <=> %s) FROM chunks WHERE tenant = %s ORDER BY embedding <=> %s LIMIT %s",
                (qvec, tenant, qvec, k)).fetchall()
        return [(r[0], float(r[1])) for r in rows]

    def save_embedder(self, tenant: str, name: str, blob: bytes) -> None:
        self.conn.execute("INSERT INTO embedders (tenant, name, model) VALUES (%s,%s,%s) ON CONFLICT (tenant) DO UPDATE "
                          "SET name = EXCLUDED.name, model = EXCLUDED.model, updated_at = now()", (tenant, name, blob))

    def load_embedder(self, tenant: str) -> tuple[str, bytes] | None:
        r = self.conn.execute("SELECT name, model FROM embedders WHERE tenant = %s", (tenant,)).fetchone()
        return (r[0], bytes(r[1])) if r else None

    def log_query(self, tenant: str, mode: str, provider: str | None, latency_ms: float, usage: dict,
                  abstained: bool | None, groundedness: float | None) -> None:
        self.conn.execute(
            "INSERT INTO query_log (tenant, mode, provider, latency_ms, tokens_in, tokens_out, cost_usd, abstained, groundedness) "
            "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (tenant, mode, provider, latency_ms, int(usage.get("tokens_in", 0)), int(usage.get("tokens_out", 0)),
             float(usage.get("cost_usd", 0.0)), abstained, groundedness))

    def usage_summary(self, tenant: str) -> dict:
        r = self.conn.execute(
            "SELECT count(*), coalesce(avg(latency_ms),0), coalesce(percentile_cont(0.95) WITHIN GROUP (ORDER BY latency_ms),0), "
            "coalesce(sum(tokens_in),0), coalesce(sum(tokens_out),0), coalesce(sum(cost_usd),0), avg(groundedness), "
            "avg(CASE WHEN abstained THEN 1.0 WHEN abstained IS NOT NULL THEN 0.0 END) "
            "FROM query_log WHERE tenant = %s", (tenant,)).fetchone()
        return {"queries": r[0], "latency_ms_avg": float(r[1]), "latency_ms_p95": float(r[2]), "tokens_in": int(r[3]),
                "tokens_out": int(r[4]), "cost_usd": float(r[5]),
                "groundedness_avg_answered": None if r[6] is None else float(r[6]),
                "abstention_rate": None if r[7] is None else float(r[7])}

    def save_eval_run(self, dataset: str, config: dict, summary: dict, per_query: list[dict]) -> str:
        rid = str(uuid.uuid4())
        self.conn.execute("INSERT INTO eval_runs (id, dataset, config, summary, per_query) VALUES (%s,%s,%s,%s,%s)",
                          (rid, dataset, json.dumps(config), json.dumps(summary), json.dumps(per_query)))
        return rid


def serialize_lsa(emb) -> bytes:
    buf = io.BytesIO()
    np.savez_compressed(buf, idf=emb.idf, components=emb.components,
                        vocab=np.frombuffer(json.dumps(emb.vocab).encode(), dtype=np.uint8))
    return buf.getvalue()


def deserialize_lsa(blob: bytes):
    from .embed import LSAEmbedder

    z = np.load(io.BytesIO(blob))
    e = LSAEmbedder(dim=z["components"].shape[1])
    e.vocab = json.loads(z["vocab"].tobytes().decode())
    e.idf, e.components = z["idf"], z["components"]
    e.name = f"lsa-{e.dim}"
    return e
