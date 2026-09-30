"""What a platform is for, in hours: the same toil, multiplied by teams.

Usage: python3 toil.py
An engineer year is taken as sixteen hundred productive hours.
"""
TASKS = [
    ("stand up a new service", 6.0, 4),
    ("wire logging and metrics", 3.0, 4),
    ("get a database provisioned", 8.0, 3),
    ("renew a certificate", 1.5, 12),
    ("copy a pipeline from another repo", 2.5, 6),
    ("debug somebody else's pipeline", 4.0, 10),
    ("patch and rebuild base images", 3.0, 12),
    ("chase an approval", 2.0, 24),
]
TEAMS = 60
PLATFORM_TEAM = 5
YEAR = 1600.0
REMOVED = 0.8

print("task                               hours  times  per team")
manual = 0.0
for name, hours, times in TASKS:
    manual += hours * times
    print("{:<35}{:<7.1f}{:<7}{:.0f}".format(name, hours, times, hours * times))

fleet = manual * TEAMS
saved = fleet * REMOVED
cost = PLATFORM_TEAM * YEAR
print()
print("per team each year      {:.0f} hours".format(manual))
print("across {} teams         {:.0f} hours".format(TEAMS, fleet))
print("a golden path removes   {:.0f} hours, {:.1f} engineer years".format(
    saved, saved / YEAR))
print("platform team of {}      costs {:.0f} hours".format(PLATFORM_TEAM, cost))
print("break even at           {:.0f} teams".format(cost / (manual * REMOVED)))
print("a platform pays for itself by serving many teams, not by serving one")
