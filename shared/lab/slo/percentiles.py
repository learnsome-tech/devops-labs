"""Why the SRE book says distributions, not averages.

Two hours of latency samples with an identical mean. Only the tail moved.
Usage: python3 percentiles.py
"""
MORNING = [50] * 95 + [60] * 5
AFTERNOON = [48] * 95 + [98] * 5


def nearest_rank(samples, percentile):
    """The smallest value at or above which that share of samples falls."""
    ordered = sorted(samples)
    index = -(-len(ordered) * percentile // 100) - 1
    return ordered[index]


def row(name, samples):
    mean = sum(samples) / len(samples)
    print("{:<12}{:<8.1f}{:<8}{:<8}{:<8}{}".format(
        name, mean,
        nearest_rank(samples, 50), nearest_rank(samples, 90),
        nearest_rank(samples, 95), nearest_rank(samples, 99)))


print("hour        mean    p50     p90     p95     p99")
row("morning", MORNING)
row("afternoon", AFTERNOON)
print()
print("the mean says nothing changed; one request in twenty got twice as slow")
