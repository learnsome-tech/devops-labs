#!/usr/bin/env bash
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

cd twelve-factor
python3 demos.py admin
#   one-off process, same code, same config, own life cycle
#      {"database": "sqlite:///quotes", "event": "migrate", "release": "2026.09.11-a1b2c3"}
#      schema at revision two
#   bad runs the migration at import time: True
