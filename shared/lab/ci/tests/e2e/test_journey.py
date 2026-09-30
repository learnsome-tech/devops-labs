import unittest

from app.calc import add, apply_discount


class JourneyTests(unittest.TestCase):
    """The slowest, broadest test: one whole customer journey."""

    def test_basket_to_receipt(self):
        basket = add(1000, 2500)
        self.assertEqual(apply_discount(basket, 20), 2800)
