from __future__ import annotations
from typing import Sequence
from enum import Enum
import os

from t9.cached import Cached
from t9.wordmap import WordMap, Character


class Language(Enum):
    """A supported language for T9"""

    EN = 0
    PL = 1

    def __str__(self):
        return self.name


def decode(
    input: Sequence[Character], lang_or_wordmap: Language | WordMap, n: int = 3
) -> tuple[str, ...]:
    """Return the top `n` (default 3) matching words for T9 input

    Calling this function for the first time for each language (for any
    `input`, including empty) will cause the dictionary to be initialized
    (which may be slow). Subsequent calls (with the same language) will be much
    faster.

    Alternatively, a `WordMap` may be passed instead of a language, in which
    case it will be used instead of the pre-defined ones.

    >>> decode([Character.GHI, Character.DEF, Character.JKL, Character.JKL], Language.EN)
    ('hell', 'hello', 'hellenic')

    >>> decode([Character.ABC], WordMap.new(["aa", "ab", "xy"]), 4)
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
