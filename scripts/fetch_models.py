#!/usr/bin/env python3
"""Fetch GGUF models from Docker Hub's `ai/` namespace (OCI artifacts).

huggingface.co is not reachable from the build environment, but Docker Hub
publishes the same open-weight models as OCI artifacts whose layer media type
is `application/vnd.docker.ai.gguf.v3`. This script uses only the public
registry API (anonymous pull token), verifies the layer sha256, and writes
`<cache>/<name>.gguf` plus `<name>.json` with provenance (repo, tag, digest,
license text found in the artifact).

Usage:
    python scripts/fetch_models.py                       # default set
    python scripts/fetch_models.py ai/smollm2:latest     # one model
    GROUNDWORK_MODEL_DIR=/path python scripts/fetch_models.py

Models are never committed to git.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import tempfile
import urllib.request

DEFAULT_MODELS = [
    "ai/nomic-embed-text-v1.5:latest",
    "ai/qwen2.5:0.5B-F16",
    "ai/smollm2:latest",
]
GGUF = "application/vnd.docker.ai.gguf.v3"
LICENSE = "application/vnd.docker.ai.license"
ACCEPT = ", ".join([
    "application/vnd.oci.image.manifest.v1+json",
    "application/vnd.oci.image.index.v1+json",
    "application/vnd.docker.distribution.manifest.v2+json",
])


def _get(url: str, headers: dict[str, str]) -> urllib.request.addinfourl:
    req = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(req, timeout=120)


def license_id(text: str) -> str:
    """SPDX id from the license layer's front matter, else its first line."""
    m = re.search(r"^spdx-id:\s*(\S+)", text, re.M)
    return m.group(1) if m else (text.strip().splitlines() or [""])[0][:80]


def local_name(ref: str) -> str:
    repo, _, tag = ref.partition(":")
    return f"{repo.split('/')[-1]}-{tag or 'latest'}".replace("/", "_")


def fetch(ref: str, cache: str) -> dict:
    repo, _, tag = ref.partition(":")
    tag = tag or "latest"
    name = local_name(ref)
    out = os.path.join(cache, name + ".gguf")
    meta_path = os.path.join(cache, name + ".json")
    if os.path.exists(out) and os.path.exists(meta_path):
        meta = json.load(open(meta_path))
        print(f"{ref}: cached at {out} sha256={meta['sha256']}")
        return meta
    tok = json.load(_get(
        f"https://auth.docker.io/token?service=registry.docker.io&scope=repository:{repo}:pull", {}))["token"]
    auth = {"Authorization": f"Bearer {tok}"}
    man = json.load(_get(f"https://registry-1.docker.io/v2/{repo}/manifests/{tag}", {**auth, "Accept": ACCEPT}))
    if "manifests" in man:  # an index: take the first manifest
        digest = man["manifests"][0]["digest"]
        man = json.load(_get(f"https://registry-1.docker.io/v2/{repo}/manifests/{digest}", {**auth, "Accept": ACCEPT}))
    layers = man.get("layers", [])
    gguf = [l for l in layers if l.get("mediaType") == GGUF]
    if len(gguf) != 1:
        raise SystemExit(f"{ref}: expected one GGUF layer, got {[l.get('mediaType') for l in layers]}")
    layer = gguf[0]
    licenses = []
    for l in layers:
        if l.get("mediaType") == LICENSE:
            licenses.append(_get(f"https://registry-1.docker.io/v2/{repo}/blobs/{l['digest']}", auth).read().decode("utf-8", "replace"))
    want = layer["digest"].split(":", 1)[1]
    fd, tmp = tempfile.mkstemp(dir=cache, prefix=name + ".", suffix=".part")
    h = hashlib.sha256()
    with os.fdopen(fd, "wb") as f, _get(f"https://registry-1.docker.io/v2/{repo}/blobs/{layer['digest']}", auth) as r:
        while chunk := r.read(1 << 20):
            h.update(chunk)
            f.write(chunk)
    if h.hexdigest() != want:
        os.unlink(tmp)
        raise SystemExit(f"{ref}: sha256 mismatch {h.hexdigest()} != {want}")
    os.chmod(tmp, 0o644)
    os.replace(tmp, out)  # atomic: concurrent fetchers never see a partial file
    meta = {
        "ref": ref, "file": out, "size_bytes": layer["size"], "sha256": want,
        "licenses": [license_id(t) for t in licenses],
    }
    if licenses:
        with open(os.path.join(cache, name + ".LICENSE.txt"), "w") as f:
            f.write("\n\n-----\n\n".join(licenses))
    with open(meta_path, "w") as f:
        json.dump(meta, f, indent=2)
    print(f"{ref}: wrote {out} ({layer['size']} bytes) sha256={want}")
    return meta


def main(argv: list[str]) -> None:
    cache = os.environ.get("GROUNDWORK_MODEL_DIR", "/home/user/models")
    os.makedirs(cache, exist_ok=True)
    for ref in argv or DEFAULT_MODELS:
        fetch(ref, cache)


if __name__ == "__main__":
    main(sys.argv[1:])
