def count_words(line: str) -> int:
    """Count the number of words in the given string

    A word is any sequence of non-whitespace characters separated from other
    words by whitespace.

    >>> count_words("Hello, World!")
    2

    >>> count_words(\"""The quick
    ... brown fox
    ... jumps     over
    ... the lazy
    ...
    ... \tdog.
    ... \""")
    9
    """

    return len(line.split())


def print_with_underscores(word: str, printer=print):
    """Print the string `word` with each character separated by an underscore

    To print the resuling string, the given function `printer` is used (by
    default the builtin `print()`)

    >>> print_with_underscores("test")
    t_e_s_t

    >>> print_with_underscores("Hello, World!")
    H_e_l_l_o_,_ _W_o_r_l_d_!

    >>> print_with_underscores("test", printer=lambda s: print(f"custom {s}"))
    custom t_e_s_t
    """

    printer("_".join(word[::]))


def first_chars(line: str) -> str:
    """Return a string made up of the first characters of the words in `line`

    A word is any sequence of non-whitespace characters separated from other
    words by one or more whitespace characters.

    >>> first_chars("Hello, World!")
    'HW'

    >>> first_chars("   abc \t def \\n ghi\\njkl")
    'adgj'
    """

    return "".join([word[0] for word in line.split()])


def last_chars(line: str) -> str:
    """Return a string made up of the last characters of the words in `line`

    A word is any sequence of non-whitespace characters separated from other
    words by one or more whitespace characters.

    >>> last_chars("Hello, World!")
    ',!'

    >>> last_chars("   abc \t def \\n ghi\\njkl")
    'cfil'
    """

    return "".join([word[-1] for word in line.split()])


def word_lengths(line: str) -> int:
    """Count the total length of the words in the given string `line`

    A word is any sequence of non-whitespace characters separated from other
    words by one or more whitespace characters.

    >>> word_lengths("Hello, World!")
    12

    >>> word_lengths("   abc \t def \\n ghi\\njkl")
    12
    """

    return sum([len(word) for word in line.split()])


def longest_word(line: str) -> tuple[str, int]:
    """Find the longest word and its length in the given string `line`

    A word is any sequence of non-whitespace characters separated from other
    words by one or more whitespace characters.

    If multiple words tie for longest, the first one is returned.

    >>> longest_word("Hello, World!")
    ('Hello,', 6)

    >>> longest_word("   abcde \t fghi \\n jkl")
    ('abcde', 5)
    """

    try:
        word = max(line.split(), key=len)
    except ValueError:
        word = ""
    return word, len(word)


def digit_string(l: list[int]) -> str:
    """Return a string containing all digits from the input list `l`

    `l` is assumed to contain only nonnegative integers.

    >>> digit_string([1, 2, 3, 4, 5])
    '12345'

    >>> digit_string([123, 456, 789])
    '123456789'
    """

    return "".join(map(str, l))


def expand_string(line: str) -> str:
    """Expand all occurences of "GvR" in `line` into "Guido van Rossum"

    >>> expand_string("Hello, World!")
    'Hello, World!'

    >>> expand_string("Hello, GvR!")
    'Hello, Guido van Rossum!'
    """

    return line.replace("GvR", "Guido van Rossum")


def sort_string(line: str) -> tuple[str, str]:
    """Sort the words in given string `line` alphabetically and from shortest
    to longest

    Equally-long words retain their relative positions. Words are returned
    separated by spaces, original whitespace is not retained.

    >>> sort_string("Hello, World!")
    ('Hello, World!', 'Hello, World!')

    >>> sort_string("abcdef ghi jklmno pqrs tuvw xyz")
    ('abcdef ghi jklmno pqrs tuvw xyz', 'ghi xyz pqrs tuvw abcdef jklmno')
    """

    return (
        " ".join(sorted(line.split())),
        " ".join(sorted(line.split(), key=len)),
    )


def count_zeroes(number: int) -> int:
    """Count the number of 0-digits in the decimal representation of the given
    integer `number`

    Leading zeroes are not counted.

    >>> count_zeroes(1020304050)
    5

    >>> count_zeroes(123456789012345678901234567890)
    3
    """

    return str(number).count("0")


def pad_numbers(l: list[int]) -> list[str]:
    """Zero-pad the integers in the given list `l` to 3 characters

    `l` is assumed to contain only nonnegative integers.

    >>> pad_numbers([1, 22, 333])
    ['001', '022', '333']
    """

    return [str(n).zfill(3) for n in l]


