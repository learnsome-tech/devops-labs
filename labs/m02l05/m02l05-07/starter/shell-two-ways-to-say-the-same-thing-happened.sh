#!/usr/bin/env bash
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

cd twelve-factor
python3 demos.py logs
#   bad on stdout    ''
#   bad wrote        quotes.log, which it now has to rotate
#   good on stdout   {"event": "request", "hits": 1, "path": "/quotes/1", "release": "2026.09.11-a1b2c3"}
#   good wrote       nothing: routing is the platform's problem
