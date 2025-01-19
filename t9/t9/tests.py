from __init__ import *
import unittest


class TestCached(unittest.TestCase):
    def test_cached(self):
        n = 0

        def init():
            nonlocal n
            n += 1

        cached = Cached(init)
        self.assertEqual(n, 0)
        cached.get()
        self.assertEqual(n, 1)
        cached.get()
        self.assertEqual(n, 1)


class TestWordMap(unittest.TestCase):
    def test_wordmap(self):
        words = WordMap.new(["b", "c", "a"])
        self.assertListEqual(words.content, ["b", "c", "a"])
        self.assertListEqual(words.next[Character.ABC].content, ["b", "c", "a"])
        self.assertIsNone(words.next[Character.DEF])

        words = WordMap.new(["aa", "dd", "gg", "jj"])
        self.assertListEqual(words.content, ["aa", "dd", "gg", "jj"])
        self.assertListEqual(words.next[Character.ABC].content, ["aa"])
        self.assertListEqual(
            words.next[Character.ABC].next[Character.ABC].content, ["aa"]
        )
        self.assertIsNone(
            words.next[Character.ABC].next[Character.ABC].next[Character.ABC]
        )
        self.assertListEqual(words.next[Character.DEF].content, ["dd"])
        self.assertListEqual(words.next[Character.GHI].content, ["gg"])
        self.assertListEqual(words.next[Character.JKL].content, ["jj"])
        self.assertIsNone(words.next[Character.MNO])


class TestT9(unittest.TestCase):
    def test_custom(self):
        self.assertTupleEqual(t9([], WordMap()), ("", "", ""))
        self.assertTupleEqual(t9([Character.ABC], WordMap()), ("", "", ""))
        self.assertTupleEqual(
            t9([Character.MNO], WordMap.new(["one", "two"])), ("one", "", "")
        )
        self.assertTupleEqual(
            t9([Character.ABC], WordMap.new(["a", "aaa", "aa"])),
            ("a", "aaa", "aa"),
        )
        self.assertTupleEqual(
            t9([Character.DEF], WordMap.new(["a", "aaa", "aa"])),
            ("", "", ""),
        )

    def test_nondefault_n(self):
        words = WordMap.new(["a", "aaa", "aa"])
        self.assertTupleEqual(
            t9([Character.ABC], words, 1),
            ("a",),
        )
        self.assertTupleEqual(
            t9([Character.ABC], words, 2),
            ("a", "aaa"),
        )
        self.assertTupleEqual(
            t9([Character.ABC], words, 3),
            ("a", "aaa", "aa"),
        )
        self.assertTupleEqual(
            t9([Character.ABC], words, 4),
            ("a", "aaa", "aa", ""),
        )
        self.assertTupleEqual(
            t9([Character.ABC], words, 5),
            ("a", "aaa", "aa", "", ""),
        )

    def test_pl(self):
        self.assertTupleEqual(t9([], Language.PL), ("", "", ""))
        self.assertTupleEqual(
            t9([Character.ABC], Language.PL), ("a", "był", "była")
        )
        self.assertTupleEqual(
            t9([Character.ABC] * 4, Language.PL), ("baba", "babcia", "abba")
        )
        self.assertTupleEqual(
            t9([Character.ABC] * 10, Language.PL), ("", "", "")
        )

    def test_en(self):
        self.assertTupleEqual(t9([], Language.EN), ("", "", ""))
        self.assertTupleEqual(
            t9([Character.ABC], Language.EN), ("and", "a", "as")
        )
        self.assertTupleEqual(
            t9([Character.ABC] * 4, Language.EN), ("baba", "abbas", "cabaret")
        )
        self.assertTupleEqual(
            t9([Character.ABC] * 10, Language.EN), ("", "", "")
        )
