#!/usr/bin/env bash
# Smoke test of a built image against PostgreSQL+pgvector and Redis on the host
# (host network, so no extra images are pulled):
#   scripts/docker_smoke.sh [IMAGE] [extra docker run args...]
set -euo pipefail
IMG=${1:-groundwork:test}; shift || true
PORT=${GW_SMOKE_PORT:-18737}; DB=gw_smoke_$$; KEY=smoke-key-0123456789abcdef
psql -h 127.0.0.1 -U postgres -qc "CREATE DATABASE $DB"
cleanup() { docker rm -f "$DB" >/dev/null 2>&1 || true; psql -h 127.0.0.1 -U postgres -qc "DROP DATABASE IF EXISTS $DB WITH (FORCE)"; }
trap cleanup EXIT
docker run -d --name "$DB" --network host --read-only "$@" \
  -e GW_DATABASE_URL="postgresql://postgres@127.0.0.1:5432/$DB" -e GW_REDIS_URL=redis://127.0.0.1:6379/14 \
  -e GW_API_KEYS="smoke:$KEY" "$IMG" python -m groundwork serve --host 127.0.0.1 --port "$PORT" >/dev/null
for i in $(seq 1 120); do curl -fsS "http://127.0.0.1:$PORT/healthz" >/dev/null 2>&1 && break; sleep 2; done
curl -fsS "http://127.0.0.1:$PORT/healthz"; echo
printf '# Turbine Manual\n\n## Gearbox\n\nThe gearbox must be lubricated every 500 operating hours. Use ISO VG 320 gear oil.\n\n## Blades\n\nInspect the blades once a year.\n' > /tmp/gw_smoke_manual.md
curl -fsS -H "Authorization: Bearer $KEY" -F file=@/tmp/gw_smoke_manual.md "http://127.0.0.1:$PORT/v1/documents"; echo
OUT=$(curl -fsS --max-time 900 -H "Authorization: Bearer $KEY" -H 'content-type: application/json' \
  -d '{"query":"How often must the gearbox be lubricated?"}' "http://127.0.0.1:$PORT/v1/query")
echo "$OUT" | python3 -c 'import json,sys; d=json.load(sys.stdin); print(json.dumps({k: d[k] for k in ("answer","provider","abstained","citations","grounding")}, indent=1)); assert not d["abstained"] and d["citations"] and "500" in d["answer"]'
echo "SMOKE OK ($IMG)"
