"""A canary release with an automated gate.

Usage: python3 canary.py
Each wave sends a share of traffic to the new version and compares its error
rate with the version already running. The gate, not a human, decides.
"""
BASELINE_ERROR_RATE = 0.002     # errors per request on the old version
THRESHOLD = 3.0                 # how many times worse the canary may be
WAVES = [(1, 0.0021), (5, 0.0024), (25, 0.0089)]

print("wave  traffic  canary errors  ratio  decision")
promoted = 0
for share, observed in WAVES:
    ratio = observed / BASELINE_ERROR_RATE
    ok = ratio <= THRESHOLD
    print("{:<6}{:<9}{:<15.4f}{:<7.2f}{}".format(
        share, f"{share} percent", observed, ratio,
        "promote" if ok else "abort and roll back"))
    if not ok:
        print()
        print(f"blast radius: {share} percent of users, for one wave")
        break
    promoted = share
else:
    print("full rollout")
