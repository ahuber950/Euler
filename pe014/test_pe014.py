import unittest
from pe014 import mod14


class Testpe014(unittest.TestCase):
    def test_pe014(self):
        self.assertEqual(mod14(10), 9)
        self.assertEqual(mod14(100), 97)
        self.assertEqual(mod14(1000000), 837799)

    def test_values(self):
        self.assertRaises(ValueError, mod14, -1)
        self.assertRaises(ValueError, mod14, 0)

    def test_types(self):
        self.assertRaises(ValueError, mod14, "hi")
