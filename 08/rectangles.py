from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie"""

    @property
    def top(self):
        """The coordinate of the top edge of this rectangle"""

        return self.pt2.y

    @property
    def left(self):
        """The coordinate of the left edge of this rectangle"""

        return self.pt1.x

    @property
    def bottom(self):
        """The coordinate of the bottom edge of this rectangle"""

        return self.pt1.y

    @property
    def right(self):
        """The coordinate of the right edge of this rectangle"""

        return self.pt2.x

    @property
    def width(self):
        """The width of this rectangle"""

        return self.pt2.x - self.pt1.x

    @property
    def height(self):
        """The height of this rectangle"""

        return self.pt2.y - self.pt1.y

    @property
    def topleft(self):
        """The top-left corner of this rectangle"""

        return Point(self.pt1.x, self.pt2.y)

    @property
    def bottomleft(self):
        """The bottom-left corner of this rectangle"""

        return self.pt1

    @property
    def topright(self):
        """The top-right corner of this rectangle"""

        return self.pt2

    @property
    def bottomright(self):
        """The bottom-right corner of this rectangle"""

        return Point(self.pt2.x, self.pt1.y)

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

    @staticmethod
    def from_points(points):
        """Create a new `Rectangle` from the points given as a list or tuple in
        the form `(bottom_left, top_right)`"""

        return Rectangle(points[0].x, points[0].y, points[1].x, points[1].y)

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
