#!/usr/bin/env bash
# Where a version number comes from when the repository is the source of truth.
# Usage: version.sh <repository>
set -euo pipefail
repo="${1:?usage: version.sh <repository>}"

tag="$(git -C "$repo" describe --tags --abbrev=0)"
since="$(git -C "$repo" rev-list --count "${tag}..HEAD")"
branch="$(git -C "$repo" rev-parse --abbrev-ref HEAD)"

printf 'last deployment tag   %s\n' "$tag"
printf 'commits since         %s\n' "$since"
printf 'branch                %s\n' "$branch"
printf 'candidate build       %s-%s\n' "$tag" "$((since + 1))"
