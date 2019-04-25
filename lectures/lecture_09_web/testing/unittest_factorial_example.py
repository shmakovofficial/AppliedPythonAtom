#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest


def factorial(n):
    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        f = factorial(5)
        self.assertEqual(f, 120)


if __name__ == "__main__":
    unittest.main()

