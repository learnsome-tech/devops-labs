"""A value stream map, in numbers: where the week actually goes.

Usage: python3 value_stream.py
Process time is hands on the work. Lead time is the clock on the wall.
"""
STEPS = [
    ("write the change", 4.0, 4.0),
    ("wait for review", 0.5, 26.0),
    ("review and rework", 1.5, 3.0),
    ("wait for the release train", 0.0, 96.0),
    ("manual regression test", 6.0, 18.0),
    ("change advisory board", 0.5, 40.0),
    ("deploy", 0.5, 1.0),
]

print("step                        process  lead")
for name, process, lead in STEPS:
    print("{:<28}{:<9.1f}{:.1f}".format(name, process, lead))

process_total = sum(s[1] for s in STEPS)
lead_total = sum(s[2] for s in STEPS)
print()
print("process time  {:.1f} hours".format(process_total))
print("lead time     {:.1f} hours".format(lead_total))
print("flow efficiency {:.1f} percent".format(process_total / lead_total * 100))
print("the queues, not the work, are the delivery problem")
