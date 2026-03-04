import pytest
from utils.string_utils import capitalize_first_letter


class TestCapitalizeFirstLetter:
    """Tests for capitalize_first_letter function"""

    def test_capitalize_normal_lowercase_string(self):
        """Test capitalizing a normal lowercase string"""
        result = capitalize_first_letter("hello world")
        assert result == "Hello world"

    def test_capitalize_already_capitalized_string(self):
        """Test that already capitalized strings remain unchanged"""
        result = capitalize_first_letter("Hello world")
        assert result == "Hello world"

    def test_capitalize_single_character(self):
        """Test capitalizing a single character string"""
        result = capitalize_first_letter("a")
        assert result == "A"

    def test_capitalize_empty_string(self):
        """Test behavior with empty string - should return empty string"""
        result = capitalize_first_letter("")
        assert result == ""

    def test_capitalize_none_input(self):
        """Test behavior with None input - docstring says should return empty string"""
        result = capitalize_first_letter(None)
        assert result == ""

    def test_capitalize_string_starting_with_number(self):
        """Test string starting with non-alphabetic character"""
        result = capitalize_first_letter("123abc")
        assert result == "123abc"

    def test_capitalize_string_with_only_whitespace(self):
        """Test string with only whitespace"""
        result = capitalize_first_letter("   ")
        assert result == "   "

    def test_capitalize_string_starting_with_special_char(self):
        """Test string starting with special character"""
        result = capitalize_first_letter("!hello")
        assert result == "!hello"

    def test_capitalize_all_caps_string(self):
        """Test string that is all uppercase"""
        result = capitalize_first_letter("HELLO")
        assert result == "HELLO"

    def test_capitalize_unicode_string(self):
        """Test with unicode characters"""
        result = capitalize_first_letter("été")
        assert result == "Été"
