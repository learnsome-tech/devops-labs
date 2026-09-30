"""Run the suite and print a deterministic summary, layer by layer.

Usage: python3 run_tests.py
"""
import unittest

LAYERS = ["tests/unit", "tests/integration", "tests/e2e"]
total = 0
failed = 0

for layer in LAYERS:
    suite = unittest.defaultTestLoader.discover(layer, top_level_dir=".")
    quiet = unittest.TextTestRunner(verbosity=0,
                                    stream=open("/dev/null", "w"))
    result = quiet.run(suite)
    name = layer.split("/")[1]
    print("{:<14}{:>3} tests   {}".format(
        name, result.testsRun,
        "passed" if result.wasSuccessful() else "FAILED"))
    total += result.testsRun
    failed += len(result.failures) + len(result.errors)

print("{:<14}{:>3} tests   {}".format("total", total,
                                      "green" if failed == 0 else "red"))
