import unittest
from pe005 import mod5


class Testpe005(unittest.TestCase):
    def test_pe005(self):
        self.assertEqual(mod5(1), 1)
        self.assertEqual(mod5(10), 2520)
        self.assertEqual(mod5(20), 232792560)

    def test_values(self):
        self.assertRaises(ValueError, mod5, -1)
        self.assertRaises(ValueError, mod5, 0)

    def test_types(self):
        self.assertRaises(ValueError, mod5, "hi")
