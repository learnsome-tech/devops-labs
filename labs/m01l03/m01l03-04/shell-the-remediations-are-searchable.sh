#!/usr/bin/env bash
# DevOps & Site Reliability Engineering — lesson m01l03 — Instability: Change Fail Rate And Deployment Rework Rate
# https://learnsome.tech/courses/devops-course/watch?lesson=m01l03
# © LearnSome.tech
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

cd dora
bash make-fixture-repo.sh fixture
#   fixture repository ready at fixture
git -C fixture log --grep=Remediates --format='%s'
#   put the old credential back
#   restore the old search index
python3 dora_metrics.py fixture | tail -3
#   failed deployment recovery time 556 minutes (median)
#   change fail rate                20 percent
#   deployment rework rate          20 percent
