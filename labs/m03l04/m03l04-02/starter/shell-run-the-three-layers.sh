#!/usr/bin/env bash
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

cd ci && python3 run_tests.py
#   unit            4 tests   passed
#   integration     1 tests   passed
#   e2e             1 tests   passed
#   total           6 tests   green
