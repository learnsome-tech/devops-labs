"""Import one variant in a throwaway directory and report what it does.

Run as:  python3 probe.py <variant directory>
Prints one JSON object so the audit can compare variants without importing
two modules called app into one interpreter.
"""
import importlib.util
import inspect
import io
import json
import os
import signal
import sys
from contextlib import redirect_stdout

variant = os.path.abspath(sys.argv[1])
sys.path.insert(0, variant)
report = {"port": None, "sigterm": False, "stdout": "", "error": None}

try:
    spec = importlib.util.spec_from_file_location(
        "variant_app", os.path.join(variant, "app.py"))
    app = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(app)
    report["port"] = app.choose_port()
    report["sigterm"] = signal.getsignal(signal.SIGTERM) not in (
        signal.SIG_DFL, signal.SIG_IGN, None)
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        if len(inspect.signature(app.handle).parameters) == 2:
            app.handle("/quotes/1", {})
        else:
            app.handle("/quotes/1")
    report["stdout"] = buffer.getvalue().strip()
except Exception as problem:                      # a violation, not a crash
    report["error"] = type(problem).__name__

print(json.dumps(report, sort_keys=True))
