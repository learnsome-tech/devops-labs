import unittest

from app.calc import add, apply_discount


class UnitTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_discount(self):
        self.assertEqual(apply_discount(1000, 10), 900)

    def test_no_discount(self):
        self.assertEqual(apply_discount(1000, 0), 1000)

    def test_rejects_silly_percent(self):
        with self.assertRaises(ValueError):
            apply_discount(1000, 140)
