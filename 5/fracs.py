from typing import Literal
from math import gcd

type Frac = list[int, int]


def sim(frac: Frac) -> Frac:
    """Simplify the fraction `frac`"""
    n = abs(gcd(frac[0], frac[1]))
    s = -1 if not is_positive(frac) else 1
    return [s * abs(frac[0] // n), abs(frac[1] // n)]


def add_frac(frac1: Frac, frac2: Frac) -> Frac:
    """Add `frac1` and `frac2`"""
    return sim([frac1[0] * frac2[1] + frac2[0] * frac1[1], frac1[1] * frac2[1]])


def sub_frac(frac1: Frac, frac2: Frac) -> Frac:
    """Subtract `frac2` from `frac1`"""
    return add_frac(frac1, [-frac2[0], frac2[1]])


def mul_frac(frac1: Frac, frac2: Frac) -> Frac:
    """Multiply `frac1` and `frac2`"""
    return sim([frac1[0] * frac2[0], frac1[1] * frac2[1]])


def div_frac(frac1: Frac, frac2: Frac) -> Frac:
    """Divide `frac1` by `frac2`"""
    return mul_frac(frac1, [frac2[1], frac2[0]])


def is_positive(frac: Frac) -> bool:
    """Check whether `frac` is positive"""
    return not is_zero(frac) and ((frac[0] < 0) == (frac[1] < 0))


def is_zero(frac: Frac) -> bool:
    """Check whether `frac` is zero"""
    return frac[0] == 0


def cmp_frac(frac1: Frac, frac2: Frac) -> Literal[-1] | Literal[0] | Literal[1]:
    """Compare `frac1` and `frac2`

    Returns 0 if `frac1` == `frac2`, -1 if `frac1` < `frac2`, and 1 if
    `frac1` > `frac2`
    """
    a = frac1[0] * frac2[1]
    b = frac2[0] * frac1[1]
    s = -1 if frac1[1] * frac2[1] < 0 else 1
    return 0 if a == b else s if a > b else -s


def frac2float(frac: Frac) -> float:
    """Convert `frac` into a `float`"""
    return float(frac[0] / frac[1])


import unittest


class TestFractions(unittest.TestCase):
    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([-1, 2], [1, -2]), [-1, 1])
        self.assertEqual(add_frac([-1, 2], [1, 2]), [0, 1])
        self.assertEqual(add_frac([2, 4], [3, 6]), [1, 1])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([-1, 2], [1, -2]), [0, 1])
        self.assertEqual(sub_frac([-1, 2], [1, 2]), [-1, 1])
        self.assertEqual(sub_frac([2, 4], [3, 6]), [0, 1])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([-1, 2], [1, -2]), [1, 4])
        self.assertEqual(mul_frac([-1, 2], [1, 2]), [-1, 4])
        self.assertEqual(mul_frac([2, 4], [3, 6]), [1, 4])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([-1, 2], [1, -2]), [1, 1])
        self.assertEqual(div_frac([-1, 2], [1, 2]), [-1, 1])
        self.assertEqual(div_frac([2, 4], [3, 6]), [1, 1])

    def test_is_positive(self):
        self.assertFalse(is_positive([-1, 2]))
        self.assertFalse(is_positive([1, -2]))
        self.assertFalse(is_positive([0, 1]))
        self.assertFalse(is_positive([0, 2]))
        self.assertTrue(is_positive([3, 1]))
        self.assertTrue(is_positive([6, 2]))

    def test_is_zero(self):
        self.assertFalse(is_zero([-1, 2]))
        self.assertFalse(is_zero([1, -2]))
        self.assertTrue(is_zero([0, 1]))
        self.assertTrue(is_zero([0, 2]))
        self.assertFalse(is_zero([3, 1]))
        self.assertFalse(is_zero([6, 2]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([-1, 2], [6, 2]), -1)
        self.assertEqual(cmp_frac([1, -2], [-1, 2]), 0)
        self.assertEqual(cmp_frac([0, 1], [1, -2]), 1)
        self.assertEqual(cmp_frac([0, 2], [0, 1]), 0)
        self.assertEqual(cmp_frac([3, 1], [0, 2]), 1)
        self.assertEqual(cmp_frac([6, 2], [3, 1]), 0)

    def test_frac2float(self):
        self.assertEqual(frac2float([-1, 2]), -0.5)
        self.assertEqual(frac2float([1, -2]), -0.5)
        self.assertEqual(frac2float([0, 1]), 0.0)
        self.assertEqual(frac2float([0, 2]), 0.0)
        self.assertEqual(frac2float([3, 1]), 3.0)
        self.assertEqual(frac2float([6, 2]), 3.0)
        self.assertAlmostEqual(frac2float([1, 3]), 0.333333333)


if __name__ == "__main__":
    unittest.main()
