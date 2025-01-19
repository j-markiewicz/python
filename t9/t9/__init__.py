from __future__ import annotations
from typing import Iterable, Sequence
from enum import Enum
import os

if __name__ == "t9":
    from t9.cached import Cached
else:
    from cached import Cached


class Language(Enum):
    """A supported language for T9"""

    EN = 0
    PL = 1

    def __str__(self):
        return self.name


class Character(Enum):
    """A T9 character, representing one of the T9 keyboard keys"""

    PUNCTUATION = 1
    ABC = 2
    DEF = 3
    GHI = 4
    JKL = 5
    MNO = 6
    PQRS = 7
    TUV = 8
    WXYZ = 9

    @staticmethod
    def from_char(char: str) -> Character | None:
        """Create a T9 `Character` from a corresponding character

        >>> Character.from_char('a')
        <Character.ABC: 2>
        """

        if char in ",.!?'-&1":
            return Character.PUNCTUATION
        elif char in "abcąć2":
            return Character.ABC
        elif char in "defę3":
            return Character.DEF
        elif char in "ghi4":
            return Character.GHI
        elif char in "jklł5":
            return Character.JKL
        elif char in "mnońó6":
            return Character.MNO
        elif char in "pqrsś7":
            return Character.PQRS
        elif char in "tuv8":
            return Character.TUV
        elif char in "wxyzżź90":
            return Character.WXYZ
        else:
            return None

    @staticmethod
    def from_input(input: str) -> Character:
        """Create a T9 `Character` from its corresponding input digit

        >>> Character.from_input("2")
        <Character.ABC: 2>
        """

        if input in "123456789":
            return Character(int(input))

        raise ValueError(f"{input} is not a valid T9 `Character`")

    def __str__(self):
        return self.name


class WordMap:
    """A map of words, implemented as a 9-ary trie"""

    next: dict[Character, None | WordMap]
    content: list[str]

    def __init__(self, **args) -> None:
        self.content = args.get("content", [])
        self.next = {
            Character.PUNCTUATION: args.get("punctuation", None),
            Character.ABC: args.get("abc", None),
            Character.DEF: args.get("def_", None),
            Character.GHI: args.get("ghi", None),
            Character.JKL: args.get("jkl", None),
            Character.MNO: args.get("mno", None),
            Character.PQRS: args.get("pqrs", None),
            Character.TUV: args.get("tuv", None),
            Character.WXYZ: args.get("wxyz", None),
        }

    @staticmethod
    def from_file(path: str) -> WordMap:
        """Create a new `WordMap` for the words in the file at `path`

        The file at `path` needs to be readable and is expected to be encoded
        in UTF-8.
        """

        with open(path, "r", encoding="utf-8") as file:
            return WordMap.new(map(str.strip, file.readlines()))

    @staticmethod
    def new(words: Iterable[str]) -> WordMap:
        """Create a new `WordMap` for the given words

        >>> WordMap.new(["one", "two"]).next[Character.MNO].content
        ['one']
        """

        res = WordMap()

        for word in words:
            chars = list(map(Character.from_char, word))

            if any(map(lambda c: c is None, chars)):
                continue

            res.content.append(word)
            current = res

            for char in chars:
                next = current.next[char]

                if next is None:
                    current.next[char] = WordMap()
                    next = current.next[char]

                current = next
                current.content.append(word)

        return res


_WORDMAPS = {
    Language.EN: Cached(
        lambda: WordMap.from_file(
            os.path.join(
                os.path.abspath(os.path.dirname(__file__)), "./words-en.txt"
            )
        )
    ),
    Language.PL: Cached(
        lambda: WordMap.from_file(
            os.path.join(
                os.path.abspath(os.path.dirname(__file__)), "./words-pl.txt"
            )
        )
    ),
}


def t9(
    input: Sequence[Character], lang_or_wordmap: Language | WordMap, n: int = 3
) -> tuple[str, ...]:
    """Return the top `n` (default 3) matching words for T9 input

    Calling this function for the first time for each language (for any
    `input`, including empty) will cause the dictionary to be initialized
    (which may be slow). Subsequent calls (with the same language) will be much
    faster.

    Alternatively, a `WordMap` may be passed instead of a language, in which
    case it will be used instead of the pre-defined ones.

    >>> t9([Character.GHI, Character.DEF, Character.JKL, Character.JKL], Language.EN)
    ('hell', 'hello', 'hellenic')

    >>> t9([Character.ABC], WordMap.new(["aa", "ab", "xy"]), 4)
    ('aa', 'ab', '', '')
    """

    if isinstance(lang_or_wordmap, Language):
        words = _WORDMAPS[lang_or_wordmap].get()
    else:
        words = lang_or_wordmap

    if len(input) == 0 or n <= 0:
        return ("",) * n

    for char in input:
        if words is None:
            break

        words = words.next[char]

    words = words.content if words is not None else []
    return tuple([*words, *([""] * n)][:n])


if __name__ == "__main__":
    import doctest

    doctest.testmod(report=True, raise_on_error=True)

    import unittest
    from tests import *

    unittest.main(verbosity=2)
