#!/usr/bin/env bash
# Build the image; forwards a proxy CA (if present) as a build secret and the host network.
#   scripts/docker_build.sh [TAG] [LOCAL_MODELS=0|1]
set -euo pipefail
cd "$(dirname "$0")/.."
TAG=${1:-groundwork:latest}; LOCAL=${2:-0}
CA=${PROXY_CA:-/root/.ccr/ca-bundle.crt}
args=(--network host --build-arg LOCAL_MODELS="$LOCAL" -t "$TAG")
[ -s "$CA" ] && args+=(--secret id=ca,src="$CA")
DOCKER_BUILDKIT=1 exec docker build "${args[@]}" .
