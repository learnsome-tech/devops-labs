"""Read an incident timeline and produce the numbers a postmortem needs.

Usage: python3 timeline.py
The events are the published Shakespeare example from the SRE book appendix,
so the arithmetic here is the arithmetic in a real postmortem.
"""
from datetime import datetime

EVENTS = [
    ("14:51", "new sonnet discovered, traffic starts to climb"),
    ("14:53", "traffic to the search service increases sharply"),
    ("14:54", "OUTAGE BEGINS, servers start returning errors"),
    ("14:55", "monitoring pages the on-call engineer"),
    ("15:01", "INCIDENT BEGINS, incident commander named"),
    ("15:36", "OUTAGE MITIGATED, traffic moved to a sacrificial cluster"),
    ("16:00", "OUTAGE ENDS, all clusters serving"),
    ("16:30", "INCIDENT ENDS, thirty minutes of nominal performance"),
]


def at(clock):
    return datetime.strptime(clock, "%H:%M")


def minutes(start, end):
    return int((at(end) - at(start)).total_seconds() // 60)


for clock, what in EVENTS:
    print("{}  {}".format(clock, what))

print()
print("time to detect    {:>3} minutes".format(minutes("14:54", "14:55")))
print("time to declare   {:>3} minutes".format(minutes("14:54", "15:01")))
print("time to mitigate  {:>3} minutes".format(minutes("14:54", "15:36")))
print("user impact       {:>3} minutes".format(minutes("14:54", "16:00")))
print("incident length   {:>3} minutes".format(minutes("15:01", "16:30")))
