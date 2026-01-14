import pytest
from utils.string_utils import capitalize_first_letter


def test_capitalize_first_letter_normal_string():
    """Test capitalizing a normal lowercase string"""
    assert capitalize_first_letter("hello") == "Hello"


def test_capitalize_first_letter_already_capitalized():
    """Test string that is already capitalized"""
    assert capitalize_first_letter("Hello") == "Hello"


def test_capitalize_first_letter_single_character():
    """Test single character string"""
    assert capitalize_first_letter("a") == "A"


def test_capitalize_first_letter_empty_string():
    """Test empty string - should handle gracefully"""
    result = capitalize_first_letter("")
    assert result == ""


def test_capitalize_first_letter_none_input():
    """Test None input - according to docstring should return empty string"""
    result = capitalize_first_letter(None)
    assert result == ""
