"""
Unit tests for string_utils module
"""
import pytest

from utils.string_utils import capitalize_first_letter


class TestCapitalizeFirstLetter:
    """Tests for capitalize_first_letter function"""

    def test_capitalize_first_letter_lowercase(self):
        """Test capitalizing a lowercase string"""
        result = capitalize_first_letter("hello")
        assert result == "Hello"

    def test_capitalize_first_letter_empty_string(self):
        """Test empty string - should handle gracefully"""
        result = capitalize_first_letter("")
        assert result == ""

    def test_capitalize_first_letter_none(self):
        """Test None input - according to docstring, should return empty string"""
        result = capitalize_first_letter(None)
        assert result == ""
