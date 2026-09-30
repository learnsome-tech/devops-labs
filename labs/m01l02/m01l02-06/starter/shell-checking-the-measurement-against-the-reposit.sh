#!/usr/bin/env bash
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

cd dora
bash make-fixture-repo.sh fixture
#   fixture repository ready at fixture
git -C fixture tag -l 'deploy-*' | wc -l
#         10
git -C fixture log --format='%ad %s' --date=short -3
#   2026-02-13 document the runbook
#   2026-02-13 drop the unused column
#   2026-02-12 log the release identifier
