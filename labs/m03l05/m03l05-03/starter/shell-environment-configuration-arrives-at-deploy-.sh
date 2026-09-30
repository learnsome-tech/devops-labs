#!/usr/bin/env bash
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

cd ci && ENVIRONMENT=staging bash deploy.sh
#   release  2.4.0-staging
#   config   from the environment, not from the artifact
#   deployed staging
