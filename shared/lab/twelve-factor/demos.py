"""Show one factor at a time by running both variants of the app.

Usage: python3 demos.py <config|port|logs|signal|admin>
Each demo runs real processes in a throwaway directory, so the bad variant
is free to scatter the files it insists on writing.
"""
import importlib.util
import io
import os
import subprocess
import sys
import threading
import tempfile
import time
import urllib.request
from contextlib import redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
ENV = {"PORT": "7654", "DATABASE_URL": "sqlite:///quotes",
       "API_KEY": "from-the-environment", "RELEASE": "2026.09.11-a1b2c3"}


def load(variant):
    """Import one variant's app.py, in a directory it may safely dirty."""
    os.chdir(tempfile.mkdtemp(prefix="factor-"))
    path = os.path.join(HERE, variant, "app.py")
    spec = importlib.util.spec_from_file_location(f"{variant}_app", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def child(variant, snippet, extra=None):
    """Run a snippet against one variant in a separate process."""
    env = {**os.environ, **ENV, **(extra or {})}
    env["PYTHONPATH"] = os.path.join(HERE, variant)
    done = subprocess.run([sys.executable, "-c", snippet],
                          cwd=tempfile.mkdtemp(prefix="factor-"),
                          env=env, capture_output=True, text=True)
    return done


def config():
    bad = child("bad", "import app; print(app.DB_PATH, app.API_KEY)")
    good = child("good", "import app; print(app.DATABASE_URL, app.API_KEY)")
    other = child("good", "import app; print(app.DATABASE_URL, app.RELEASE)",
                  {"DATABASE_URL": "postgres://quotes/prod",
                   "RELEASE": "2026.09.12-ff0011"})
    print("bad, from the source file   ", bad.stdout.strip())
    print("good, from the environment  ", good.stdout.strip())
    print("good, second deploy         ", other.stdout.strip())
    print("same build, different config, and no credential in the repository")


def port():
    bad = load("bad")
    print("bad chooses   ", bad.choose_port(), "whatever was asked for")
    os.environ.update(ENV)
    good = load("good")
    asked = int(os.environ["PORT"])
    print("good chooses  ", good.choose_port(), "which is what PORT asked for")
    server = good.serve(asked, {})
    threading.Thread(target=server.handle_request, daemon=True).start()
    body = urllib.request.urlopen(f"http://127.0.0.1:{asked}/quotes/1").read()
    server.server_close()
    print("served        ", body.decode())


def logs():
    bad = child("bad", "import app; app.handle('/quotes/1')")
    good = child("good", "import app; app.handle('/quotes/1', {})")
    print("bad on stdout   ", repr(bad.stdout.strip()))
    print("bad wrote       ", "quotes.log, which it now has to rotate")
    print("good on stdout  ", good.stdout.strip())
    print("good wrote      ", "nothing: routing is the platform's problem")


def signal_demo():
    snippet = "import app, time; time.sleep(30)"
    for variant in ("bad", "good"):
        env = dict(os.environ, **ENV)
        env["PYTHONPATH"] = os.path.join(HERE, variant)
        proc = subprocess.Popen([sys.executable, "-c", snippet],
                                cwd=tempfile.mkdtemp(prefix="factor-"),
                                env=env, stdout=subprocess.PIPE, text=True)
        time.sleep(0.4)
        proc.terminate()
        out, _ = proc.communicate(timeout=10)
        how = ("handled the signal" if proc.returncode == 0
               else "was killed by the signal")
        print(f"{variant:<5} exit {proc.returncode:<4} {how}")
        if out.strip():
            print(f"      logged {out.strip()}")


def admin():
    env = dict(os.environ, **ENV)
    done = subprocess.run([sys.executable, "manage.py", "migrate"],
                          cwd=os.path.join(HERE, "good"),
                          env=env, capture_output=True, text=True)
    print("one-off process, same code, same config, own life cycle")
    for line in done.stdout.strip().split("\n"):
        print("  ", line)
    bad_source = open(os.path.join(HERE, "bad", "app.py")).read()
    ran_at_import = "\nmigrate()" in bad_source
    print("bad runs the migration at import time:", ran_at_import)


DEMOS = {"config": config, "port": port, "logs": logs,
         "signal": signal_demo, "admin": admin}
DEMOS[sys.argv[1]]()
