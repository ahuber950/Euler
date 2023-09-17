import unittest
from pe007 import mod7


class Testpe007(unittest.TestCase):
    def test_pe007(self):
        self.assertEqual(mod7(6), 13)
        self.assertEqual(mod7(10001), 104743)
        self.assertEqual(mod7(1), 2)

    def test_values(self):
        self.assertRaises(ValueError, mod7, -1)
        self.assertRaises(ValueError, mod7, 0)

    def test_types(self):
        self.assertRaises(ValueError, mod7, "hi")
