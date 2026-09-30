"""A rolling update, one step at a time.

Usage: python3 rolling.py
Ten replicas, surge one, unavailable one: the arithmetic a scheduler does.
"""
REPLICAS = 10
MAX_SURGE = 1
MAX_UNAVAILABLE = 1

old, new, step = REPLICAS, 0, 0
print("step  old  new  serving  capacity")
while old > 0:
    step += 1
    starting = min(MAX_SURGE + MAX_UNAVAILABLE, old)
    old -= starting
    new += starting
    serving = old + new
    print("{:<6}{:<5}{:<5}{:<9}{:.0f} percent".format(
        step, old, new, serving, serving / REPLICAS * 100))
print()
print("both versions serve traffic at once, so the schema must accept both")
