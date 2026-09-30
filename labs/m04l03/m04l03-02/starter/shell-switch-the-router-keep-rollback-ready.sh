#!/usr/bin/env bash
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

python3 release/bluegreen.py
#   stage                         blue  green
#   blue live, green idle         100   0
#   green built and warmed        100   0
#   smoke tests against green     100   0
#   router switched               0     100
#   blue kept warm for rollback   0     100
#   
#   rollback is one router change back to blue, not a redeploy
#   cost of the strategy: two production sized environments at once
