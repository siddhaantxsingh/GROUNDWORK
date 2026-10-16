"""HTTP API (FastAPI).

Auth: `Authorization: Bearer <api key>`; keys map to tenants via
GW_API_KEYS="tenant1:key1,tenant2:key2". Keys are compared in constant time
against SHA-256 digests held in memory. Every data operation is scoped to the
caller's tenant: a document id from another tenant behaves exactly like a
missing one (404), so ids cannot be probed.

Endpoints
  POST   /v1/documents            multipart upload (file), returns document info
  GET    /v1/documents            list the tenant's documents
  DELETE /v1/documents/{id}       delete a document and all its chunks
  POST   /v1/query                retrieval (+ optional grounded answer)
  GET    /v1/usage                latency / token / cost summary for the tenant
  GET    /healthz                 liveness + dependency status
  GET    /metrics                 Prometheus text format
"""
from __future__ import annotations

import hashlib
import hmac
import os
import threading
import time
from collections import Counter

from fastapi import Depends, FastAPI, File, Header, HTTPException, Request, UploadFile
from fastapi.responses import JSONResponse, PlainTextResponse
from pydantic import BaseModel, Field

from .cache import RateLimiter, RedisCache
from .engine import Engine, EngineConfig
from .ingest import MAX_DOCUMENT_BYTES, ParseError
from .retrieve import RetrievalConfig
from .store import Store, connect, migrate


class QueryBody(BaseModel):
    query: str = Field(min_length=1, max_length=2000)
    k: int = Field(default=5, ge=1, le=50)
    generate: bool = True
    mode: str = Field(default="bm25", pattern="^(bm25|dense|hybrid)$")
    rerank: bool = True
    rewrite: str = Field(default="none", pattern="^(none|rm3)$")
    doc_ids: list[str] | None = Field(default=None, max_length=100)


def parse_keys(spec: str) -> dict[bytes, str]:
    out = {}
    for item in filter(None, (s.strip() for s in spec.split(","))):
        tenant, _, key = item.partition(":")
        if not tenant or len(key) < 16:
            raise ValueError("GW_API_KEYS entries must be tenant:key with keys of at least 16 characters")
        out[hashlib.sha256(key.encode()).digest()] = tenant
    return out


class Metrics:
    def __init__(self) -> None:
        self.lock = threading.Lock()
        self.requests: Counter = Counter()
        self.latency_sum: Counter = Counter()

    def observe(self, route: str, status: int, seconds: float) -> None:
        with self.lock:
            self.requests[(route, status)] += 1
            self.latency_sum[route] += seconds

    def render(self, extra: dict[str, float]) -> str:
        lines = ["# TYPE gw_http_requests_total counter"]
        with self.lock:
            for (route, status), n in sorted(self.requests.items()):
                lines.append(f'gw_http_requests_total{{route="{route}",status="{status}"}} {n}')
            lines.append("# TYPE gw_http_request_seconds_sum counter")
            for route, s in sorted(self.latency_sum.items()):
                lines.append(f'gw_http_request_seconds_sum{{route="{route}"}} {s:.6f}')
        for k, v in extra.items():
            lines.append(f"{k} {v}")
        return "\n".join(lines) + "\n"