if __name__ == "__main__":
    import doctest
    from sys import argv

    verbose = "-v" in argv or "--verbose" in argv
    section_end = "\n\n" if verbose else "\n"

    assert doctest.testmod(verbose=verbose).failed == 0

    print("Doctests passed", end=section_end)

    # Test `count_words`
    word_counts = [
        ("", 0),
        (" ", 0),
        (" \t \n\n\t   \t", 0),
        ("a b c d e", 5),
        ("  a   b   c   d   e  ", 5),
        (".a.b.c.d.e.", 1),
        (
            """
            a
            b
            c

            d
            e
            """,
            5,
        ),
    ]

    for word, count in word_counts:
        assert count_words(word) == count

        if verbose:
            print(f'✓ count_words("{word}") == {count}')

    print("count_words tests passed", end=section_end)

    # Test `print_with_underscores`
    underscored = [
        ("hello", "h_e_l_l_o"),
        ("   hello   ", " _ _ _h_e_l_l_o_ _ _ "),
        ("", ""),
        ("a", "a"),
        ("ab", "a_b"),
        (
            """multi
line

""",
            """m_u_l_t_i_
_l_i_n_e_
_
""",
        ),
    ]

    for before, after in underscored:
        res = None

        def printer(s):
            global res
            res = s

        print_with_underscores(before, printer=printer)
        assert res == after

        if verbose:
            print(f'✓ print_with_underscores("{before}") -> "{after}"')

    print("print_with_underscores tests passed", end=section_end)

    # Test `first_chars`
    first_last_chars = [
        ("hello", "h", "o"),
        ("   hello   ", "h", "o"),
        ("", "", ""),
        ("a", "a", "a"),
        ("a b", "ab", "ab"),
        ("this is a test", "tiat", "ssat"),
        (
            """multi
line

""",
            "ml",
            "ie",
        ),
    ]

    for line, first, _ in first_last_chars:
        assert first_chars(line) == first

        if verbose:
            print(f'✓ first_chars("{line}") == "{first}"')

    print("first_chars tests passed", end=section_end)

    # Test `last_chars`
    for line, _, last in first_last_chars:
        assert last_chars(line) == last

        if verbose:
            print(f'✓ last_chars("{line}") == "{last}"')

    print("last_chars tests passed", end=section_end)

    # Test `word_lengths`
    lengths = [
        ("hello", 5),
        ("   hello   ", 5),
        ("", 0),
        ("a", 1),
        ("a b", 2),
        ("this is a test", 11),
        (
            """multi
line

""",
            9,
        ),
    ]

    for line, length in lengths:
        assert word_lengths(line) == length

        if verbose:
            print(f'✓ word_lengths("{line}") == {length}')

    print("word_lengths tests passed", end=section_end)

    # Test `longest_word`
    longest = [
        ("hello", "hello", 5),
        ("   hello   ", "hello", 5),
        ("", "", 0),
        ("a", "a", 1),
        ("a b", "a", 1),
        ("this is a test", "this", 4),
        (
            """multi
line

""",
            "multi",
            5,
        ),
    ]

    for line, word, length in longest:
        assert longest_word(line) == (word, length)

        if verbose:
            print(f'✓ longest_word("{line}") == "{word}", {length}')

    print("longest_word tests passed", end=section_end)

    # Test `digit_string`
    numbers = [
        ([], ""),
        ([000, 00, 0], "000"),
        ([0x12, 34], "1834"),
    ]

    for l, res in numbers:
        assert digit_string(l) == res

        if verbose:
            print(f'✓ digit_string({l}) == "{res}"')

    print("digit_string tests passed", end=section_end)

    # Test `expand_string`
    gvr = [
        ("test", "test"),
        ("gvr GVR GvR   GvR", "gvr GVR Guido van Rossum   Guido van Rossum"),
    ]

    for gvr, guido in gvr:
        assert expand_string(gvr) == guido

        if verbose:
            print(f'✓ expand_string("{gvr}") == "{guido}"')

    print("expand_string tests passed", end=section_end)

    # Test `sort_string`
    strings = [
        ("test", "test", "test"),
        ("", "", ""),
        ("a b c", "a b c", "a b c"),
        ("bb c aaa", "aaa bb c", "c bb aaa"),
        (
            """bb
                        c
         
         aaa""",
            "aaa bb c",
            "c bb aaa",
        ),
    ]

    for unsorted, alpha, length in strings:
        assert sort_string(unsorted) == (alpha, length)

        if verbose:
            print(f'✓ sort_string("{unsorted}") == "{alpha}", "{length}"')

    print("sort_string tests passed", end=section_end)

    # Test `count_zeroes`
    zeroes = [
        (0, 1),
        (123, 0),
        (-1230456, 1),
        (10**100, 100),
    ]

    for num, zeroes in zeroes:
        assert count_zeroes(num) == zeroes

        if verbose:
            print(f"✓ count_zeroes({num}) == {zeroes}")

    print("count_zeroes tests passed", end=section_end)

    # Test `pad_numbers`
    number_strings = [
        ([], []),
        ([0, 1, 2], ["000", "001", "002"]),
        ([0], ["000"]),
        ([0xA], ["010"]),
    ]

    for unpadded, padded in number_strings:
        assert pad_numbers(unpadded) == padded

        if verbose:
            print(f"✓ pad_numbers({unpadded}) == {padded}")

    print("pad_numbers tests passed", end=section_end)

    print("All tests passed")
