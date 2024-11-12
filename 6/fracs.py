from math import gcd


class Frac:
    """Klasa reprezentująca ułamek"""

    def __init__(self, x=0, y=1):
        n = abs(gcd(x, y))
        s = -1 if not (x < 0) == (y < 0) else 1
        self.x = s * abs(x // n)
        self.y = abs(y // n)

    def __str__(self):
        """Zwrócić ułamek jako `str` w formacie `"x/y"` lub `"x"`"""

        if self.y == 1:
            return f"{self.x}"
        else:
            return f"{self.x}/{self.y}"

    def __repr__(self):
        """Zwrócić ułamek jako `str` w formacie `"Frac(x, y)"`"""

        return f"Frac({self.x}, {self.y})"

    def __eq__(self, other):
        """Sprawdzić, czy ułamek jest równy `other`"""

        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        """Sprawdzić, czy ułamek jest mniejszy niż `other`"""

        a = self.x * other.y
        b = other.x * self.y
        return (a < b) ^ (self.y * other.y < 0)

    def __le__(self, other):
        """Sprawdzić, czy ułamek jest mniejszy niż lub równy `other`"""

        a = self.x * other.y
        b = other.x * self.y
        return a == b or (a < b) ^ (self.y * other.y < 0)

    def __add__(self, other):
        """Dodaj `self` do `other`"""

        return Frac(self.x * other.y + other.x * self.y, self.y * other.y)

    def __sub__(self, other):
        """Odejmij `other` od `self`"""

        return self + (-other)

    def __mul__(self, other):
        """Pomnóż `self` i `other`"""

        return Frac(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        """Podziel `self` przez `other`"""

        return self * ~other

    def __floordiv__(self, other):
        """Podziel `self` przez `other`"""

        res = self / other
        return Frac(res.x // res.y, 1)

    def __mod__(self, other):
        """Znajdź resztę z dzielenia `self` przez `other`"""

        return (self / other - self // other) * other

    def __pos__(self):
        """Zastosuj jednoargumentowy operator +"""

        return self

    def __neg__(self):
        """Znajdź ułamek przeciwny do `self`"""

        return Frac(-self.x, self.y)

    def __invert__(self):
        """Znajdź ułamek odwrotny do `self`"""

        return Frac(self.y, self.x)

    def __float__(self):
        """Przekonwertuj ułamek na `float`a"""

        return self.x / self.y

    def __hash__(self):
        """Shaszuj `self`"""

        return hash(float(self))


import unittest


class TestFrac(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Frac(1, 2)), "1/2")
        self.assertEqual(str(Frac(-1, 2)), "-1/2")
        self.assertEqual(str(Frac(1, -2)), "-1/2")
        self.assertEqual(str(Frac(-1)), "-1")
        self.assertEqual(str(Frac(2, 4)), "1/2")

    def test_repr(self):
        self.assertEqual(repr(Frac(1, 2)), "Frac(1, 2)")
        self.assertEqual(repr(Frac(-1, 2)), "Frac(-1, 2)")
        self.assertEqual(repr(Frac(1, -2)), "Frac(-1, 2)")
        self.assertEqual(repr(Frac(-1)), "Frac(-1, 1)")
        self.assertEqual(repr(Frac(2, 4)), "Frac(1, 2)")

    def test_cmp(self):
        self.assertEqual(Frac(), Frac(0))
        self.assertEqual(Frac(0), Frac(0, 1))
        self.assertEqual(Frac(1), Frac(1, 1))
        self.assertEqual(Frac(2, 4), Frac(3, 6))
        self.assertGreaterEqual(Frac(2, 4), Frac(3, 6))
        self.assertLessEqual(Frac(2, 4), Frac(3, 6))
        self.assertLess(Frac(-1, 2), Frac())
        self.assertLess(Frac(1, -2), Frac())
        self.assertEqual(Frac(0, 1), Frac())
        self.assertEqual(Frac(0, 2), Frac())
        self.assertGreater(Frac(3, 1), Frac())
        self.assertGreater(Frac(6, 2), Frac())
        self.assertNotEqual(Frac(-1, 2), Frac())
        self.assertNotEqual(Frac(1, -2), Frac())
        self.assertEqual(Frac(0, 1), Frac())
        self.assertEqual(Frac(0, 2), Frac())
        self.assertNotEqual(Frac(3, 1), Frac())
        self.assertNotEqual(Frac(6, 2), Frac())

    def test_add(self):
        self.assertEqual(Frac(1, 2) + Frac(1, 3), Frac(5, 6))
        self.assertEqual(Frac(-1, 2) + Frac(1, -2), Frac(-1, 1))
        self.assertEqual(Frac(-1, 2) + Frac(1, 2), Frac(0, 1))
        self.assertEqual(Frac(2, 4) + Frac(3, 6), Frac(1, 1))

    def test_sub(self):
        self.assertEqual(Frac(1, 2) - Frac(1, 3), Frac(1, 6))
        self.assertEqual(Frac(-1, 2) - Frac(1, -2), Frac(0, 1))
        self.assertEqual(Frac(-1, 2) - Frac(1, 2), Frac(-1, 1))
        self.assertEqual(Frac(2, 4) - Frac(3, 6), Frac(0, 1))

    def test_mul(self):
        self.assertEqual(Frac(1, 2) * Frac(1, 3), Frac(1, 6))
        self.assertEqual(Frac(-1, 2) * Frac(1, -2), Frac(1, 4))
        self.assertEqual(Frac(-1, 2) * Frac(1, 2), Frac(-1, 4))
        self.assertEqual(Frac(2, 4) * Frac(3, 6), Frac(1, 4))

    def test_div(self):
        self.assertEqual(Frac(1, 2) / Frac(1, 3), Frac(3, 2))
        self.assertEqual(Frac(-1, 2) / Frac(1, -2), Frac(1, 1))
        self.assertEqual(Frac(-1, 2) / Frac(1, 2), Frac(-1, 1))
        self.assertEqual(Frac(2, 4) / Frac(3, 6), Frac(1, 1))

    def test_floor_div(self):
        self.assertEqual(Frac(1, 2) // Frac(1, 3), Frac(1))
        self.assertEqual(Frac(-1, 2) // Frac(1, -2), Frac(1))
        self.assertEqual(Frac(-1, 2) // Frac(1, 2), Frac(-1))
        self.assertEqual(Frac(2, 4) // Frac(3, 6), Frac(1))

    def test_mod(self):
        self.assertEqual(Frac(1, 2) % Frac(1, 3), Frac(1, 6))
        self.assertEqual(Frac(-1, 2) % Frac(1, -2), Frac())
        self.assertEqual(Frac(2, 4) % Frac(3, 6), Frac())
        self.assertEqual(Frac(-2, 4) % Frac(3, 9), Frac(1, 6))

    def test_pos(self):
        self.assertEqual(+Frac(1, 2), Frac(1, 2))
        self.assertEqual(+Frac(-1, 2), Frac(-1, 2))
        self.assertEqual(+Frac(1, -2), Frac(1, -2))
        self.assertEqual(+Frac(-1), Frac(-1))
        self.assertEqual(+Frac(2, 4), Frac(2, 4))

    def test_neg(self):
        self.assertEqual(-Frac(1, 2), Frac(-1, 2))
        self.assertEqual(-Frac(-1, 2), Frac(1, 2))
        self.assertEqual(-Frac(1, -2), Frac(-1, -2))
        self.assertEqual(-Frac(-1), Frac(1))
        self.assertEqual(-Frac(2, 4), Frac(-2, 4))

    def test_invert(self):
        self.assertEqual(~Frac(1, 2), Frac(2, 1))
        self.assertEqual(~Frac(-1, 2), Frac(-2, 1))
        self.assertEqual(~Frac(1, -2), Frac(-2, 1))
        self.assertEqual(~Frac(-1), Frac(-1))
        self.assertEqual(~Frac(2, 4), Frac(4, 2))

    def test_float(self):
        self.assertEqual(float(Frac(-1, 2)), -0.5)
        self.assertEqual(float(Frac(1, -2)), -0.5)
        self.assertEqual(float(Frac(0, 1)), 0.0)
        self.assertEqual(float(Frac(0, 2)), 0.0)
        self.assertEqual(float(Frac(3, 1)), 3.0)
        self.assertEqual(float(Frac(6, 2)), 3.0)
        self.assertAlmostEqual(float(Frac(1, 3)), 0.333333333)

    def test_hash(self):
        self.assertEqual(hash(Frac(-1, 2)), hash(-0.5))
        self.assertEqual(hash(Frac(1, -2)), hash(-0.5))
        self.assertEqual(hash(Frac(0, 1)), hash(0.0))
        self.assertEqual(hash(Frac(0, 2)), hash(0.0))
        self.assertEqual(hash(Frac(3, 1)), hash(3.0))
        self.assertEqual(hash(Frac(6, 2)), hash(3.0))


if __name__ == "__main__":
    unittest.main()
