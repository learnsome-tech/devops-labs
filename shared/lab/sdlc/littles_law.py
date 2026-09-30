"""Little's law, applied to a delivery pipeline.

Usage: python3 littles_law.py
Lead time equals work in progress divided by throughput. That is arithmetic,
not opinion, so the only ways to shorten lead time are fewer things at once
or more finished per week.
"""
SCENARIOS = [
    ("today", 18, 6),
    ("hire two people, same habits", 24, 8),
    ("halve the work in progress", 9, 6),
    ("halve it and deploy twice as often", 9, 12),
]

print("scenario                             wip  per week  lead time")
for name, wip, throughput in SCENARIOS:
    weeks = wip / throughput
    print("{:<37}{:<5}{:<10}{:.1f} weeks".format(name, wip, throughput, weeks))
print()
print("more people changed nothing: work in progress grew with the team")
print("the lever is finishing, not starting")
