import unittest
import doctest

import t9
import t9.cached
import t9.t9
import t9.wordmap


class TestDocs(unittest.TestCase):
    def test_docs(self):
        self.assertEqual(doctest.testmod(t9).failed, 0)
        self.assertEqual(doctest.testmod(t9.cached).failed, 0)
        self.assertEqual(doctest.testmod(t9.t9).failed, 0)
        self.assertEqual(doctest.testmod(t9.wordmap).failed, 0)
