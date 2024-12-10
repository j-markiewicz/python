from points import Point
from math import sqrt


EPSILON = 0.000001


def test_str():
    assert str(Point(2.0, 3.0)) == "(2.0, 3.0)"
    assert str(Point(-2, -7)) == "(-2, -7)"


def test_repr():
    assert repr(Point(2.0, 3.0)) == "Point(2.0, 3.0)"
    assert repr(Point(-2, -7)) == "Point(-2, -7)"


def test_eq():
    assert Point(1, 2) == Point(1, 2)
    assert Point(1, 2) == Point(1.0, 2.0)
    assert Point(0, 0) == Point(-0, 0)
    assert Point(1, 2) != Point(1, 3)
    assert Point(1, 2) != Point(1.1, 2.0)
    assert Point(0, 0) != Point(100, 0)


def test_add():
    assert Point(1, 2) + Point(2, 3) == Point(3, 5)
    assert Point(1, 2) + Point(-1, -2.5) == Point(0, -0.5)
    assert Point(0, 0) + Point(0, 0) == Point(0, 0)


def test_sub():
    assert Point(1, 2) - Point(2, 3) == Point(-1, -1)
    assert Point(1, 2) - Point(-1, -2.5) == Point(2, 4.5)
    assert Point(0, 0) - Point(0, 0) == Point(0, 0)


def test_mul():
    assert Point(1, 2) * Point(2, 3) == 8
    assert Point(1, 2) * Point(-1, -2.5) == -6
    assert Point(0, 0) * Point(0, 0) == 0


def test_cross():
    assert Point(1, 2).cross(Point(2, 3)) == -1
    assert Point(1, 2).cross(Point(-1, -2.5)) == -0.5
    assert Point(0, 0).cross(Point(0, 0)) == 0


def test_length():
    assert Point(3, 4).length() == 5
    assert abs(Point(1, 1).length() - sqrt(2)) < EPSILON
    assert Point(0, 0).length() == 0


def test_hash():
    assert hash(Point(1, 2)) == hash(Point(1, 2))
    assert hash(Point(1, 2)) == hash(Point(1.0, 2.0))
    assert hash(Point(0, 0)) == hash(Point(-0, 0))
    assert hash(Point(1, 2)) != hash(Point(1, 3))
    assert hash(Point(1, 2)) != hash(Point(1.1, 2.0))
    assert hash(Point(0, 0)) != hash(Point(100, 0))
