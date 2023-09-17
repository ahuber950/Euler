import unittest
from pe012 import mod12


class Testpe012(unittest.TestCase):
    def test_pe012(self):
        self.assertEqual(mod12(5), 28)
        self.assertEqual(mod12(500), 76576500)

    def test_values(self):
        self.assertRaises(ValueError, mod12, -1)
        self.assertRaises(ValueError, mod12, 0)

    def test_types(self):
        self.assertRaises(ValueError, mod12, "hi")
