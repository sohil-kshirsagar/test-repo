import pytest
from utils.string_utils import capitalize_first_letter


def test_capitalize_first_letter_with_none():
    """Test that None input returns empty string as per docstring"""
    result = capitalize_first_letter(None)
    assert result == "", "None should return empty string according to docstring"


def test_capitalize_first_letter_with_empty_string():
    """Test that empty string is handled properly"""
    result = capitalize_first_letter("")
    assert result == "", "Empty string should return empty string"


def test_capitalize_first_letter_with_single_character():
    """Test single character strings"""
    assert capitalize_first_letter("a") == "A"
    assert capitalize_first_letter("A") == "A"
    assert capitalize_first_letter("z") == "Z"


def test_capitalize_first_letter_with_normal_strings():
    """Test normal multi-character strings"""
    assert capitalize_first_letter("hello") == "Hello"
    assert capitalize_first_letter("world") == "World"
    assert capitalize_first_letter("python") == "Python"


def test_capitalize_first_letter_already_capitalized():
    """Test strings that are already capitalized"""
    assert capitalize_first_letter("Hello") == "Hello"
    assert capitalize_first_letter("HELLO") == "HELLO"


def test_capitalize_first_letter_with_non_letter_first_char():
    """Test strings starting with non-letter characters"""
    assert capitalize_first_letter("123abc") == "123abc"
    assert capitalize_first_letter("!hello") == "!hello"
    assert capitalize_first_letter(" hello") == " hello"


def test_capitalize_first_letter_with_numbers_only():
    """Test string with only numbers"""
    result = capitalize_first_letter("12345")
    assert result == "12345"


def test_capitalize_first_letter_with_special_characters():
    """Test strings with special characters at the start"""
    assert capitalize_first_letter("@test") == "@test"
    assert capitalize_first_letter("#hashtag") == "#hashtag"
