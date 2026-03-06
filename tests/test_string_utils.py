import pytest
from utils.string_utils import capitalize_first_letter


class TestCapitalizeFirstLetter:
    """Test suite for capitalize_first_letter function"""

    def test_capitalize_normal_string(self):
        """Test capitalizing a normal lowercase string"""
        result = capitalize_first_letter("hello")
        assert result == "Hello"

    def test_capitalize_already_capitalized(self):
        """Test string that's already capitalized remains unchanged"""
        result = capitalize_first_letter("Hello")
        assert result == "Hello"

    def test_capitalize_single_character(self):
        """Test capitalizing a single character string"""
        result = capitalize_first_letter("a")
        assert result == "A"

    def test_capitalize_with_spaces(self):
        """Test string with spaces - only first letter should be capitalized"""
        result = capitalize_first_letter("hello world")
        assert result == "Hello world"

    def test_capitalize_none_input(self):
        """Test that None input returns empty string per docstring specification"""
        # According to the docstring: "If string is None, return empty string"
        result = capitalize_first_letter(None)
        assert result == ""

    def test_capitalize_empty_string(self):
        """Test that empty string is handled gracefully"""
        # Empty string should return empty string
        result = capitalize_first_letter("")
        assert result == ""

    def test_capitalize_number_first(self):
        """Test string starting with a number"""
        result = capitalize_first_letter("123abc")
        assert result == "123abc"

    def test_capitalize_special_char_first(self):
        """Test string starting with special character"""
        result = capitalize_first_letter("!hello")
        assert result == "!hello"
