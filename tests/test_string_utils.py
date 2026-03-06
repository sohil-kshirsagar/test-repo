"""
Tests for string_utils module
"""
import pytest
from utils.string_utils import capitalize_first_letter


def test_capitalize_first_letter_basic():
    """Test basic capitalization"""
    assert capitalize_first_letter("hello") == "Hello"
    assert capitalize_first_letter("world") == "World"


def test_capitalize_first_letter_already_capitalized():
    """Test string that's already capitalized"""
    assert capitalize_first_letter("Hello") == "Hello"


def test_capitalize_first_letter_single_character():
    """Test single character string"""
    assert capitalize_first_letter("a") == "A"
    assert capitalize_first_letter("Z") == "Z"


def test_capitalize_first_letter_with_numbers():
    """Test string starting with numbers"""
    result = capitalize_first_letter("123abc")
    # Numbers don't have upper/lower case, so this should return "123abc"
    assert result == "123abc"


def test_capitalize_first_letter_none():
    """Test that None returns empty string per docstring"""
    # Per docstring: "If string is None, return empty string"
    result = capitalize_first_letter(None)
    assert result == "", "Function should return empty string for None input per docstring"


def test_capitalize_first_letter_empty_string():
    """Test empty string handling"""
    # Edge case: empty string should be handled gracefully
    result = capitalize_first_letter("")
    assert result == ""
