"""Audit both variants of the sample app against all twelve factors.

Every row is a real check: some read the source, some run the code in a
throwaway directory. Run as:  python3 audit.py
"""
import json
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
FACTORS = [
    ("I", "Codebase"), ("II", "Dependencies"), ("III", "Config"),
    ("IV", "Backing services"), ("V", "Build, release, run"),
    ("VI", "Processes"), ("VII", "Port binding"), ("VIII", "Concurrency"),
    ("IX", "Disposability"), ("X", "Dev prod parity"), ("XI", "Logs"),
    ("XII", "Admin processes"),
]


def probe(variant):
    work = tempfile.mkdtemp(prefix="factor-")
    env = dict(os.environ, PORT="7654", DATABASE_URL="sqlite:///quotes",
               API_KEY="from-the-environment", RELEASE="2026.09.11-a1b2c3")
    out = subprocess.run([sys.executable, os.path.join(HERE, "probe.py"),
                          os.path.join(HERE, variant)],
                         cwd=work, env=env, capture_output=True, text=True)
    return json.loads(out.stdout)


def check(variant):
    path = os.path.join(HERE, variant)
    files = sorted(os.listdir(path))
    source = open(os.path.join(path, "app.py")).read()
    live = probe(variant)
    return {
        "I": not [f for f in files if re.search(r"(dev|prod|staging)", f)],
        "II": "requirements.txt" in files,
        "III": "os.environ" in source and not re.search(
            r'^[A-Z_]+ = "(?!\{)', source, re.M),
        "IV": "DATABASE_URL" in source and "sqlite3" not in source,
        "V": "RELEASE" in source,
        "VI": "global " not in source,
        "VII": live["port"] == 7654,
        "VIII": "Procfile" in files and "threading" not in source,
        "IX": live["sigterm"],
        "X": 'ENV == "production"' not in source,
        "XI": live["stdout"] != "" and "filename=" not in source,
        "XII": ("manage.py" in files
                and not re.search(r"^migrate\(\)", source, re.M)),
    }


bad, good = check("bad"), check("good")
print("factor                     bad    good")
for number, name in FACTORS:
    label = "{:<4}{:<23}".format(number, name)
    print("{}{:<7}{}".format(label, "PASS" if bad[number] else "FAIL",
                             "PASS" if good[number] else "FAIL"))
print("totals                     {}/12   {}/12".format(
    sum(bad.values()), sum(good.values())))
