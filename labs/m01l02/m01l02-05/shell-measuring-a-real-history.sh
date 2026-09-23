#!/usr/bin/env bash
# DevOps & Site Reliability Engineering — lesson m01l02 — Throughput: Change Lead Time And Deployment Frequency
# https://learnsome.tech/courses/devops-course/watch?lesson=m01l02
# © LearnSome.tech
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

cd dora
bash make-fixture-repo.sh fixture
#   fixture repository ready at fixture
python3 dora_metrics.py fixture
#   deployments                     10 over 11.2 days
#   change lead time                4.0 hours (median)
#   deployment frequency            6.2 per week
#   failed deployment recovery time 556 minutes (median)
#   change fail rate                20 percent
#   deployment rework rate          20 percent
