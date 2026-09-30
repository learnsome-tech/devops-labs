#!/usr/bin/env bash
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

bun run ci/validate-workflow.ts ci/pipeline.yml
#   workflow  pipeline.yml
#   jobs      3 (test, build, deploy)
#   steps     7
#   verdict   valid
