import unittest
import doctest

import main


class TestModule(unittest.TestCase):
    def test_make_ruler(self):
        example_tape = """
|....|....|....|....|....|....|....|....|....|....|....|....|
0    1    2    3    4    5    6    7    8    9   10   11   12
        """.strip()

        self.assertEqual(main.make_ruler(0), "|\n0")

        self.assertEqual(
            main.make_ruler(1),
            "|....|\n0    1",
        )

        self.assertEqual(main.make_ruler(12), example_tape)

        long_tape = main.make_ruler(1000000)
        self.assertEqual(
            len(long_tape.splitlines()[0]), len(long_tape.splitlines()[1])
        )

    def test_make_grid(self):
        self.assertEqual(main.make_grid(0, 0), "+")
        self.assertEqual(main.make_grid(0, 1), "+---+")
        self.assertEqual(main.make_grid(1, 0), "+\n|\n+")
        self.assertEqual(main.make_grid(1, 1), "+---+\n|   |\n+---+")
        self.assertEqual(
            main.make_grid(5, 10),
            """
+---+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+---+---+
            """.strip(),
        )

    def test_factorial(self):
        self.assertEqual(main.factorial(0), 1)
        self.assertEqual(main.factorial(1), 1)
        self.assertEqual(main.factorial(2), 2)
        self.assertEqual(main.factorial(3), 6)
        self.assertEqual(main.factorial(4), 24)
        self.assertEqual(
            main.factorial(10), 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
        )
        self.assertEqual(
            main.factorial(100),
            93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000,
        )

    def test_fibonacci(self):
        self.assertListEqual(
            [main.fibonacci(n) for n in range(12)],
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
        )

    def test_odwracanie(self):
        l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        copy = l.copy()
        for odw in [main.odwracanie, main.odwracanie_rec]:
            self.assertListEqual(odw(l, 0, 9), list(reversed(copy)))
            self.assertIs(odw(l, 0, 9), l)
            self.assertListEqual(l, copy)
            self.assertListEqual(odw(l, 0, 4), [4, 3, 2, 1, 0, 5, 6, 7, 8, 9])
            self.assertListEqual(odw(l, 5, 9), [4, 3, 2, 1, 0, 9, 8, 7, 6, 5])
            self.assertIs(odw(l, 0, 4), l)
            self.assertIs(odw(l, 5, 9), l)
            self.assertListEqual(l, copy)


if __name__ == "__main__":
    assert doctest.testmod(main).failed == 0
    unittest.main()
