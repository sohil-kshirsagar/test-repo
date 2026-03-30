import pytest
from utils.string_utils import capitalize_first_letter


class TestCapitalizeFirstLetter:
    """Test suite for capitalize_first_letter function"""

    def test_capitalize_normal_string(self):
        """Test capitalizing a normal lowercase string"""
        result = capitalize_first_letter("hello")
        assert result == "Hello"

    def test_capitalize_already_capitalized(self):
        """Test with already capitalized string"""
        result = capitalize_first_letter("Hello")
        assert result == "Hello"

    def test_none_input_returns_empty_string(self):
        """Test that None input returns empty string as per docstring"""
        result = capitalize_first_letter(None)
        assert result == ""

    def test_empty_string_returns_empty_string(self):
        """Test that empty string is handled gracefully"""
        result = capitalize_first_letter("")
        assert result == ""

    def test_single_character_string(self):
        """Test with single character"""
        result = capitalize_first_letter("a")
        assert result == "A"

    def test_string_with_numbers(self):
        """Test string starting with a number"""
        result = capitalize_first_letter("123abc")
        assert result == "123abc"

    def test_string_with_special_chars(self):
        """Test string starting with special character"""
        result = capitalize_first_letter("!hello")
        assert result == "!hello"
