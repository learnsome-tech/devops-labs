#!/usr/bin/env bash
# DevOps & Site Reliability Engineering — lesson m06l02 — The Incident Lifecycle
# https://learnsome.tech/courses/devops-course/watch?lesson=m06l02
# © LearnSome.tech
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

python3 incident/timeline.py
#   14:51  new sonnet discovered, traffic starts to climb
#   14:53  traffic to the search service increases sharply
#   14:54  OUTAGE BEGINS, servers start returning errors
#   14:55  monitoring pages the on-call engineer
#   15:01  INCIDENT BEGINS, incident commander named
#   15:36  OUTAGE MITIGATED, traffic moved to a sacrificial cluster
#   16:00  OUTAGE ENDS, all clusters serving
#   16:30  INCIDENT ENDS, thirty minutes of nominal performance
#   
#   time to detect      1 minutes
#   time to declare     7 minutes
#   time to mitigate   42 minutes
#   user impact        66 minutes
#   incident length    89 minutes
