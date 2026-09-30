#!/usr/bin/env bash
# Shell session from the video, as a script you can run.
# Each bare line was typed at the prompt; the commented lines are what the
# machine answered. Run it from artifacts/lab:  bash <thisfile>

cd dora
bash make-fixture-repo.sh fixture
#   fixture repository ready at fixture
bash gaming.sh fixture
#   honest, deployments tagged when they reached production
#     deployments                     10 over 11.2 days
#     change lead time                4.0 hours (median)
#     deployment frequency            6.2 per week
#     failed deployment recovery time 556 minutes (median)
#     change fail rate                20 percent
#     deployment rework rate          20 percent
#   gamed, every commit relabelled a deployment
#     deployments                     14 over 12.2 days
#     change lead time                0.0 hours (median)
#     deployment frequency            8.0 per week
#     failed deployment recovery time no failed deployments in this window
#     change fail rate                0 percent
#     deployment rework rate          14 percent
