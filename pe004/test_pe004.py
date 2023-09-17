import unittest
from pe004 import mod4


class Testpe004(unittest.TestCase):
    def test_pe004(self):
        self.assertEqual(mod4(1), 9)
        self.assertEqual(mod4(2), 9009)
        self.assertEqual(mod4(3), 906609)

    def test_values(self):
        self.assertRaises(ValueError, mod4, -1)
        self.assertRaises(ValueError, mod4, 0)

    def test_types(self):
        self.assertRaises(ValueError, mod4, "hi")
