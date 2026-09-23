#!/usr/bin/env bash
# DevOps & Site Reliability Engineering — lesson m04l02 — Deployment Strategies: Rolling Updates
# https://learnsome.tech/courses/devops-course/watch?lesson=m04l02
# © LearnSome.tech
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

python3 release/rolling.py
#   step  old  new  serving  capacity
#   1     8    2    10       100 percent
#   2     6    4    10       100 percent
#   3     4    6    10       100 percent
#   4     2    8    10       100 percent
#   5     0    10   10       100 percent
#   
#   both versions serve traffic at once, so the schema must accept both
