from typing import Sequence


def print_numbers():
    """Print the numbers 0 - 30, except numbers divisible by 3

    >>> print_numbers()
    1 2 4 5 7 8 10 11 13 14 16 17 19 20 22 23 25 26 28 29
    """

    print(" ".join([str(n) for n in range(30) if n % 3 != 0]))


def pow_3(input=input, print=print):
    """Read numbers from stdin and print their 3rd powers until "stop" is typed

    Stdin input is retrieved using `input` (by default the builtin `input`),
    stdout printing is done using `print` (by default the builtin `print`).
    """

    while True:
        line = input("> ")

        if line == "stop":
            break

        try:
            num = float(line)
            print(f"{num} {num**3}")
        except ValueError:
            print('input must be a number or "stop"')


def measuring_tape(length: int) -> str:
    """Make a measuring tape of the given length

    >>> print(measuring_tape(5))
    |....|....|....|....|....|
    0    1    2    3    4    5
    """

    increment = max(5, len(str(length)) + 1)
    tape = ("|" + "." * (increment - 1)) * length + "|"
    marks = "0" + "".join([f"{n:>{increment}}" for n in range(1, length + 1)])

    return f"{tape}\n{marks}"


def rectangle(height: int, width: int) -> str:
    """Make a rectangle made out of squares with the given width and height

    >>> print(rectangle(2, 4))
    +---+---+---+---+
    |   |   |   |   |
    +---+---+---+---+
    |   |   |   |   |
    +---+---+---+---+
    """

    horizontal = "+" + "---+" * width
    vertical = "|" + "   |" * width

    return f"\n{vertical}\n".join([horizontal] * (height + 1))


def combine_sequences[
    T: Sequence[int] | Sequence[float] | str
](a: T, b: T) -> tuple[T, T]:
    """Combine two strings or lists of numbers into their intersection and sum

    >>> combine_sequences([1, 2, 3], [2, 3, 4])
    ([2, 3], [1, 2, 3, 4])

    >>> combine_sequences("abcde", "defg")
    ('de', 'adbecfg')
    """

    intersection = list(set(a).intersection(set(b)))
    union = list(set(a).union(set(b)))

    def find_key(x, a: list, b: list):
        try:
            ia = a.index(x)
        except ValueError:
            ia = None

        try:
            ib = b.index(x)
        except ValueError:
            ib = None

        if ia != None and ib == None:
            return ia * 2
        elif ib != None and ia == None:
            return ib * 2 + 1
        else:
            return min(ia * 2, ib * 2 + 1)

    intersection.sort(key=lambda x: find_key(x, list(a), list(b)))
    union.sort(key=lambda x: find_key(x, list(a), list(b)))

    if type(a) == str:
        return ("".join(intersection), "".join(union))
    else:
        return (intersection, union)


def sum_sequences(seqs: list[Sequence[int | float]]) -> list[int | float]:
    """Sum all elements in each of the provided sequences of numbers

    >>> sum_sequences([[], [4], (1, 2), [3, 4], (5, 6, 7)])
    [0, 4, 3, 7, 18]
    """

    return list(map(lambda seq: sum(list(seq)), seqs))


def roman2int(num: str) -> int:
    """Convert the given roman numeral to an int

    >>> roman2int("MMXXIV")
    2024
    """

    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    # or

    values = {
        n: values.get(n)
        for n in [
            "I",
            "V",
            "X",
            "L",
            "C",
            "D",
            "M",
        ]
    }

    # or

    values = {
        n: val + 1
        for n, val in [
            ("I", 0),
            ("V", 4),
            ("X", 9),
            ("L", 49),
            ("C", 99),
            ("D", 499),
            ("M", 999),
        ]
    }

    # or

    values = dict(
        [
            ("I", 1),
            ("V", 5),
            ("X", 10),
            ("L", 50),
            ("C", 100),
            ("D", 500),
            ("M", 1000),
        ]
    )

    # or

    values = dict(
        I=1,
        V=5,
        X=10,
        L=50,
        C=100,
        D=500,
        M=1000,
    )

    # or

    values = dict(
        zip(
            [
                "I",
                "V",
                "X",
                "L",
                "C",
                "D",
                "M",
            ],
            [1, 5, 10, 50, 100, 500, 1000],
        )
    )

    # or

    import json

    values = json.loads(
        """{
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }"""
    )

    # etc.

    res = 0
    last = 10000
    for l in num:
        val = values[l]

        if last < val:
            res += val - 2 * last
        else:
            res += val
        last = val

    return res
