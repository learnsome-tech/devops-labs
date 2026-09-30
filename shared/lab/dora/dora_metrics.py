"""Compute DORA's five software delivery metrics from a real git history.

Usage: python3 dora_metrics.py <repository>

The repository is read, never written. A deployment is an annotated tag named
deploy-NNNN. A change is a commit. A deployment is judged failed when a later
commit carries the trailer Remediates: <that tag>, which is also what makes
the deployment carrying that commit unplanned, and therefore rework.
"""
import re
import statistics
import subprocess
import sys
from datetime import datetime

REPO = sys.argv[1] if len(sys.argv) > 1 else "."
TRAILER = re.compile(r"^Remediates:\s*(deploy-\d+)\s*$", re.M)


def git(*args):
    out = subprocess.run(["git", "-C", REPO, *args],
                         capture_output=True, text=True, check=True)
    return out.stdout.strip()


def when(text):
    return datetime.fromisoformat(text)


def deployments():
    """Every deployment tag, oldest first, with the commits it carried."""
    shape = "%(refname:short) %(taggerdate:iso-strict)"
    rows = git("for-each-ref", "--sort=taggerdate", "--format=" + shape,
               "refs/tags/deploy-*").splitlines()
    pairs = (row.split(" ", 1) for row in rows)
    tags = [(name, when(date)) for name, date in pairs]
    out, previous = [], None
    for name, date in tags:
        span = f"{previous}..{name}" if previous else name
        log = git("log", "--format=%H%x1f%aI%x1f%B%x1e", span)
        changes = []
        for entry in (e for e in log.split("\x1e") if e.strip()):
            sha, authored, body = entry.strip().split("\x1f", 2)
            changes.append({"sha": sha, "authored": when(authored),
                            "body": body})
        out.append({"tag": name, "at": date, "changes": changes})
        previous = name
    return out


def report(deploys):
    remediations = {}
    for deploy in deploys:
        for change in deploy["changes"]:
            for failed in TRAILER.findall(change["body"]):
                remediations[failed] = deploy
    lead = [(deploy["at"] - change["authored"]).total_seconds() / 3600
            for deploy in deploys for change in deploy["changes"]]
    window = (deploys[-1]["at"] - deploys[0]["at"]).total_seconds() / 86400
    recovery = [(fix["at"] - broken["at"]).total_seconds() / 60
                for broken in deploys if broken["tag"] in remediations
                for fix in [remediations[broken["tag"]]]]
    rework = [d for d in deploys
              if any(TRAILER.search(c["body"]) for c in d["changes"])]
    failed = [d for d in deploys if d["tag"] in remediations]
    total = len(deploys)
    print(f"deployments                     {total} over {window:.1f} days")
    middle = statistics.median(lead)
    print(f"change lead time                {middle:.1f} hours (median)")
    print(f"deployment frequency            {total / window * 7:.1f} per week")
    healed = (f"{statistics.median(recovery):.0f} minutes (median)" if recovery
              else "no failed deployments in this window")
    print(f"failed deployment recovery time {healed}")
    print("change fail rate                "
          f"{len(failed) / total * 100:.0f} percent")
    print("deployment rework rate          "
          f"{len(rework) / total * 100:.0f} percent")


report(deployments())
