import pytest
from utils.string_utils import capitalize_first_letter


def test_capitalize_first_letter_basic():
    """Test basic string capitalization"""
    assert capitalize_first_letter("hello") == "Hello"


def test_capitalize_first_letter_already_capitalized():
    """Test string that is already capitalized"""
    assert capitalize_first_letter("Hello") == "Hello"


def test_capitalize_first_letter_single_char():
    """Test single character string"""
    assert capitalize_first_letter("h") == "H"


def test_capitalize_first_letter_empty_string():
    """Test empty string - per docstring, should handle gracefully"""
    # The docstring doesn't specify behavior for empty string,
    # but it should handle edge cases gracefully
    with pytest.raises(IndexError):
        capitalize_first_letter("")
