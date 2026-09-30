#!/usr/bin/env bash
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

python3 release/feature_flag.py
#   rollout   0 percent    0 of 20 users   []
#   rollout  25 percent    5 of 20 users   ['user-1', 'user-4', 'user-11']
#   rollout 100 percent   20 of 20 users   ['user-1', 'user-2', 'user-3']
#   
#   kill switch on    0 of 20 users
#   the code shipped hours ago; only the flag value changed
