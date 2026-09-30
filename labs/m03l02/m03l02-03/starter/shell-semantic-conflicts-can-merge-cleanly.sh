#!/usr/bin/env bash
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

bash git/semantic_conflict.sh
#   merge rename   clean, no conflict
#   merge caller   clean, no conflict
#   build    red: cannot import apply_discount from app.calc
#   verdict  git merged the text; only the build noticed the meaning
