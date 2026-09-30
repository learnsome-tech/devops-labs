import unittest

from app.calc import apply_discount


class IntegrationTests(unittest.TestCase):
    """Two parts together: the price rule and the order total."""

    def test_order_total(self):
        lines = [(1000, 10), (2500, 0)]
        total = sum(apply_discount(p, d) for p, d in lines)
        self.assertEqual(total, 3400)
