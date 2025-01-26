from t9 import WordMap, Character, Language, decode
import unittest


class TestT9(unittest.TestCase):
    def test_custom(self):
        self.assertTupleEqual(decode([], WordMap()), ("", "", ""))
        self.assertTupleEqual(decode([Character.ABC], WordMap()), ("", "", ""))
        self.assertTupleEqual(
            decode([Character.MNO], WordMap.new(["one", "two"])),
            ("one", "", ""),
        )
        self.assertTupleEqual(
            decode([Character.ABC], WordMap.new(["a", "aaa", "aa"])),
            ("a", "aaa", "aa"),
        )
        self.assertTupleEqual(
            decode([Character.DEF], WordMap.new(["a", "aaa", "aa"])),
            ("", "", ""),
        )

    def test_nondefault_n(self):
        words = WordMap.new(["a", "aaa", "aa"])
        self.assertTupleEqual(
            decode([Character.ABC], words, 1),
            ("a",),
        )
        self.assertTupleEqual(
            decode([Character.ABC], words, 2),
            ("a", "aaa"),
        )
        self.assertTupleEqual(
            decode([Character.ABC], words, 3),
            ("a", "aaa", "aa"),
        )
        self.assertTupleEqual(
            decode([Character.ABC], words, 4),
            ("a", "aaa", "aa", ""),
        )
        self.assertTupleEqual(
            decode([Character.ABC], words, 5),
            ("a", "aaa", "aa", "", ""),
        )

    def test_pl(self):
        self.assertTupleEqual(decode([], Language.PL), ("", "", ""))
        self.assertTupleEqual(
            decode([Character.ABC], Language.PL), ("a", "był", "była")
        )
        self.assertTupleEqual(
            decode([Character.ABC] * 4, Language.PL), ("baba", "babcia", "abba")
        )
        self.assertTupleEqual(
            decode([Character.ABC] * 10, Language.PL), ("", "", "")
        )

    def test_en(self):
        self.assertTupleEqual(decode([], Language.EN), ("", "", ""))
        self.assertTupleEqual(
            decode([Character.ABC], Language.EN), ("and", "a", "as")
        )
        self.assertTupleEqual(
            decode([Character.ABC] * 4, Language.EN),
            ("baba", "abbas", "cabaret"),
        )
        self.assertTupleEqual(
            decode([Character.ABC] * 10, Language.EN), ("", "", "")
        )
