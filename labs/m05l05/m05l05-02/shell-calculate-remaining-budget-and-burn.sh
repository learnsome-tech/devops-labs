#!/usr/bin/env bash
# DevOps & Site Reliability Engineering — lesson m05l05 — Error Budgets
# https://learnsome.tech/courses/devops-course/watch?lesson=m05l05
# © LearnSome.tech
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

python3 slo/error_budget.py
#   objective                 99.9 percent over 30 days
#   error budget              2,000 failed requests
#   budget spent              1,430 requests, 71.5 percent
#   window elapsed            33.3 percent
#   burn rate                 2.14 times the sustainable rate
#   budget exhausted in       4.0 days
#   verdict                   freeze and fix
