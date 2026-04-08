import pytest
from utils.string_utils import capitalize_first_letter


def test_capitalize_normal_string():
    """Test capitalizing a normal lowercase string"""
    assert capitalize_first_letter("hello") == "Hello"


def test_capitalize_already_capitalized():
    """Test string that is already capitalized"""
    assert capitalize_first_letter("Hello") == "Hello"


def test_capitalize_single_character():
    """Test capitalizing a single character"""
    assert capitalize_first_letter("a") == "A"


def test_capitalize_empty_string():
    """Test with empty string - should raise IndexError or handle gracefully"""
    with pytest.raises(IndexError):
        capitalize_first_letter("")


def test_capitalize_none_input():
    """Test with None input - per docstring, should return empty string"""
    # According to the docstring: "If string is None, return empty string"
    result = capitalize_first_letter(None)
    assert result == "", "Function should return empty string for None input per docstring"


def test_capitalize_string_with_number():
    """Test string starting with a number"""
    result = capitalize_first_letter("123abc")
    # Numbers don't have upper/lower case, so should remain the same
    assert result == "123abc"


def test_capitalize_string_with_special_char():
    """Test string starting with special character"""
    result = capitalize_first_letter("!hello")
    assert result == "!hello"


def test_capitalize_all_uppercase():
    """Test string that is all uppercase"""
    assert capitalize_first_letter("HELLO") == "HELLO"


def test_capitalize_multiword_string():
    """Test that only first letter is capitalized, not all words"""
    assert capitalize_first_letter("hello world") == "Hello world"
