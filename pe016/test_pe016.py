import unittest
from pe016 import mod16


class Testpe015(unittest.TestCase):
    def test_pe015(self):
        self.assertEqual(mod16(2), 4)
        self.assertEqual(mod16(10), 7)
        self.assertEqual(mod16(1000), 1366)

    def test_values(self):
        self.assertRaises(ValueError, mod16, -1)
        self.assertRaises(ValueError, mod16, -5)

    def test_types(self):
        self.assertRaises(ValueError, mod16, "hi")
