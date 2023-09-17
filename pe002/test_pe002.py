import unittest
from pe002 import mod2


class Testpe002(unittest.TestCase):
    def test_pe001(self):
        self.assertEqual(mod2(10), 10)

    def test_values(self):
        self.assertRaises(ValueError, mod2, -1)

    def test_types(self):
        self.assertRaises(ValueError, mod2, "hi")
