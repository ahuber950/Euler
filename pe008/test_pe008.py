import unittest
from pe008 import mod8


class Testpe008(unittest.TestCase):
    def test_pe008(self):
        self.assertEqual(mod8(4), 5832)
        self.assertEqual(mod8(13), 23514624000)
        self.assertEqual(mod8(1), 9)

    def test_values(self):
        self.assertRaises(ValueError, mod8, -1)
        self.assertRaises(ValueError, mod8, 0)

    def test_types(self):
        self.assertRaises(ValueError, mod8, "hi")
