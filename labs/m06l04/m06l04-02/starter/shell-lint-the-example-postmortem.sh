#!/usr/bin/env bash
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

python3 incident/lint_postmortem.py incident/postmortem.md
#   sections required   16
#   sections missing    none
#   action items        4
#   classified items    4
#   blaming language    none found
#   verdict             ready for review
