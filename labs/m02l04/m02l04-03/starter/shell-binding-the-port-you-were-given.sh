#!/usr/bin/env bash
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

cd twelve-factor
python3 demos.py port
#   bad chooses    8080 whatever was asked for
#   good chooses   7654 which is what PORT asked for
