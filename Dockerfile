# Groundwork API image.
#   docker build -t groundwork .                              # default: no local models (small image)
#   docker build --build-arg LOCAL_MODELS=1 -t groundwork:local .   # + llama-cpp-python (CPU), models mounted at runtime
# Built and smoke-tested on 2026-10-14 (docs/evidence/2026-10-14/).
# syntax=docker/dockerfile:1
# Behind a TLS-intercepting proxy, pass its CA as an optional build secret:
#   docker build --secret id=ca,src=/path/to/ca.crt ...   (scripts/docker_build.sh does this; nothing is stored in the image)
FROM python:3.12-slim AS build
ARG LOCAL_MODELS=0
RUN if [ "$LOCAL_MODELS" = "1" ]; then apt-get update && apt-get install -y --no-install-recommends build-essential cmake \
    && rm -rf /var/lib/apt/lists/*; fi
WORKDIR /src
COPY pyproject.toml ./
COPY groundwork ./groundwork
# Portable x86-64 build (AVX2/FMA, no -march=native) so the image runs on other hosts.
ENV CMAKE_ARGS="-DGGML_NATIVE=OFF -DGGML_AVX=ON -DGGML_AVX2=ON -DGGML_FMA=ON -DGGML_F16C=ON" CMAKE_BUILD_PARALLEL_LEVEL=4
RUN --mount=type=secret,id=ca,required=false \
    if [ -s /run/secrets/ca ]; then export PIP_CERT=/run/secrets/ca; fi \
    && if [ "$LOCAL_MODELS" = "1" ]; then EXTRA="[local]"; else EXTRA=""; fi \
    && pip wheel --no-cache-dir --wheel-dir /wheels ".${EXTRA}"

FROM python:3.12-slim
ARG LOCAL_MODELS=0
RUN if [ "$LOCAL_MODELS" = "1" ]; then apt-get update && apt-get install -y --no-install-recommends libgomp1 \
    && rm -rf /var/lib/apt/lists/*; fi \
    && useradd --create-home --uid 10001 app
COPY --from=build /wheels /wheels
RUN pip install --no-cache-dir --no-index /wheels/*.whl && rm -rf /wheels
WORKDIR /app
USER app
ENV GW_MODEL_DIR=/models
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s CMD python -c "import urllib.request,sys;sys.exit(0 if urllib.request.urlopen('http://127.0.0.1:8080/healthz').status==200 else 1)"
CMD ["python", "-m", "groundwork", "serve", "--host", "0.0.0.0", "--port", "8080"]
