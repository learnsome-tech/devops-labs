"""The same quote service, one factor at a time, done the manifesto's way."""
import json
import os
import signal
import sys

RELEASE = os.environ.get("RELEASE", "unknown")      # V   build, release, run
DATABASE_URL = os.environ["DATABASE_URL"]           # III IV config from env
API_KEY = os.environ["API_KEY"]                     # III secrets from env


def log(event, **fields):
    """XI  one event per line, on stdout, for the platform to route."""
    record = {"event": event, "release": RELEASE}
    record.update(fields)
    print(json.dumps(record, sort_keys=True), flush=True)


def choose_port():
    """VII  the platform hands the port down; the app binds it."""
    return int(os.environ["PORT"])


def handle(path, store):
    """VI  every request is served from a backing service, not from memory."""
    store["hits"] = store.get("hits", 0) + 1
    log("request", path=path, hits=store["hits"])
    return 200, "hits {}".format(store["hits"])


def serve(port, store):
    """VII  bind the port the platform handed down and answer on it."""
    from http.server import BaseHTTPRequestHandler, HTTPServer

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            status, body = handle(self.path, store)
            self.send_response(status)
            self.end_headers()
            self.wfile.write(body.encode())

        def log_message(self, *args):
            pass

    return HTTPServer(("127.0.0.1", port), Handler)


def shutdown(signum, frame):
    """IX  a fast, clean exit on the signal the platform actually sends."""
    log("shutdown", signal=signum)
    sys.exit(0)


signal.signal(signal.SIGTERM, shutdown)
