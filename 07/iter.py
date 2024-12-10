from random import choice


def zero_one():
    """Iterate over the infinite sequence 0, 1, 0, 1, 0, 1, ..."""

    yield_one = False

    while True:
        yield int(yield_one)
        yield_one = not yield_one


def directions():
    """Infinitely iterate over the values "N", "E", "S", "W" in random order"""

    while True:
        yield choice("NESW")


def weekdays():
    """Iterate over weekday indices (0, 1, 2, 3, 4, 5, 6, 0, ...) infinitely"""

    value = 0
    while True:
        yield value
        value += 1
        value %= 7


import unittest


class TestFrac(unittest.TestCase):
    def test_zero_one(self):
        iter = zero_one()
        for _ in range(100):
            self.assertEqual(next(iter), 0)
            self.assertEqual(next(iter), 1)

    def test_directions(self):
        iter = directions()
        for _ in range(100):
            self.assertIn(next(iter), ["N", "E", "S", "W"])

    def test_weekdays(self):
        iter = weekdays()
        for _ in range(100):
            self.assertEqual(next(iter), 0)
            self.assertEqual(next(iter), 1)
            self.assertEqual(next(iter), 2)
            self.assertEqual(next(iter), 3)
            self.assertEqual(next(iter), 4)
            self.assertEqual(next(iter), 5)
            self.assertEqual(next(iter), 6)


if __name__ == "__main__":
    unittest.main()
