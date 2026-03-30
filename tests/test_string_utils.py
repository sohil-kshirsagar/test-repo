import pytest
from utils.string_utils import capitalize_first_letter


class TestCapitalizeFirstLetter:
    """Test cases for capitalize_first_letter function"""

    def test_capitalize_simple_lowercase_word(self):
        """Test capitalizing a simple lowercase word"""
        result = capitalize_first_letter("hello")
        assert result == "Hello"

    def test_capitalize_already_capitalized_word(self):
        """Test with already capitalized word"""
        result = capitalize_first_letter("Hello")
        assert result == "Hello"

    def test_capitalize_all_uppercase_word(self):
        """Test with all uppercase word"""
        result = capitalize_first_letter("HELLO")
        assert result == "HELLO"

    def test_capitalize_single_character(self):
        """Test with single character string"""
        result = capitalize_first_letter("a")
        assert result == "A"

    def test_capitalize_with_spaces(self):
        """Test with string containing spaces (only first letter should be capitalized)"""
        result = capitalize_first_letter("hello world")
        assert result == "Hello world"

    def test_capitalize_with_numbers(self):
        """Test with string starting with number"""
        result = capitalize_first_letter("123abc")
        assert result == "123abc"  # Numbers don't have upper case

    def test_capitalize_with_special_characters(self):
        """Test with special character at the start"""
        result = capitalize_first_letter("!hello")
        assert result == "!hello"  # Special chars don't have upper case

    def test_capitalize_empty_string(self):
        """Test with empty string - should handle gracefully"""
        with pytest.raises(IndexError):
            # Empty string will cause IndexError on string[0]
            capitalize_first_letter("")

    def test_capitalize_none_input(self):
        """Test with None input - docstring says should return empty string"""
        # According to docstring: "If string is None, return empty string"
        result = capitalize_first_letter(None)
        assert result == ""
