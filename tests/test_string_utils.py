import pytest
from utils.string_utils import capitalize_first_letter


class TestCapitalizeFirstLetter:
    """Comprehensive tests for capitalize_first_letter function"""

    # Basic functionality tests
    def test_lowercase_string(self):
        """Test capitalizing a lowercase string"""
        assert capitalize_first_letter("hello") == "Hello"

    def test_already_capitalized(self):
        """Test string that already starts with uppercase"""
        assert capitalize_first_letter("Hello") == "Hello"

    def test_all_uppercase(self):
        """Test string that is all uppercase"""
        assert capitalize_first_letter("HELLO") == "HELLO"

    def test_mixed_case(self):
        """Test mixed case string"""
        assert capitalize_first_letter("hELLO wORLD") == "HELLO wORLD"

    # Edge cases - empty and None
    def test_empty_string(self):
        """Test empty string returns empty string"""
        assert capitalize_first_letter("") == ""

    def test_none_input(self):
        """Test None input returns empty string"""
        assert capitalize_first_letter(None) == ""

    # Single character tests
    def test_single_lowercase_char(self):
        """Test single lowercase character"""
        assert capitalize_first_letter("a") == "A"

    def test_single_uppercase_char(self):
        """Test single uppercase character"""
        assert capitalize_first_letter("A") == "A"

    # Strings with spaces
    def test_string_with_leading_space(self):
        """Test string with leading space"""
        assert capitalize_first_letter(" hello") == " hello"

    def test_string_with_multiple_words(self):
        """Test string with multiple words only capitalizes first"""
        assert capitalize_first_letter("hello world") == "Hello world"

    # Strings with numbers
    def test_string_starting_with_number(self):
        """Test string starting with a number"""
        assert capitalize_first_letter("123abc") == "123abc"

    def test_string_with_numbers_after_letter(self):
        """Test string with numbers after first letter"""
        assert capitalize_first_letter("a123") == "A123"

    # Strings with special characters
    def test_string_starting_with_special_char(self):
        """Test string starting with special character"""
        assert capitalize_first_letter("!hello") == "!hello"

    def test_string_with_special_chars(self):
        """Test string containing special characters"""
        assert capitalize_first_letter("hello!world") == "Hello!world"

    # Unicode tests
    def test_unicode_lowercase(self):
        """Test unicode lowercase letter"""
        assert capitalize_first_letter("ñoño") == "Ñoño"

    def test_unicode_string(self):
        """Test string with unicode characters after first letter"""
        assert capitalize_first_letter("hello 世界") == "Hello 世界"

    # Whitespace variations
    def test_only_whitespace(self):
        """Test string with only whitespace"""
        assert capitalize_first_letter("   ") == "   "

    def test_tabs_and_newlines(self):
        """Test string starting with tab"""
        assert capitalize_first_letter("\thello") == "\thello"

    def test_newline_start(self):
        """Test string starting with newline"""
        assert capitalize_first_letter("\nhello") == "\nhello"

