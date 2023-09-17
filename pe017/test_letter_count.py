import unittest
from pe017 import letter_count

class Testpe017(unittest.TestCase):
    def test_letter_count(self):
        self.assertEqual(letter_count(1), 3)
        self.assertEqual(letter_count(13), 8)
        self.assertEqual(letter_count(342), 23)
        self.assertEqual(letter_count(990), 20)
        self.assertEqual(letter_count(1000), 11)

    def test_values(self):
        self.assertRaises(ValueError, letter_count, 0)
        self.assertRaises(ValueError, letter_count, -5)

    def test_types(self):
        self.assertRaises(ValueError, letter_count, "hi")