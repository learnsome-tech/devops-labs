#!/usr/bin/env bash
# When did these deployments actually reach production?
# Usage: deploy_times.sh <repository> <tag> [tag ...]
set -euo pipefail
repo="${1:?usage: deploy_times.sh <repository> <tag> [tag ...]}"
shift
for tag in "$@"; do
  printf '%-12s %s\n' "$tag" \
    "$(git -C "$repo" for-each-ref --format='%(taggerdate:iso)' \
       "refs/tags/$tag")"
done
