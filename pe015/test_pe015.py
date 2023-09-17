import unittest
from pe015 import mod15


class Testpe015(unittest.TestCase):
    def test_pe015(self):
        self.assertEqual(mod15(2,2), 2)
        self.assertEqual(mod15(3,3), 6)
        self.assertEqual(mod15(21,21), 137846528820)

    def test_values(self):
        self.assertRaises(ValueError, mod15, -1,5)
        self.assertRaises(ValueError, mod15, 0,0)

    def test_types(self):
        self.assertRaises(ValueError, mod15, "hi", 5)
