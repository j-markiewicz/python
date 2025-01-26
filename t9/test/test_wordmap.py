from t9 import WordMap, Character
import unittest


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
