import pytest
from utils.string_utils import capitalize_first_letter


def test_capitalize_first_letter_normal_string():
    """Test capitalizing a normal lowercase string"""
    assert capitalize_first_letter("hello") == "Hello"


def test_capitalize_first_letter_already_capitalized():
    """Test string that's already capitalized"""
    assert capitalize_first_letter("World") == "World"


def test_capitalize_first_letter_single_character():
    """Test single character string"""
    assert capitalize_first_letter("a") == "A"


def test_capitalize_first_letter_with_spaces():
    """Test string starting with space"""
    assert capitalize_first_letter(" hello") == " hello"


def test_capitalize_first_letter_empty_string():
    """Test empty string - should handle gracefully"""
    with pytest.raises(IndexError):
        capitalize_first_letter("")


def test_capitalize_first_letter_none_input():
    """Test None input - according to docstring, should return empty string"""
    # Docstring says: "If string is None, return empty string"
    # This tests the documented behavior
    result = capitalize_first_letter(None)
    assert result == ""


def test_capitalize_first_letter_with_numbers():
    """Test string starting with a number"""
    assert capitalize_first_letter("123abc") == "123abc"


def test_capitalize_first_letter_special_characters():
    """Test string starting with special character"""
    assert capitalize_first_letter("!hello") == "!hello"
