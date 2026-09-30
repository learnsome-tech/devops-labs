"""Check a postmortem against the structure and the culture it needs.

Usage: python3 lint_postmortem.py <file>
Sections come from the example postmortem in the SRE book appendix. The blame
check looks for language that names a person as the cause.
"""
import re
import sys

REQUIRED = ["Date", "Authors", "Status", "Summary", "Impact", "Root Causes",
            "Trigger", "Detection", "Resolution", "Action Items",
            "Lessons Learned", "What went well", "What went wrong",
            "Where we got lucky", "Timeline", "Supporting information"]
BLAME = ["fault", "careless", "should have known", "failed to check",
         "sloppy", "incompetent", "to blame"]

text = open(sys.argv[1] if len(sys.argv) > 1 else "postmortem.md").read()

missing = [s for s in REQUIRED if s.lower() not in text.lower()]
blame = [w for w in BLAME if w in text.lower()]
ROW = r"^\| (?!Action item)(?!---)(.+?) \| (\w+) \|"
KINDS = {"prevent", "mitigate", "detect", "process"}
actions = re.findall(ROW, text, re.M)
owned = [a for a in actions if a[1] in KINDS]

print("sections required   {}".format(len(REQUIRED)))
print("sections missing    {}".format(len(missing) or "none"))
print("action items        {}".format(len(actions)))
print("classified items    {}".format(len(owned)))
found = ", ".join(blame) if blame else "none found"
print("blaming language    {}".format(found))
print("verdict             {}".format(
    "ready for review" if not missing and not blame else "send it back"))
