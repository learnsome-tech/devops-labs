#!/usr/bin/env bash
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

cd ci && bash pipeline.sh
#   stage:lint checking formatting and obvious mistakes
#   stage:test running the test suite
#   unit            4 tests   passed
#   integration     1 tests   passed
#   e2e             1 tests   passed
#   total           6 tests   green
#   stage:build producing one immutable artifact
#   artifact dist/calc-2.4.0.tar
#   digest   3237998773
#   stage:gate artifact is built once and promoted, never rebuilt
#   pipeline passed
