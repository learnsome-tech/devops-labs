#!/usr/bin/env bash
# DevOps & Site Reliability Engineering — lesson m04l04 — Deployment Strategies: Canary Releases
# https://learnsome.tech/courses/devops-course/watch?lesson=m04l04
# © LearnSome.tech
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

python3 release/canary.py
#   wave  traffic  canary errors  ratio  decision
#   1     1 percent0.0021         1.05   promote
#   5     5 percent0.0024         1.20   promote
#   25    25 percent0.0089         4.45   abort and roll back
#   
#   blast radius: 25 percent of users, for one wave
