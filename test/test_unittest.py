import os
import sys
import pytest

# make Lab1/src visible
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from main import word_count


class TestWordCount(unittest.TestCase):

    def test_basic_sentence(self):
        result = word_count("I love data and I love Python")
        expected = {"i": 2, "love": 2, "data": 1, "and": 1, "python": 1}
        self.assertEqual(result, expected)

    def test_case_insensitivity(self):
        result = word_count("Hello hello HELLO")
        self.assertEqual(result, {"hello": 3})

    def test_punctuation_removal(self):
        result = word_count("AI, AI! AI.")
        self.assertEqual(result, {"ai": 3})

    def test_empty_string(self):
        self.assertEqual(word_count(""), {})

    def test_invalid_input_type(self):
        with self.assertRaises(ValueError):
            word_count(1234)


if __name__ == "__main__":
    unittest.main()
