import os
import sys
import pytest

# make Lab1/src visible
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


from main import word_count


def test_basic_sentence():
    result = word_count("I love data and I love Python")
    assert result == {"i": 2, "love": 2, "data": 1, "and": 1, "python": 1}


def test_case_insensitivity():
    result = word_count("Hello hello HELLO")
    assert result == {"hello": 3}


def test_punctuation_removal():
    result = word_count("AI, AI! AI.")
    assert result == {"ai": 3}


def test_empty_string():
    result = word_count("")
    assert result == {}


def test_invalid_input_type():
    with pytest.raises(ValueError):
        word_count(1234)
