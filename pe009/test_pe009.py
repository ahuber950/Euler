import unittest
from pe009 import mod9


class Testpe009(unittest.TestCase):
    def test_pe009(self):
        self.assertEqual(mod9(1000), 31875000)
        self.assertEqual(mod9(12), 60)

    def test_values(self):
        self.assertRaises(ValueError, mod9, -1)
        self.assertRaises(ValueError, mod9, 0)

    def test_types(self):
        self.assertRaises(ValueError, mod9, "hi")
