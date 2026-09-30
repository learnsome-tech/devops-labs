"""Feature flags: deploy on Tuesday, release on Thursday.

Usage: python3 feature_flag.py
The bucket is a hash, so a user sees the same answer on every request and on
every server, which is what makes a percentage rollout measurable.
"""
import hashlib

USERS = [f"user-{n}" for n in range(1, 21)]


def bucket(user, flag):
    digest = hashlib.sha256(f"{flag}:{user}".encode()).hexdigest()
    return int(digest[:8], 16) % 100


def enabled(user, flag, percent, kill_switch=False):
    return not kill_switch and bucket(user, flag) < percent


for percent in (0, 25, 100):
    on = [u for u in USERS if enabled(u, "new-search", percent)]
    print(f"rollout {percent:>3} percent   {len(on):>2} of 20 users   {on[:3]}")

print()
killed = sum(enabled(u, "new-search", 100, True) for u in USERS)
print("kill switch on   ", killed, "of 20 users")
print("the code shipped hours ago; only the flag value changed")
