#!/usr/bin/env bash
# Deploy a release: an immutable artifact plus the config for one environment.
set -euo pipefail
version="$(cat VERSION)"
environment="${ENVIRONMENT:-staging}"
printf 'release  %s-%s\n' "$version" "$environment"
printf 'config   from the environment, not from the artifact\n'
printf 'deployed %s\n' "$environment"
