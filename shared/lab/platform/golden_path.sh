#!/usr/bin/env bash
# A golden path: one command, a service that already meets the standards.
# Usage: golden_path.sh <service name>
set -euo pipefail
name="${1:?usage: golden_path.sh <service name>}"
root="$(mktemp -d)/$name"

mkdir -p "$root"/{app,tests,.github/workflows}
printf 'def handle(path):\n    return 200, "ok"\n' >"$root/app/main.py"
{ printf 'name: pipeline\non: [push]\njobs:\n'
  printf '  test:\n    runs-on: ubuntu-24.04\n'
} >"$root/.github/workflows/pipeline.yml"
printf 'slo: 99.9 availability over 30 days\nowner: quotes team\n' \
  >"$root/service.yaml"
printf '# %s\n\nCreated from the golden path template.\n' "$name" \
  >"$root/README.md"

printf 'created %s\n' "$name"
( cd "$root/.." && find "$name" -type f | sort | sed 's/^/  /' )
printf 'defaults applied: pipeline, ownership, service level objective\n'
rm -rf "$(dirname "$root")"
