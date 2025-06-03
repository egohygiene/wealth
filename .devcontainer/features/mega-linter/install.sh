#!/usr/bin/env bash
set -euo pipefail

if ! command -v mega-linter-runner >/dev/null 2>&1; then
    npm install -g mega-linter-runner
fi
