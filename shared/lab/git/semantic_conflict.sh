#!/usr/bin/env bash
# Two branches, no merge conflict, broken build.
#
# This is the failure that continuous integration exists to catch: git can
# merge text that no longer makes sense together. Usage: semantic_conflict.sh
set -euo pipefail

work="$(mktemp -d)"
cd "$work"
git init -q -b main
git config user.name "Fixture Engineer"
git config user.email "engineer@example.com"
mkdir app
printf 'def apply_discount(pennies, percent):\n    return pennies - pennies * percent // 100\n' >app/calc.py
printf 'from app.calc import apply_discount\n\nprint(apply_discount(1000, 10))\n' >app/report.py
git add . && git commit -qm "start"

git checkout -q -b rename main
printf 'def discount(pennies, percent):\n    return pennies - pennies * percent // 100\n' >app/calc.py
git commit -qam "rename the pricing function"

git checkout -q -b caller main
printf 'from app.calc import apply_discount\n\nprint(apply_discount(2500, 20))\n' >app/report.py
git commit -qam "use the pricing function in a second place"

git checkout -q main
for branch in rename caller; do
  if git merge --no-edit -q "$branch" >/dev/null 2>&1; then
    printf 'merge %-8s clean, no conflict\n' "$branch"
  else
    printf 'merge %-8s conflict\n' "$branch"
  fi
done

if python3 app/report.py >/dev/null 2>&1; then
  printf 'build    green\n'
else
  printf 'build    red: cannot import apply_discount from app.calc\n'
fi
printf 'verdict  git merged the text; only the build noticed the meaning\n'
rm -rf "$work"
