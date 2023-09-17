import unittest
from pe003 import mod3


class Testpe003(unittest.TestCase):
    def test_pe003(self):
        self.assertEqual(mod3(10), 5)
        self.assertEqual(mod3(25), 5)
        self.assertEqual(mod3(13195), 29)
        self.assertEqual(mod3(600851475143), 6857)

    def test_values(self):
        self.assertRaises(ValueError, mod3, -1)

    def test_types(self):
        self.assertRaises(ValueError, mod3, "hi")