def create_app(engine: Engine | None = None, api_keys: dict[bytes, str] | None = None,
               limiter: RateLimiter | None = None, redis_client=None, metrics_token_env: str | None = None) -> FastAPI:
    if engine is None:
        conn = connect(os.environ["GW_DATABASE_URL"])
        from .config import apply_to_engine_config, provider_from_env

        cfg = apply_to_engine_config(EngineConfig(dim=int(os.environ.get("GW_DIM", "256"))))
        migrate(conn, cfg.dim)
        if redis_client is None and os.environ.get("GW_REDIS_URL"):
            import redis

            redis_client = redis.Redis.from_url(os.environ["GW_REDIS_URL"], socket_timeout=0.5, socket_connect_timeout=0.5)
        engine = Engine(Store(conn), cfg, provider=provider_from_env(), cache=RedisCache(redis_client) if redis_client else None)
    keys = api_keys if api_keys is not None else parse_keys(os.environ.get("GW_API_KEYS", ""))
    limiter = limiter or RateLimiter(int(os.environ.get("GW_RATE_PER_MIN", "120")), redis_client)
    metrics = Metrics()
    app = FastAPI(title="Groundwork", version="0.1.0")

    @app.middleware("http")
    async def timing(request: Request, call_next):
        t0 = time.perf_counter()
        resp = await call_next(request)
        route = request.scope.get("route")
        metrics.observe(getattr(route, "path", "unmatched"), resp.status_code, time.perf_counter() - t0)
        return resp

    def tenant_of(authorization: str | None = Header(default=None)) -> str:
        if not authorization or not authorization.startswith("Bearer "):
            raise HTTPException(401, "missing bearer token")
        digest = hashlib.sha256(authorization[7:].encode()).digest()
        tenant = None
        for k, t in keys.items():  # constant-time compare against every key
            if hmac.compare_digest(k, digest):
                tenant = t
        if tenant is None:
            raise HTTPException(401, "invalid api key")
        if not limiter.allow(digest.hex()):
            raise HTTPException(429, "rate limit exceeded")
        return tenant

    @app.post("/v1/documents", status_code=201)
    async def upload(file: UploadFile = File(...), tenant: str = Depends(tenant_of)):
        data = await file.read(MAX_DOCUMENT_BYTES + 1)
        if len(data) > MAX_DOCUMENT_BYTES:
            raise HTTPException(413, "document too large")
        try:
            info = engine.ingest(tenant, file.filename or "upload", data)
        except ParseError as e:
            raise HTTPException(422, str(e))
        except ValueError as e:
            raise HTTPException(422, str(e))
        return JSONResponse(info, status_code=201 if info["created"] else 200)

    @app.get("/v1/documents")
    def list_docs(tenant: str = Depends(tenant_of)):
        with engine.lock:
            return {"documents": engine.store.list_documents(tenant)}

    @app.delete("/v1/documents/{doc_id}", status_code=204)
    def delete(doc_id: str, tenant: str = Depends(tenant_of)):
        if not engine.delete(tenant, doc_id):
            raise HTTPException(404, "document not found")

    @app.post("/v1/query")
    def query(body: QueryBody, tenant: str = Depends(tenant_of)):
        cfg = RetrievalConfig(mode=body.mode, rerank=body.rerank, rewrite=body.rewrite)
        try:
            return engine.query(tenant, body.query, body.k, body.generate, cfg, body.doc_ids)
        except ValueError as e:
            raise HTTPException(422, str(e))

    @app.get("/v1/usage")
    def usage(tenant: str = Depends(tenant_of)):
        with engine.lock:
            return engine.store.usage_summary(tenant)

    @app.get("/healthz")
    def health():
        status = {"database": "ok", "redis": "disabled"}
        code = 200
        if not engine.lock.acquire(timeout=2.0):
            status["database"] = "busy"
        else:
            try:
                engine.store.conn.execute("SELECT 1")
            except Exception:
                status["database"], code = "unavailable", 503
            finally:
                engine.lock.release()
        if redis_client is not None:
            try:
                redis_client.ping()
                status["redis"] = "ok"
            except Exception:
                status["redis"] = "unavailable (cache bypassed, local rate limiting)"
        return JSONResponse(status, status_code=code)

    metrics_token = os.environ.get("GW_METRICS_TOKEN", "") if metrics_token_env is None else metrics_token_env

    @app.get("/metrics", response_class=PlainTextResponse)
    def prom(authorization: str | None = Header(default=None)):
        # Aggregates only (no tenant names). Optional bearer token; when unset,
        # the endpoint must be exposed on an internal network only.
        if metrics_token and not hmac.compare_digest((authorization or "").encode(), f"Bearer {metrics_token}".encode()):
            raise HTTPException(401, "metrics token required")
        extra = {"gw_tenants_loaded": len(engine.tenants), "gw_index_chunks_total": sum(len(ti.corpus) for ti in engine.tenants.values())}
        if engine.cache is not None:
            extra["gw_cache_errors_total"] = engine.cache.errors
        extra["gw_ratelimit_fallbacks_total"] = limiter.fallbacks
        return metrics.render(extra)

    app.state.engine = engine
    return app
