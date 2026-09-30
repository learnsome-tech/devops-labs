"""The same quote service, one factor at a time, done the manifesto's way."""
import json
import os
import signal
import sys

RELEASE = os.environ.get("RELEASE", "unknown")      # V   build, release, run
DATABASE_URL = os.environ["DATABASE_URL"]           # III IV config from env
API_KEY = os.environ["API_KEY"]                     # III secrets from env
