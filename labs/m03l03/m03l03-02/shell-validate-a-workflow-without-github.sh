#!/usr/bin/env bash
# DevOps & Site Reliability Engineering — lesson m03l03 — Continuous Integration
# https://learnsome.tech/courses/devops-course/watch?lesson=m03l03
# © LearnSome.tech
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

bun run ci/validate-workflow.ts ci/pipeline.yml
#   workflow  pipeline.yml
#   jobs      3 (test, build, deploy)
#   steps     7
#   verdict   valid
