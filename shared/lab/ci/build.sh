#!/usr/bin/env bash
# Build once, then promote the same bytes through every environment.
# The digest is taken from the file contents, so the same source always
# produces the same artifact identity, on any machine, on any day.
set -euo pipefail
version="$(cat VERSION)"
mkdir -p dist
out="dist/calc-${version}.tar"
find app -name '*.py' | sort | tar -cf "$out" -T -
digest="$(find app -name '*.py' | sort | xargs cat | cksum | cut -d' ' -f1)"
printf 'artifact %s\n' "$out"
printf 'digest   %s\n' "$digest"
