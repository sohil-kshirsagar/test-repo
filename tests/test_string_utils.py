import pytest
from utils.string_utils import capitalize_first_letter


def test_capitalize_first_letter_basic():
    """Test basic capitalization of lowercase string"""
    assert capitalize_first_letter("hello") == "Hello"


def test_capitalize_first_letter_empty_string():
    """Test empty string - should handle gracefully"""
    # According to docstring: for None return empty string, but empty string should be handled
    assert capitalize_first_letter("") == ""


def test_capitalize_first_letter_none():
    """Test None input - docstring says should return empty string"""
    # According to the docstring: "If string is None, return empty string"
    assert capitalize_first_letter(None) == ""
