#!/usr/bin/env bash
# DevOps & Site Reliability Engineering — lesson m03l04 — Testing Strategies And The Test Pyramid
# https://learnsome.tech/courses/devops-course/watch?lesson=m03l04
# © LearnSome.tech
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

cd ci && python3 run_tests.py
#   unit            4 tests   passed
#   integration     1 tests   passed
#   e2e             1 tests   passed
#   total           6 tests   green
