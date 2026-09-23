#!/usr/bin/env bash
# DevOps & Site Reliability Engineering — lesson m02l06 — Admin Processes And The Open Source Update
# https://learnsome.tech/courses/devops-course/watch?lesson=m02l06
# © LearnSome.tech
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

cd twelve-factor
python3 audit.py
#   factor                     bad    good
#   I   Codebase               FAIL   PASS
#   II  Dependencies           FAIL   PASS
#   III Config                 FAIL   PASS
#   IV  Backing services       FAIL   PASS
#   V   Build, release, run    FAIL   PASS
#   VI  Processes              FAIL   PASS
#   VII Port binding           FAIL   PASS
#   VIIIConcurrency            FAIL   PASS
#   IX  Disposability          FAIL   PASS
#   X   Dev prod parity        FAIL   PASS
#   XI  Logs                   FAIL   PASS
#   XII Admin processes        FAIL   PASS
#   totals                     0/12   12/12
