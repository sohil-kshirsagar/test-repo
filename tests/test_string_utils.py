import pytest
from utils.string_utils import capitalize_first_letter


class TestCapitalizeFirstLetter:
    """Test suite for capitalize_first_letter function"""

    def test_none_input_returns_empty_string(self):
        """Test that None input returns empty string as per docstring specification"""
        result = capitalize_first_letter(None)
        assert result == "", "Expected empty string for None input"

    def test_normal_lowercase_string(self):
        """Test capitalizing a normal lowercase string"""
        result = capitalize_first_letter("hello")
        assert result == "Hello", "Expected first letter to be capitalized"

    def test_already_capitalized_string(self):
        """Test string that is already capitalized"""
        result = capitalize_first_letter("World")
        assert result == "World", "Expected already capitalized string to remain unchanged"

    def test_empty_string(self):
        """Test empty string input"""
        result = capitalize_first_letter("")
        assert result == "", "Expected empty string to return empty string"

    def test_single_character_lowercase(self):
        """Test single lowercase character"""
        result = capitalize_first_letter("a")
        assert result == "A", "Expected single lowercase character to be capitalized"

    def test_single_character_uppercase(self):
        """Test single uppercase character"""
        result = capitalize_first_letter("Z")
        assert result == "Z", "Expected single uppercase character to remain uppercase"

    def test_string_with_spaces(self):
        """Test string starting with a letter followed by spaces"""
        result = capitalize_first_letter("hello world")
        assert result == "Hello world", "Expected only first letter to be capitalized"

    def test_all_caps_string(self):
        """Test string that is all uppercase"""
        result = capitalize_first_letter("HELLO")
        assert result == "HELLO", "Expected all caps string to remain all caps"
