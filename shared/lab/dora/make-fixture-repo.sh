#!/usr/bin/env bash
# Build a small repository with a real, fixed history to measure.
#
# Usage: make-fixture-repo.sh <directory>
# Every date is pinned, so the metrics computed from it are the same on any
# machine, in any timezone, on any day.
set -euo pipefail

target="${1:?usage: make-fixture-repo.sh <directory>}"
rm -rf "$target"
mkdir -p "$target"
cd "$target"
git init -q -b main
git config user.name "Fixture Engineer"
git config user.email "engineer@example.com"

commit() {                 # commit <iso date> <subject> [trailer]
  local when="$1" subject="$2" trailer="${3:-}"
  echo "$subject" >>CHANGELOG
  git add CHANGELOG
  GIT_AUTHOR_DATE="$when" GIT_COMMITTER_DATE="$when" \
    git commit -q -m "$subject" ${trailer:+-m "$trailer"}
}

deploy() {                 # deploy <iso date> <tag>
  GIT_COMMITTER_DATE="$1" git tag -a "$2" -m "deployed to production"
}

commit 2026-02-01T09:00:00+00:00 "add the quote endpoint"
commit 2026-02-01T15:00:00+00:00 "add pagination"
deploy 2026-02-02T10:00:00+00:00 deploy-0001
commit 2026-02-03T10:00:00+00:00 "cache the quote of the day"
deploy 2026-02-04T11:00:00+00:00 deploy-0002
commit 2026-02-04T16:00:00+00:00 "tidy the request logger"
commit 2026-02-05T08:00:00+00:00 "add a health endpoint"
deploy 2026-02-05T09:30:00+00:00 deploy-0003
commit 2026-02-06T09:00:00+00:00 "switch to the new search index"
deploy 2026-02-06T14:00:00+00:00 deploy-0004
commit 2026-02-06T14:40:00+00:00 "restore the old search index" \
  "Remediates: deploy-0004"
deploy 2026-02-06T15:12:00+00:00 deploy-0005
commit 2026-02-08T12:00:00+00:00 "widen the rate limit"
commit 2026-02-09T08:00:00+00:00 "retry failed writes"
deploy 2026-02-09T10:00:00+00:00 deploy-0006
commit 2026-02-10T13:00:00+00:00 "roll the database credential"
deploy 2026-02-10T16:00:00+00:00 deploy-0007
commit 2026-02-11T08:50:00+00:00 "put the old credential back" \
  "Remediates: deploy-0007"
deploy 2026-02-11T09:20:00+00:00 deploy-0008
commit 2026-02-12T09:00:00+00:00 "log the release identifier"
deploy 2026-02-12T11:00:00+00:00 deploy-0009
commit 2026-02-13T09:00:00+00:00 "drop the unused column"
commit 2026-02-13T14:00:00+00:00 "document the runbook"
deploy 2026-02-13T15:30:00+00:00 deploy-0010

echo "fixture repository ready at $target"
