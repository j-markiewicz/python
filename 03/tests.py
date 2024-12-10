import unittest
import doctest

import main


class TestModule(unittest.TestCase):
    def test_pow_3(self):
        i = -1

        def mock_input(_: str) -> str:
            nonlocal i
            i += 1
            return ["1.0", "2", "2.5", "abc", "-5", "stop"][i]

        j = -1

        def mock_print(s: str):
            nonlocal j
            j += 1
            self.assertEqual(
                s,
                [
                    "1.0 1.0",
                    "2.0 8.0",
                    "2.5 15.625",
                    'input must be a number or "stop"',
                    "-5.0 -125.0",
                ][j],
            )

        main.pow_3(input=mock_input, print=mock_print)

    def test_measuring_tape(self):
        example_tape = """
|....|....|....|....|....|....|....|....|....|....|....|....|
0    1    2    3    4    5    6    7    8    9   10   11   12
        """.strip()

        self.assertEqual(main.measuring_tape(0), "|\n0")

        self.assertEqual(
            main.measuring_tape(1),
            "|....|\n0    1",
        )

        self.assertEqual(main.measuring_tape(12), example_tape)

        long_tape = main.measuring_tape(1000000)
        self.assertEqual(
            len(long_tape.splitlines()[0]), len(long_tape.splitlines()[1])
        )

    def test_rectangle(self):
        self.assertEqual(main.rectangle(0, 0), "+")
        self.assertEqual(main.rectangle(0, 1), "+---+")
        self.assertEqual(main.rectangle(1, 0), "+\n|\n+")
        self.assertEqual(main.rectangle(1, 1), "+---+\n|   |\n+---+")
        self.assertEqual(
            main.rectangle(5, 10),
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

    def test_combine_sequences(self):
        self.assertSequenceEqual(
            main.combine_sequences([1.0, 1.1, 1.2], [1.1])[0],
            [1.1],
        )

        self.assertSequenceEqual(
            main.combine_sequences([1.0, 1.1, 1.2], [1.1])[1],
            [1.0, 1.1, 1.2],
        )

        self.assertSequenceEqual(
            main.combine_sequences("", "abc")[0],
            "",
        )

        self.assertSequenceEqual(
            main.combine_sequences("", "abc")[1],
            "abc",
        )

    def test_sum_sequences(self):
        self.assertSequenceEqual(main.sum_sequences([]), [])

        self.assertSequenceEqual(
            main.sum_sequences([[], [1], [1, 1], [1.0], [1.0, 1.0], [1, 1.0]]),
            [0, 1, 2, 1.0, 2.0, 2.0],
        )

        self.assertSequenceEqual(
            list(
                map(
                    type,
                    main.sum_sequences(
                        [[], [1], [1, 1], [1.0], [1.0, 1.0], [1, 1.0]]
                    ),
                )
            ),
            [int, int, int, float, float, float],
        )

    def test_roman2int(self):
        self.assertEqual(main.roman2int(""), 0)
        self.assertEqual(main.roman2int("I"), 1)
        self.assertEqual(main.roman2int("IV"), 4)
        self.assertEqual(main.roman2int("MMMCMXCIX"), 3999)


if __name__ == "__main__":
    assert doctest.testmod(main).failed == 0
    unittest.main()
