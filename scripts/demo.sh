#!/usr/bin/env bash
# End-to-end demo against a real server: creates a throwaway database,
# starts the API, uploads examples/, asks questions, deletes, cleans up.
# Needs: PostgreSQL with pgvector (GW_ADMIN_URL), Redis optional, curl.
set -euo pipefail
cd "$(dirname "$0")/.."
ADMIN=${GW_ADMIN_URL:-postgresql://postgres@127.0.0.1:5432/postgres}
DB=gw_demo_$$
psql "$ADMIN" -qc "CREATE DATABASE $DB"
cleanup() { kill "${PID:-0}" 2>/dev/null || true; psql "$ADMIN" -qc "DROP DATABASE IF EXISTS $DB WITH (FORCE)"; }
trap cleanup EXIT
KEY=$(python3 -c "import secrets;print(secrets.token_hex(16))")
export GW_DATABASE_URL="${ADMIN%/*}/$DB" GW_API_KEYS="demo:$KEY" GW_DIM=64
python3 -m groundwork serve --port 8765 >/tmp/gw-demo-server.log 2>&1 & PID=$!
for i in $(seq 50); do curl -sf localhost:8765/healthz >/dev/null && break; sleep 0.2; done
H="Authorization: Bearer $KEY"
echo "== upload"; curl -s -H "$H" -F file=@examples/turbine-manual.md localhost:8765/v1/documents; echo
python3 - <<'PY'
from fpdf import FPDF
p = FPDF(); p.set_font("helvetica", size=11)
for t in ["Hydraulic pitch system overview.", "The pitch accumulator pressure must be checked every 6 months.", "Torque table."]:
    p.add_page(); p.multi_cell(0, 6, t)
open("/tmp/gw-demo-pitch.pdf", "wb").write(bytes(p.output()))
PY
curl -s -H "$H" -F file=@/tmp/gw-demo-pitch.pdf localhost:8765/v1/documents; echo
for q in "How often must the gearbox be lubricated?" "When is the pitch accumulator pressure checked?" "Who won the 1998 World Cup?"; do
  echo "== query: $q"
  curl -s -H "$H" -H 'content-type: application/json' -d "{\"query\":\"$q\"}" localhost:8765/v1/query \
    | python3 -c "import json,sys;d=json.load(sys.stdin);print(' answer:',d['answer']);print(' sources:',[(s['document'],s['pages'],s['section']) for s in d['sources']][:2]);print(' grounding:',{k:d['grounding'][k] for k in ('groundedness','citation_precision')});print(' timings_ms:',{k:round(v,2) for k,v in d['timings_ms'].items()})"
done
echo "== usage"; curl -s -H "$H" localhost:8765/v1/usage; echo
