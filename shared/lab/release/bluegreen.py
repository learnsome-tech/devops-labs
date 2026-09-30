"""Blue green: two full environments, one router.

Usage: python3 bluegreen.py
"""
STAGES = [
    ("blue live, green idle", 100, 0),
    ("green built and warmed", 100, 0),
    ("smoke tests against green", 100, 0),
    ("router switched", 0, 100),
    ("blue kept warm for rollback", 0, 100),
]

print("stage                         blue  green")
for name, blue, green in STAGES:
    print("{:<30}{:<6}{}".format(name, blue, green))
print()
print("rollback is one router change back to blue, not a redeploy")
print("cost of the strategy: two production sized environments at once")
