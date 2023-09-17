import unittest
from pe017 import mod17

class Testpe017(unittest.TestCase):
    def test_mod17(self):
        self.assertEqual(mod17(1), 3)
        self.assertEqual(mod17(1000), 21124)

    def test_values(self):
        self.assertRaises(ValueError, mod17, -1)
        self.assertRaises(ValueError, mod17, -5)

    def test_types(self):
        self.assertRaises(ValueError, mod17, "hi")