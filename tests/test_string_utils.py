import pytest
from utils.string_utils import capitalize_first_letter


class TestCapitalizeFirstLetter:
    """Test cases for capitalize_first_letter function."""

    def test_capitalize_first_letter_lowercase(self):
        """Test capitalizing a string starting with lowercase letter."""
        result = capitalize_first_letter("hello")
        assert result == "Hello"

    def test_capitalize_first_letter_already_capitalized(self):
        """Test string that is already capitalized."""
        result = capitalize_first_letter("Hello")
        assert result == "Hello"

    def test_capitalize_first_letter_single_character(self):
        """Test capitalizing a single character string."""
        result = capitalize_first_letter("a")
        assert result == "A"

    def test_capitalize_first_letter_with_spaces(self):
        """Test capitalizing a string with spaces."""
        result = capitalize_first_letter("hello world")
        assert result == "Hello world"

    def test_capitalize_first_letter_none(self):
        """Test that None returns empty string as per docstring."""
        # According to the docstring: "If string is None, return empty string"
        result = capitalize_first_letter(None)
        assert result == ""
