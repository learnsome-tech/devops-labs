"""The unit under test: small, pure, and fast to check."""


def add(left, right):
    return left + right


def apply_discount(pennies, percent):
    if not 0 <= percent <= 100:
        raise ValueError("percent out of range")
    return pennies - pennies * percent // 100
