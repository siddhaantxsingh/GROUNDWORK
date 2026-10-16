import os
import uuid

import psycopg
import pytest

ADMIN_URL = os.environ.get("GW_TEST_ADMIN_URL", "postgresql://postgres@127.0.0.1:5432/postgres")
REDIS_URL = os.environ.get("GW_TEST_REDIS_URL", "redis://127.0.0.1:6379/15")


@pytest.fixture
def db_url():
    """A fresh PostgreSQL database per test (dropped afterwards)."""
    name = "gw_test_" + uuid.uuid4().hex[:10]
    with psycopg.connect(ADMIN_URL, autocommit=True) as c:
        c.execute(f"CREATE DATABASE {name}")
    url = ADMIN_URL.rsplit("/", 1)[0] + "/" + name
    yield url
    with psycopg.connect(ADMIN_URL, autocommit=True) as c:
        c.execute(f"DROP DATABASE IF EXISTS {name} WITH (FORCE)")


@pytest.fixture
def redis_client():
    import redis

    r = redis.Redis.from_url(REDIS_URL)
    try:
        r.ping()
    except Exception:
        pytest.skip("redis not available")
    r.flushdb()
    yield r
    r.flushdb()


def pytest_collection_modifyitems(config, items):
    """`localmodel` tests load real GGUF models; they are opt-in so CI stays light."""
    if os.environ.get("GW_RUN_LOCAL_MODELS") == "1":
        return
    skip = pytest.mark.skip(reason="local model test: set GW_RUN_LOCAL_MODELS=1 (needs groundwork[local] + scripts/fetch_models.py)")
    for item in items:
        if "localmodel" in item.keywords:
            item.add_marker(skip)
