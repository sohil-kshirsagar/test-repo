import pytest
from utils.string_utils import capitalize_first_letter


class TestCapitalizeFirstLetter:
    """Test suite for capitalize_first_letter function"""

    def test_none_input_returns_empty_string(self):
        """
        Test that None input returns empty string as documented.
        The docstring explicitly states: "If string is None, return empty string"
        """
        result = capitalize_first_letter(None)
        assert result == "", f"Expected empty string for None input, got {result!r}"

    def test_empty_string_returns_empty_string(self):
        """
        Test that empty string returns empty string.
        Edge case: no characters to capitalize
        """
        result = capitalize_first_letter("")
        assert result == "", f"Expected empty string for empty input, got {result!r}"

    def test_single_lowercase_character(self):
        """Test single lowercase character is capitalized"""
        result = capitalize_first_letter("a")
        assert result == "A", f"Expected 'A' for input 'a', got {result!r}"

    def test_single_uppercase_character(self):
        """Test single uppercase character remains uppercase"""
        result = capitalize_first_letter("A")
        assert result == "A", f"Expected 'A' for input 'A', got {result!r}"

    def test_normal_lowercase_string(self):
        """Test normal lowercase string has first letter capitalized"""
        result = capitalize_first_letter("hello")
        assert result == "Hello", f"Expected 'Hello' for input 'hello', got {result!r}"

    def test_already_capitalized_string(self):
        """Test that already capitalized string remains unchanged"""
        result = capitalize_first_letter("Hello")
        assert result == "Hello", f"Expected 'Hello' for input 'Hello', got {result!r}"

    def test_all_uppercase_string(self):
        """Test string with all uppercase letters"""
        result = capitalize_first_letter("HELLO")
        assert result == "HELLO", f"Expected 'HELLO' for input 'HELLO', got {result!r}"

    def test_mixed_case_string(self):
        """Test mixed case string capitalizes first letter only"""
        result = capitalize_first_letter("hELLO")
        assert result == "HELLO", f"Expected 'HELLO' for input 'hELLO', got {result!r}"

    def test_string_with_spaces(self):
        """Test string with multiple words"""
        result = capitalize_first_letter("hello world")
        assert result == "Hello world", f"Expected 'Hello world' for input 'hello world', got {result!r}"

    def test_string_starting_with_number(self):
        """Test string starting with a number - edge case for upper() method"""
        result = capitalize_first_letter("123abc")
        # Numbers don't have upper/lower case, so should remain unchanged
        assert result == "123abc", f"Expected '123abc' for input '123abc', got {result!r}"

    def test_string_starting_with_special_character(self):
        """Test string starting with special character"""
        result = capitalize_first_letter("!hello")
        # Special chars don't have upper case, rest should be preserved
        assert result == "!hello", f"Expected '!hello' for input '!hello', got {result!r}"

    def test_string_with_only_whitespace(self):
        """Test string with only whitespace character"""
        result = capitalize_first_letter(" ")
        assert result == " ", f"Expected single space for input ' ', got {result!r}"
