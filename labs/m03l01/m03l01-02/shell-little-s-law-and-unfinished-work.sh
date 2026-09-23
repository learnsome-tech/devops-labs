#!/usr/bin/env bash
# DevOps & Site Reliability Engineering — lesson m03l01 — SDLC: From Request To Running Software
# https://learnsome.tech/courses/devops-course/watch?lesson=m03l01
# © LearnSome.tech
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

python3 sdlc/littles_law.py
#   scenario                             wip  per week  lead time
#   today                                18   6         3.0 weeks
#   hire two people, same habits         24   8         3.0 weeks
#   halve the work in progress           9    6         1.5 weeks
#   halve it and deploy twice as often   9    12        0.8 weeks
#   
#   more people changed nothing: work in progress grew with the team
#   the lever is finishing, not starting
