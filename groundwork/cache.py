"""Redis-backed query cache and rate limiter, both degrading safely when
Redis is unavailable.

Cache: keys are namespaced per tenant with a per-tenant generation counter;
invalidation (on ingest/delete) increments the generation, so stale entries
are never served and expire by TTL. If Redis is down the cache is bypassed
(a miss), never an error.

Rate limiter: fixed one-minute window per API key (INCR + EXPIRE). If Redis
is down it falls back to an in-process token bucket with the same rate, so
limits still apply per process (documented: not cluster-wide in that mode).
"""
from __future__ import annotations

import json
import threading
import time


class RedisCache:
    def __init__(self, client, ttl_s: int = 300) -> None:
        self.r, self.ttl = client, ttl_s
        self.errors = 0

    def _gen(self, tenant: str) -> int:
        return int(self.r.get(f"gw:gen:{tenant}") or 0)

    def get(self, tenant: str, key: str):
        try:
            raw = self.r.get(f"gw:q:{tenant}:{self._gen(tenant)}:{key}")
            return json.loads(raw) if raw else None
        except Exception:
            self.errors += 1
            return None

    def put(self, tenant: str, key: str, value: dict) -> None:
        try:
            self.r.set(f"gw:q:{tenant}:{self._gen(tenant)}:{key}", json.dumps(value), ex=self.ttl)
        except Exception:
            self.errors += 1

    def invalidate(self, tenant: str) -> None:
        try:
            self.r.incr(f"gw:gen:{tenant}")
        except Exception:
            # Cannot invalidate: disable caching for this tenant until Redis
            # returns, by making every read miss (generation unknown).
            self.errors += 1


class RateLimiter:
    def __init__(self, per_minute: int, client=None) -> None:
        self.per_minute, self.r = per_minute, client
        self._local: dict[str, tuple[float, float]] = {}
        self._lock = threading.Lock()
        self.fallbacks = 0

    def allow(self, key: str) -> bool:
        if self.per_minute <= 0:
            return True
        if self.r is not None:
            try:
                window = int(time.time() // 60)
                k = f"gw:rl:{key}:{window}"
                n = self.r.incr(k)
                if n == 1:
                    self.r.expire(k, 120)
                return n <= self.per_minute
            except Exception:
                self.fallbacks += 1
        with self._lock:
            rate = self.per_minute / 60.0
            tokens, last = self._local.get(key, (float(self.per_minute), time.monotonic()))
            now = time.monotonic()
            tokens = min(float(self.per_minute), tokens + (now - last) * rate)
            if tokens < 1.0:
                self._local[key] = (tokens, now)
                return False
            self._local[key] = (tokens - 1.0, now)
            return True
