from utils.string_utils import capitalize_first_letter


def test_capitalize_first_letter_basic():
    """Test capitalizing the first letter of a normal string"""
    assert capitalize_first_letter("hello") == "Hello"


def test_capitalize_first_letter_empty_string():
    """Test handling of empty string - should handle gracefully"""
    # Per docstring: "return the string with the first letter capitalized"
    # Empty string has no first letter, so should return empty string
    assert capitalize_first_letter("") == ""


def test_capitalize_first_letter_none():
    """Test handling of None value - should return empty string per docstring"""
    # Per docstring: "If string is None, return empty string"
    assert capitalize_first_letter(None) == ""
