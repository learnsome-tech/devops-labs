#!/usr/bin/env bash
# The same pipeline the workflow file runs, as a script you can run locally.
# A stage that fails stops the pipeline: that is the whole point of a gate.
set -euo pipefail

stage() { printf '%-10s %s\n' "$1" "$2"; }

stage stage:lint "checking formatting and obvious mistakes"
python3 -m py_compile app/calc.py

stage stage:test "running the test suite"
python3 run_tests.py

stage stage:build "producing one immutable artifact"
bash build.sh

stage stage:gate "artifact is built once and promoted, never rebuilt"
echo "pipeline passed"
