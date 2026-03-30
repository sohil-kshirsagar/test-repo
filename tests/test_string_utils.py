import pytest
from utils.string_utils import capitalize_first_letter


class TestCapitalizeFirstLetter:
    """Tests for capitalize_first_letter function"""

    def test_capitalize_first_letter_lowercase(self):
        """Test capitalizing first letter of lowercase string"""
        result = capitalize_first_letter("hello")
        assert result == "Hello"

    def test_capitalize_first_letter_single_character(self):
        """Test single character string"""
        result = capitalize_first_letter("a")
        assert result == "A"

    def test_capitalize_first_letter_none(self):
        """Test None input should return empty string according to docstring"""
        result = capitalize_first_letter(None)
        assert result == ""

    def test_capitalize_first_letter_empty_string(self):
        """Test empty string input"""
        result = capitalize_first_letter("")
        assert result == ""
