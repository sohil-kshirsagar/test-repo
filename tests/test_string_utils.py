import pytest
from utils.string_utils import capitalize_first_letter


class TestCapitalizeFirstLetter:
    """Test suite for capitalize_first_letter function"""

    def test_none_input_returns_empty_string(self):
        """Test that None input returns empty string as per docstring"""
        # This tests the documented behavior: "If string is None, return empty string"
        result = capitalize_first_letter(None)
        assert result == "", "None input should return empty string"

    def test_empty_string_returns_empty_string(self):
        """Test that empty string is handled correctly"""
        # Empty string should return empty string (edge case)
        result = capitalize_first_letter("")
        assert result == ""

    def test_single_lowercase_character(self):
        """Test single lowercase character gets capitalized"""
        result = capitalize_first_letter("a")
        assert result == "A"

    def test_single_uppercase_character(self):
        """Test single uppercase character remains uppercase"""
        result = capitalize_first_letter("A")
        assert result == "A"

    def test_lowercase_word(self):
        """Test normal lowercase word gets first letter capitalized"""
        result = capitalize_first_letter("hello")
        assert result == "Hello"

    def test_already_capitalized_word(self):
        """Test already capitalized word remains unchanged"""
        result = capitalize_first_letter("Hello")
        assert result == "Hello"

    def test_all_uppercase_word(self):
        """Test all uppercase word - only first letter should be uppercase, rest unchanged"""
        result = capitalize_first_letter("HELLO")
        assert result == "HELLO"

    def test_string_with_spaces(self):
        """Test string starting with space"""
        result = capitalize_first_letter(" hello")
        assert result == " hello", "Space should remain space (not capitalized)"

    def test_string_with_numbers(self):
        """Test string starting with number"""
        result = capitalize_first_letter("123abc")
        assert result == "123abc", "Numbers should not be capitalized"

    def test_string_with_special_characters(self):
        """Test string starting with special character"""
        result = capitalize_first_letter("!hello")
        assert result == "!hello", "Special characters should not be capitalized"

    def test_unicode_characters(self):
        """Test unicode characters are handled correctly"""
        result = capitalize_first_letter("café")
        assert result == "Café"

    def test_string_with_only_numbers(self):
        """Test string containing only numbers"""
        result = capitalize_first_letter("123")
        assert result == "123"
