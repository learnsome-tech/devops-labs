#!/usr/bin/env bash
# DevOps & Site Reliability Engineering — lesson m05l02 — Percentiles Rather Than Averages
# https://learnsome.tech/courses/devops-course/watch?lesson=m05l02
# © LearnSome.tech
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

python3 slo/percentiles.py
#   hour        mean    p50     p90     p95     p99
#   morning     50.5    50      50      50      60
#   afternoon   50.5    48      48      48      98
#   
#   the mean says nothing changed; one request in twenty got twice as slow
