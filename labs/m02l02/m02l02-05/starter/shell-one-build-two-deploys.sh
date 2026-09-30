#!/usr/bin/env bash
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

cd twelve-factor
python3 demos.py config
#   bad, from the source file    quotes.db shhh-do-not-tell
#   good, from the environment   sqlite:///quotes from-the-environment
#   good, second deploy          postgres://quotes/prod 2026.09.12-ff0011
#   same build, different config, and no credential in the repository
