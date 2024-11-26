import pytest
from points import Point
from rectangles import Rectangle


EPSILON = 0.000001


def test_properties():
    assert Rectangle(1, 2, 3, 4).top == 4
    assert Rectangle(1, 2, 3, 4).right == 3
    assert Rectangle(1, 2, 3, 4).bottom == 2
    assert Rectangle(1, 2, 3, 4).left == 1
    assert Rectangle(1, 2, 3, 4).width == 2
    assert Rectangle(1, 2, 3, 4).height == 2
    assert Rectangle(1, 2, 3, 4).topleft == Point(1, 4)
    assert Rectangle(1, 2, 3, 4).bottomleft == Point(1, 2)
    assert Rectangle(1, 2, 3, 4).topright == Point(3, 4)
    assert Rectangle(1, 2, 3, 4).bottomright == Point(3, 2)

    assert abs(Rectangle(1.2, 3.4, 5.6, 7.8).top - 7.8) < EPSILON
    assert abs(Rectangle(1.2, 3.4, 5.6, 7.8).right - 5.6) < EPSILON
    assert abs(Rectangle(1.2, 3.4, 5.6, 7.8).bottom - 3.4) < EPSILON
    assert abs(Rectangle(1.2, 3.4, 5.6, 7.8).left - 1.2) < EPSILON
    assert abs(Rectangle(1.2, 3.4, 5.6, 8.9).width - 4.4) < EPSILON
    assert abs(Rectangle(1.2, 3.4, 5.6, 8.9).height - 5.5) < EPSILON
    assert Rectangle(1.2, 3.4, 5.6, 7.8).topleft == Point(1.2, 7.8)
    assert Rectangle(1.2, 3.4, 5.6, 7.8).bottomleft == Point(1.2, 3.4)
    assert Rectangle(1.2, 3.4, 5.6, 7.8).topright == Point(5.6, 7.8)
    assert Rectangle(1.2, 3.4, 5.6, 7.8).bottomright == Point(5.6, 3.4)


def test_from_points():
    assert Rectangle.from_points(
        (Point(1.2, 3.4), Point(5.6, 7.8))
    ) == Rectangle(1.2, 3.4, 5.6, 7.8)
    assert Rectangle.from_points((Point(1, 2), Point(3, 4))) == Rectangle(
        1, 2, 3, 4
    )
    assert Rectangle.from_points(
        [Point(1.2, 3.4), Point(5.6, 7.8)]
    ) == Rectangle(1.2, 3.4, 5.6, 7.8)
    assert Rectangle.from_points([Point(1, 2), Point(3, 4)]) == Rectangle(
        1, 2, 3, 4
    )


def test_str():
    assert str(Rectangle(1, 2, 3, 4)) == "[(1, 2), (3, 4)]"
    assert str(Rectangle(1.2, 3.4, 5.6, 7.8)) == "[(1.2, 3.4), (5.6, 7.8)]"


def test_repr():
    assert repr(Rectangle(1, 2, 3, 4)) == "Rectangle(1, 2, 3, 4)"
    assert (
        repr(Rectangle(1.2, 3.4, 5.6, 7.8)) == "Rectangle(1.2, 3.4, 5.6, 7.8)"
    )


def test_eq():
    assert Rectangle(1.2, 3.4, 5.6, 7.8) == Rectangle(1.2, 3.4, 5.6, 7.8)
    assert Rectangle(1, 2, 3, 4) == Rectangle(1, 2, 3, 4)
    assert Rectangle(1, 2, 3, 4) != Rectangle(1.2, 3.4, 5.6, 7.8)
    assert Rectangle(1.2, 3.4, 5.6, 7.8) != Rectangle(1, 2, 3, 4)


def test_center():
    assert Rectangle(1, 2, 3, 4).center() == Point(2, 3)
    assert abs(Rectangle(1.2, 3.4, 5.6, 7.8).center().x - 3.4) < EPSILON
    assert abs(Rectangle(1.2, 3.4, 5.6, 7.8).center().y - 5.6) < EPSILON
    assert Rectangle(-10, -5, 10, 5).center() == Point(0, 0)


def test_area():
    assert Rectangle(1, 2, 3, 4).area() == 4
    assert abs(Rectangle(1.2, 3.4, 5.6, 7.8).area() - 19.36) < EPSILON
    assert Rectangle(-10, -5, 10, 5).area() == 200


def test_move():
    assert (
        abs(Rectangle(1.2, 3.4, 5.6, 7.8).move(1.1, -1.1).pt1.x - 2.3) < EPSILON
    )
    assert (
        abs(Rectangle(1.2, 3.4, 5.6, 7.8).move(1.1, -1.1).pt1.y - 2.3) < EPSILON
    )
    assert (
        abs(Rectangle(1.2, 3.4, 5.6, 7.8).move(1.1, -1.1).pt2.x - 6.7) < EPSILON
    )
    assert (
        abs(Rectangle(1.2, 3.4, 5.6, 7.8).move(1.1, -1.1).pt2.y - 6.7) < EPSILON
    )
    assert Rectangle(1, 2, 3, 4).move(-10, -10) == Rectangle(-9, -8, -7, -6)


def test_intersection():
    assert Rectangle(0.2, 3.4, 5.6, 7.8).intersection(
        Rectangle(1, 2, 3, 4)
    ) == Rectangle(1, 2, 3, 4).intersection(Rectangle(0.2, 3.4, 5.6, 7.8))

    with pytest.raises(ValueError):
        Rectangle(1.2, 3.4, 5.6, 7.8).intersection(Rectangle(1, 2, 1.1, 2.2))

    assert Rectangle(0, 1, 2, 3).intersection(
        Rectangle(1, 2, 3, 4)
    ) == Rectangle(1, 2, 2, 3)


def test_cover():
    assert Rectangle(0.2, 3.4, 5.6, 7.8).cover(
        Rectangle(1, 2, 3, 4)
    ) == Rectangle(1, 2, 3, 4).cover(Rectangle(0.2, 3.4, 5.6, 7.8))
    assert Rectangle(1.2, 3.4, 5.6, 7.8).cover(
        Rectangle(1, 2, 3, 4)
    ) == Rectangle(1, 2, 5.6, 7.8)
    assert Rectangle(0, 1, 2, 3).cover(Rectangle(1, 2, 3, 4)) == Rectangle(
        0, 1, 3, 4
    )


def test_make4():
    assert Rectangle(-10, -5, 10, 5).make4() == (
        Rectangle(-10, -5, 0, 0),
        Rectangle(0, -5, 10, 0),
        Rectangle(-10, 0, 0, 5),
        Rectangle(0, 0, 10, 5),
    )
    assert Rectangle(1, 2, 3, 4).make4() == (
        Rectangle(1, 2, 2, 3),
        Rectangle(2, 2, 3, 3),
        Rectangle(1, 3, 2, 4),
        Rectangle(2, 3, 3, 4),
    )
