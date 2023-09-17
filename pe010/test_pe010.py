import unittest
from pe010 import mod10


class Testpe010(unittest.TestCase):
    def test_pe010(self):
        self.assertEqual(mod10(10), 17)
        self.assertEqual(mod10(12), 28)
        self.assertEqual(mod10(2000000), 142913828922)

    def test_values(self):
        self.assertRaises(ValueError, mod10, -1)
        self.assertRaises(ValueError, mod10, 0)

    def test_types(self):
        self.assertRaises(ValueError, mod10, "hi")
