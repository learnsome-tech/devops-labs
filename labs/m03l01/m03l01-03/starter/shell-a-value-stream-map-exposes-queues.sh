#!/usr/bin/env bash
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

python3 sdlc/value_stream.py
#   step                        process  lead
#   write the change            4.0      4.0
#   wait for review             0.5      26.0
#   review and rework           1.5      3.0
#   wait for the release train  0.0      96.0
#   manual regression test      6.0      18.0
#   change advisory board       0.5      40.0
#   deploy                      0.5      1.0
#   
#   process time  13.0 hours
#   lead time     188.0 hours
#   flow efficiency 6.9 percent
#   the queues, not the work, are the delivery problem
