from t9.cached import Cached
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
