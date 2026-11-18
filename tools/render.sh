#!/usr/bin/env bash
# Usage: tools/render.sh <url> <out.html> [--click "selector"]...
# Build once: docker build -t nptel-copywrite-render:1.55 -f tools/Dockerfile.render tools
# out.html must be under the repo or $CLAUDE_JOB_DIR/tmp (both are mounted).
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
out="$(realpath -m "$2")"; mkdir -p "$(dirname "$out")"
url="$1"; shift 2
exec docker run --rm --init --cpus=1 --memory=1500m \
  -v "$here:/tools:ro" -v "$(dirname "$out"):/out" \
  -e PYTHONUNBUFFERED=1 nptel-copywrite-render:1.55 \
  python /tools/render.py "$url" "/out/$(basename "$out")" "$@"
