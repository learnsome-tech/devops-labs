"""Quote service written the way services were written before the manifesto.

Every numbered comment marks a factor this file breaks on purpose.
"""
import logging
import sqlite3
import threading

ENV = "development"             # X    dev and prod take different branches
DB_PATH = "quotes.db"           # III  config is baked into the code
API_KEY = "shhh-do-not-tell"    # III  a credential in version control
PORT = 8080                     # VII  the port is not the platform's choice
LOG_FILE = "quotes.log"         # XI   logs are a file this process manages

logging.basicConfig(filename=LOG_FILE, level=logging.INFO)

HITS = 0                        # VI   request state lives in the process
CACHE = {}                      # VI   and dies with the process
LOCK = threading.Lock()         # VIII scale means more threads in here


def migrate():
    """XII  the schema change runs inside the web process, at import time."""
    db = sqlite3.connect(DB_PATH)
    db.execute("CREATE TABLE IF NOT EXISTS quotes (id INTEGER, body TEXT)")
    db.commit()
    db.close()


def choose_port():
    """VII  a constant, so two copies on one host collide."""
    return PORT


def handle(path):
    """IV  the store is a local file, not an attached resource."""
    global HITS
    with LOCK:
        HITS += 1
    if ENV == "production":
        logging.info("served %s in prod", path)
    else:
        logging.info("served %s", path)
    return 200, "hits {}".format(HITS)


migrate()
