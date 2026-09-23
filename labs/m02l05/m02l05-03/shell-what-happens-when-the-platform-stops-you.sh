#!/usr/bin/env bash
# DevOps & Site Reliability Engineering — lesson m02l05 — Disposability, Dev Prod Parity And Logs
# https://learnsome.tech/courses/devops-course/watch?lesson=m02l05
# © LearnSome.tech
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

cd twelve-factor
python3 demos.py signal
#   bad   exit -15  was killed by the signal
#   good  exit 0    handled the signal
#         logged {"event": "shutdown", "release": "2026.09.11-a1b2c3", "signal": 15}
