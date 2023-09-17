import unittest
from pe006 import mod6


class Testpe006(unittest.TestCase):
    def test_pe006(self):
        self.assertEqual(mod6(10), 2640)
        self.assertEqual(mod6(100), 25164150)

    def test_values(self):
        self.assertRaises(ValueError, mod6, -1)
        self.assertRaises(ValueError, mod6, 0)

    def test_types(self):
        self.assertRaises(ValueError, mod6, "hi")
