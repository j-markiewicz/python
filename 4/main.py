def make_ruler(n: int) -> str:
    """Make a ruler of the given length `n`

    >>> print(make_ruler(5))
    |....|....|....|....|....|
    0    1    2    3    4    5
    """

    increment = max(5, len(str(n)) + 1)
    tape = ("|" + "." * (increment - 1)) * n + "|"
    marks = "0" + "".join([f"{n:>{increment}}" for n in range(1, n + 1)])

    return f"{tape}\n{marks}"


def make_grid(rows: int, cols: int) -> str:
    """Make a grid of squares with the given number of rows and columns

    >>> print(make_grid(2, 4))
    +---+---+---+---+
    |   |   |   |   |
    +---+---+---+---+
    |   |   |   |   |
    +---+---+---+---+
    """

    horizontal = "+" + "---+" * cols
    vertical = "|" + "   |" * cols

    return f"\n{vertical}\n".join([horizontal] * (rows + 1))


def factorial(n: int) -> int:
    """Iteratively calculate the factorial of `n`

    >>> factorial(5)
    120
    """

    res = 1
    for i in range(n):
        res *= i + 1

    return res


def fibonacci(n: int) -> int:
    """Iteratively calculate the `n`th fibonacci number

    >>> fibonacci(6)
    8
    """

    a = 0
    b = 1

    for _ in range(n):
        a, b = b, a
        b += a

    return a


def odwracanie[T: list[any]](l: T, left: int, right: int) -> T:
    """Iteratively reverse the order of elements from `left` to `right` in `l`

    This function modifies `l` in place and returns a reference to it.

    >>> odwracanie([0, 1, 2, 3, 4, 5], 1, 3)
    [0, 3, 2, 1, 4, 5]
    """

    for i in range((right - left + 1) // 2):
        l[left + i], l[right - i] = l[right - i], l[left + i]

    return l


def odwracanie_rec[T: list[any]](l: T, left: int, right: int) -> T:
    """Recursively reverse the order of elements from `left` to `right` in `l`

    This function modifies `l` in place and returns a reference to it.

    >>> odwracanie_rec([0, 1, 2, 3, 4, 5], 1, 3)
    [0, 3, 2, 1, 4, 5]
    """

    if left >= right:
        return l

    l[left], l[right] = l[right], l[left]
    return odwracanie_rec(l, left + 1, right - 1)


def sum_seq[E: int | float, S: list[S | E] | tuple[S | E]](sequence: S) -> E:
    """Sum all elements in the arbitrarily nested `sequence`

    >>> sum_seq([[[1.0], 2, 3], (4, 5), [[[[[[6]]]]]]])
    21.0
    """

    return sum(flatten(sequence))


def flatten[E, S: list[S | E] | tuple[S | E]](seq: S) -> list[E]:
    """Flatten the elements from the arbitrarily nested sequence `seq`

    >>> flatten([([1.0], 2, "3"), (4, True), [[[[[[6]]]]]]])
    [1.0, 2, '3', 4, True, 6]
    """

    res = []

    for e in seq:
        if isinstance(e, list) or isinstance(e, tuple):
            res.extend(flatten(e))
        else:
            res.append(e)

    return res
