import unittest
from pe013 import mod13


class Testpe013(unittest.TestCase):
    def test_pe013(self):
        self.assertEqual(mod13("values.txt"), "5537376230")

    def test_values(self):
        self.assertRaises(ValueError, mod13, -1)
        self.assertRaises(ValueError, mod13, 0)

    def test_types(self):
        self.assertRaises(ValueError, mod13, "hi")
