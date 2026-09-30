#!/usr/bin/env bash
# Measure the same work twice: once honestly, once gamed.
#
# The gamed repository calls every commit a deployment. No code changed, no
# process changed, and the delivery numbers move anyway.
# Usage: gaming.sh <repository>
set -euo pipefail
repo="${1:?usage: gaming.sh <repository>}"
scratch="$(mktemp -d)"
copy="$scratch/gamed"
cp -R "$repo" "$copy"

git -C "$copy" tag -l 'deploy-*' | xargs -n1 git -C "$copy" tag -d >/dev/null
count=0
for sha in $(git -C "$copy" rev-list --reverse HEAD); do
  count=$((count + 1))
  stamp="$(git -C "$copy" show -s --format=%aI "$sha")"
  GIT_COMMITTER_DATE="$stamp" \
    git -C "$copy" tag -a "deploy-9$(printf '%03d' "$count")" "$sha" \
      -m "deployed"
done

echo "honest, deployments tagged when they reached production"
python3 dora_metrics.py "$repo" | sed 's/^/  /'
echo "gamed, every commit relabelled a deployment"
python3 dora_metrics.py "$copy" | sed 's/^/  /'
rm -rf "$scratch"
