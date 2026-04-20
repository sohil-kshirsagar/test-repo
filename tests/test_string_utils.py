import pytest
from utils.string_utils import capitalize_first_letter


class TestCapitalizeFirstLetter:
    """Test suite for capitalize_first_letter function"""

    def test_capitalize_normal_lowercase_string(self):
        """Test capitalizing a normal lowercase string"""
        result = capitalize_first_letter("hello")
        assert result == "Hello"

    def test_capitalize_already_capitalized_string(self):
        """Test with string that is already capitalized"""
        result = capitalize_first_letter("Hello")
        assert result == "Hello"

    def test_capitalize_single_character(self):
        """Test with single character string"""
        result = capitalize_first_letter("a")
        assert result == "A"

    def test_capitalize_with_none_input(self):
        """Test that None input returns empty string as per docstring specification"""
        # According to docstring: "If string is None, return empty string"
        result = capitalize_first_letter(None)
        assert result == ""

    def test_capitalize_empty_string(self):
        """Test with empty string - should handle gracefully"""
        # Edge case: empty string should either return empty string or handle error
        # Based on the function's purpose, returning empty string makes sense
        result = capitalize_first_letter("")
        assert result == ""

    def test_capitalize_string_with_leading_space(self):
        """Test string starting with a space"""
        result = capitalize_first_letter(" hello")
        # Should capitalize the space (no-op) and keep rest as is
        assert result == " hello"

    def test_capitalize_string_with_number_first(self):
        """Test string starting with a number"""
        result = capitalize_first_letter("123hello")
        # Numbers don't have upper/lower case, should return unchanged
        assert result == "123hello"

    def test_capitalize_all_uppercase_string(self):
        """Test with all uppercase string"""
        result = capitalize_first_letter("HELLO")
        assert result == "HELLO"

    def test_capitalize_string_with_special_characters(self):
        """Test string starting with special character"""
        result = capitalize_first_letter("!hello")
        # Special characters don't have upper/lower case
        assert result == "!hello"
