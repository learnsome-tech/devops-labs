#!/usr/bin/env bash
# DevOps & Site Reliability Engineering — lesson m01l04 — Restoration: Failed Deployment Recovery Time
# https://learnsome.tech/courses/devops-course/watch?lesson=m01l04
# © LearnSome.tech
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

cd dora
bash make-fixture-repo.sh fixture
#   fixture repository ready at fixture
bash deploy_times.sh fixture deploy-0007 deploy-0008
#   deploy-0007  2026-02-10 16:00:00 +0000
#   deploy-0008  2026-02-11 09:20:00 +0000
python3 dora_metrics.py fixture | sed -n '4p'
#   failed deployment recovery time 556 minutes (median)
