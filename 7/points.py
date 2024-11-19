from math import sqrt


class Point:
    """Klasa reprezentująca punkt na płaszczyźnie"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Zwrócić punkt jako `str` w formacie `"(x, y)"`"""

        return f"({self.x}, {self.y})"

    def __repr__(self):
        """Zwrócić punkt jako `str` w formacie `"Point(x, y)"`"""

        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        """Sprawdzić, czy ułamek jest równy `other`"""

        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        """Dodaj `self` do `other`"""

        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Odejmij `other` od `self`"""

        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """Oblicz iloczyn skalarny `self • other`"""

        return self.x * other.x + self.y * other.y

    def cross(self, other):
        """Oblicz iloczyn wektorowy `self × other`"""

        return self.x * other.y - self.y * other.x

    def length(self):
        """Oblicz długość `self`"""

        return sqrt(self.x**2 + self.y**2)

    def __hash__(self):
        """Oblicz hash `self`"""

        return hash((self.x, self.y))


import unittest


class TestPoint(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Point(2.0, 3.0)), "(2.0, 3.0)")
        self.assertEqual(str(Point(-2, -7)), "(-2.0, -7.0)")

    def test_repr(self):
        self.assertEqual(repr(Point(2.0, 3.0)), "Point(2.0, 3.0)")
        self.assertEqual(repr(Point(-2, -7)), "Point(-2.0, -7.0)")

    def test_eq(self):
        self.assertEqual(Point(1, 2), Point(1, 2))
        self.assertEqual(Point(1, 2), Point(1.0, 2.0))
        self.assertEqual(Point(0, 0), Point(-0, 0))
        self.assertNotEqual(Point(1, 2), Point(1, 3))
        self.assertNotEqual(Point(1, 2), Point(1.1, 2.0))
        self.assertNotEqual(Point(0, 0), Point(100, 0))

    def test_add(self):
        self.assertEqual(Point(1, 2) + Point(2, 3), Point(3, 5))
        self.assertEqual(Point(1, 2) + Point(-1, -2.5), Point(0, -0.5))
        self.assertEqual(Point(0, 0) + Point(0, 0), Point(0, 0))

    def test_sub(self):
        self.assertEqual(Point(1, 2) - Point(2, 3), Point(-1, -1))
        self.assertEqual(Point(1, 2) - Point(-1, -2.5), Point(2, 4.5))
        self.assertEqual(Point(0, 0) - Point(0, 0), Point(0, 0))

    def test_mul(self):
        self.assertEqual(Point(1, 2) * Point(2, 3), 8)
        self.assertEqual(Point(1, 2) * Point(-1, -2.5), -6)
        self.assertEqual(Point(0, 0) * Point(0, 0), 0)

    def test_cross(self):
        self.assertEqual(Point(1, 2).cross(Point(2, 3)), -1)
        self.assertEqual(Point(1, 2).cross(Point(-1, -2.5)), -0.5)
        self.assertEqual(Point(0, 0).cross(Point(0, 0)), 0)

    def test_length(self):
        self.assertEqual(Point(3, 4).length(), 5)
        self.assertAlmostEqual(Point(1, 1).length(), sqrt(2))
        self.assertEqual(Point(0, 0).length(), 0)

    def test_hash(self):
        self.assertEqual(hash(Point(1, 2)), hash(Point(1, 2)))
        self.assertEqual(hash(Point(1, 2)), hash(Point(1.0, 2.0)))
        self.assertEqual(hash(Point(0, 0)), hash(Point(-0, 0)))
        self.assertNotEqual(hash(Point(1, 2)), hash(Point(1, 3)))
        self.assertNotEqual(hash(Point(1, 2)), hash(Point(1.1, 2.0)))
        self.assertNotEqual(hash(Point(0, 0)), hash(Point(100, 0)))


if __name__ == "__main__":
    unittest.main()
