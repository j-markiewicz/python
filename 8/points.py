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
