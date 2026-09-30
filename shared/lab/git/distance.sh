#!/usr/bin/env bash
# What a long-lived branch costs, measured rather than asserted.
#
# Two branches make the same kind of change to the same file. One comes back
# immediately; the other comes back after trunk has moved nine times.
# Usage: distance.sh
set -euo pipefail

work="$(mktemp -d)"
cd "$work"
git init -q -b main
git config user.name "Fixture Engineer"
git config user.email "engineer@example.com"
seq 1 10 >config.txt
git add . && git commit -qm "start"

for name in short long; do
  git checkout -q -b "$name" main
  sed -i.bak "3s/.*/changed on $name/" config.txt && rm config.txt.bak
  git commit -qam "work on $name"
  git checkout -q main
done

merge_report() {                 # merge_report <branch>
  local branch="$1" behind conflicts status
  behind="$(git rev-list --count "$branch"..main)"
  if git merge --no-commit --no-ff -q "$branch" >/dev/null 2>&1; then
    status=clean
  else
    status=conflict
  fi
  conflicts="$(git diff --name-only --diff-filter=U | wc -l | tr -d ' ')"
  git merge --abort 2>/dev/null || git reset -q --hard HEAD
  printf '%-8s %2s commits behind trunk   merge %-9s conflicted files %s\n' \
    "$branch" "$behind" "$status" "$conflicts"
}

merge_report short
for n in $(seq 1 9); do
  sed -i.bak "3s/.*/trunk edit $n/" config.txt && rm config.txt.bak
  git commit -qam "trunk moves on $n"
done
merge_report long
rm -rf "$work"
