import unittest
from pe001 import mod1


class Testpe001(unittest.TestCase):
    def test_pe001(self):
        self.assertEqual(mod1(10), 23)

    def test_values(self):
        self.assertRaises(ValueError, mod1, -1)

    def test_types(self):
        self.assertRaises(ValueError, mod1, "hi")
