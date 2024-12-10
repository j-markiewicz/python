from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie"""

    def __init__(self, x1, y1, x2, y2):
        """Create a new `Rectangle` from the coordinates of the bottom-left and
        top-right corners (x1 must be less than x2 and y1 must be less than y2)
        """

        if x1 >= x2:
            raise ValueError("x1 is not less than x2")

        if y1 >= y2:
            raise ValueError("y1 is not less than y2")

        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        """Return a user-friendly string representation of this rectangle"""

        return f"[{self.pt1}, {self.pt2}]"

    def __repr__(self):
        """Return a python-friendly string representation of this rectangle"""

        return (
            f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"
        )

    def __eq__(self, other):
        """Return whether `self` equals `other`"""

        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    def center(self):
        """Return the center of this rectangle"""

        return Point(
            (self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2
        )

    def area(self):
        """Return the area of this rectangle"""

        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):
        """Return a new rectangle equal to this rectangle moved by (x, y)"""

        return Rectangle(
            self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y
        )

    def intersection(self, other):
        """Return the intersection of `self` and `other`"""

        return Rectangle(
            max(self.pt1.x, other.pt1.x),
            max(self.pt1.y, other.pt1.y),
            min(self.pt2.x, other.pt2.x),
            min(self.pt2.y, other.pt2.y),
        )

    def cover(self, other):
        """Return the smallest rectangle that covers both `self` and `other`"""

        return Rectangle(
            min(self.pt1.x, other.pt1.x),
            min(self.pt1.y, other.pt1.y),
            max(self.pt2.x, other.pt2.x),
            max(self.pt2.y, other.pt2.y),
        )

    def make4(self):
        """Divide this rectangle into four equal-sized smaller rectangles"""

        width = self.pt2.x - self.pt1.x
        height = self.pt2.y - self.pt1.y

        return (
            Rectangle(
                self.pt1.x,
                self.pt1.y,
                self.pt2.x - width / 2,
                self.pt2.y - height / 2,
            ),
            Rectangle(
                self.pt1.x + width / 2,
                self.pt1.y,
                self.pt2.x,
                self.pt2.y - height / 2,
            ),
            Rectangle(
                self.pt1.x,
                self.pt1.y + height / 2,
                self.pt2.x - width / 2,
                self.pt2.y,
            ),
            Rectangle(
                self.pt1.x + width / 2,
                self.pt1.y + height / 2,
                self.pt2.x,
                self.pt2.y,
            ),
        )


import unittest


class TestRectangle(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Rectangle(1, 2, 3, 4)), "[(1, 2), (3, 4)]")
        self.assertEqual(
            str(Rectangle(1.2, 3.4, 5.6, 7.8)), "[(1.2, 3.4), (5.6, 7.8)]"
        )

    def test_repr(self):
        self.assertEqual(repr(Rectangle(1, 2, 3, 4)), "Rectangle(1, 2, 3, 4)")
        self.assertEqual(
            repr(Rectangle(1.2, 3.4, 5.6, 7.8)), "Rectangle(1.2, 3.4, 5.6, 7.8)"
        )

    def test_eq(self):
        self.assertEqual(
            Rectangle(1.2, 3.4, 5.6, 7.8), Rectangle(1.2, 3.4, 5.6, 7.8)
        )
        self.assertEqual(Rectangle(1, 2, 3, 4), Rectangle(1, 2, 3, 4))
        self.assertNotEqual(
            Rectangle(1, 2, 3, 4), Rectangle(1.2, 3.4, 5.6, 7.8)
        )
        self.assertNotEqual(
            Rectangle(1.2, 3.4, 5.6, 7.8), Rectangle(1, 2, 3, 4)
        )

    def test_center(self):
        self.assertEqual(Rectangle(1, 2, 3, 4).center(), Point(2, 3))
        self.assertAlmostEqual(Rectangle(1.2, 3.4, 5.6, 7.8).center().x, 3.4)
        self.assertAlmostEqual(Rectangle(1.2, 3.4, 5.6, 7.8).center().y, 5.6)
        self.assertEqual(Rectangle(-10, -5, 10, 5).center(), Point(0, 0))

    def test_area(self):
        self.assertEqual(Rectangle(1, 2, 3, 4).area(), 4)
        self.assertAlmostEqual(Rectangle(1.2, 3.4, 5.6, 7.8).area(), 19.36)
        self.assertEqual(Rectangle(-10, -5, 10, 5).area(), 200)

    def test_move(self):
        self.assertAlmostEqual(
            Rectangle(1.2, 3.4, 5.6, 7.8).move(1.1, -1.1).pt1.x,
            2.3,
        )
        self.assertAlmostEqual(
            Rectangle(1.2, 3.4, 5.6, 7.8).move(1.1, -1.1).pt1.y,
            2.3,
        )
        self.assertAlmostEqual(
            Rectangle(1.2, 3.4, 5.6, 7.8).move(1.1, -1.1).pt2.x,
            6.7,
        )
        self.assertAlmostEqual(
            Rectangle(1.2, 3.4, 5.6, 7.8).move(1.1, -1.1).pt2.y,
            6.7,
        )
        self.assertEqual(
            Rectangle(1, 2, 3, 4).move(-10, -10), Rectangle(-9, -8, -7, -6)
        )

    def test_intersection(self):
        self.assertEqual(
            Rectangle(0.2, 3.4, 5.6, 7.8).intersection(Rectangle(1, 2, 3, 4)),
            Rectangle(1, 2, 3, 4).intersection(Rectangle(0.2, 3.4, 5.6, 7.8)),
        )
        self.assertRaises(
            ValueError,
            lambda: Rectangle(1.2, 3.4, 5.6, 7.8).intersection(
                Rectangle(1, 2, 1.1, 2.2)
            ),
        )
        self.assertEqual(
            Rectangle(0, 1, 2, 3).intersection(Rectangle(1, 2, 3, 4)),
            Rectangle(1, 2, 2, 3),
        )

    def test_cover(self):
        self.assertEqual(
            Rectangle(0.2, 3.4, 5.6, 7.8).cover(Rectangle(1, 2, 3, 4)),
            Rectangle(1, 2, 3, 4).cover(Rectangle(0.2, 3.4, 5.6, 7.8)),
        )
        self.assertEqual(
            Rectangle(1.2, 3.4, 5.6, 7.8).cover(Rectangle(1, 2, 3, 4)),
            Rectangle(1, 2, 5.6, 7.8),
        )
        self.assertEqual(
            Rectangle(0, 1, 2, 3).cover(Rectangle(1, 2, 3, 4)),
            Rectangle(0, 1, 3, 4),
        )

    def test_make4(self):
        self.assertTupleEqual(
            Rectangle(-10, -5, 10, 5).make4(),
            (
                Rectangle(-10, -5, 0, 0),
                Rectangle(0, -5, 10, 0),
                Rectangle(-10, 0, 0, 5),
                Rectangle(0, 0, 10, 5),
            ),
        )
        self.assertTupleEqual(
            Rectangle(1, 2, 3, 4).make4(),
            (
                Rectangle(1, 2, 2, 3),
                Rectangle(2, 2, 3, 3),
                Rectangle(1, 3, 2, 4),
                Rectangle(2, 3, 3, 4),
            ),
        )


if __name__ == "__main__":
    unittest.main()
