"""Tests for text formatting utilities."""

import pytest

from utils.text_formatter import (  # isort:skip
    extract_initials,
    format_display_name,
    normalize_whitespace,
    truncate_with_ellipsis,
)


class TestNormalizeWhitespace:
    """Tests for normalize_whitespace function."""

    def test_tabs_and_newlines_collapsed(self):
        """Tabs and newlines should be collapsed to single space."""
        result = normalize_whitespace("hello\t\n\r\nworld")
        assert result == "hello world"

    def test_leading_trailing_whitespace_stripped(self):
        """Leading and trailing whitespace should be stripped."""
        result = normalize_whitespace("  hello world  ")
        assert result == "hello world"

    def test_empty_string_returns_empty(self):
        """Empty string should return empty string."""
        result = normalize_whitespace("")
        assert result == ""

    def test_only_whitespace_returns_empty(self):
        """String with only whitespace should return empty string."""
        result = normalize_whitespace("   \t\n\r  ")
        assert result == ""

    def test_none_raises_type_error(self):
        """None input should raise TypeError."""
        with pytest.raises(TypeError, match="Expected string, got NoneType"):
            normalize_whitespace(None)


class TestTruncateWithEllipsis:
    """Tests for truncate_with_ellipsis function."""

    def test_text_equal_to_max_length_unchanged(self):
        """Text equal to max_length should be returned unchanged."""
        result = truncate_with_ellipsis("hello", 5)
        assert result == "hello"

    def test_text_longer_than_max_length_truncated(self):
        """Text longer than max_length should be truncated with ellipsis."""
        result = truncate_with_ellipsis("hello world", 8)
        assert result == "hello..."

    def test_truncate_at_minimum_length(self):
        """Truncation at minimum length (4) should work correctly."""
        result = truncate_with_ellipsis("hello", 4)
        assert result == "h..."

    def test_max_length_less_than_four_raises_error(self):
        """max_length less than 4 should raise ValueError."""
        with pytest.raises(ValueError, match="max_length must be"):
            truncate_with_ellipsis("hello", 3)

    def test_max_length_zero_raises_error(self):
        """max_length of 0 should raise ValueError."""
        with pytest.raises(ValueError, match="max_length must be"):
            truncate_with_ellipsis("hello", 0)

    def test_max_length_negative_raises_error(self):
        """Negative max_length should raise ValueError."""
        with pytest.raises(ValueError, match="max_length must be"):
            truncate_with_ellipsis("hello", -1)

    def test_non_string_text_raises_type_error(self):
        """Non-string text should raise TypeError."""
        with pytest.raises(TypeError, match="Expected string, got int"):
            truncate_with_ellipsis(123, 10)

    def test_non_integer_max_length_raises_value_error(self):
        """Non-integer max_length should raise ValueError."""
        with pytest.raises(ValueError, match="max_length must be"):
            truncate_with_ellipsis("hello", "10")

    def test_float_max_length_raises_value_error(self):
        """Float max_length should raise ValueError."""
        with pytest.raises(ValueError, match="max_length must be"):
            truncate_with_ellipsis("hello", 10.5)


class TestExtractInitials:
    """Tests for extract_initials function."""

    def test_single_name_returns_single_initial(self):
        """Single name should return single uppercase initial."""
        result = extract_initials("John")
        assert result == "J"

    def test_two_names_returns_two_initials(self):
        """Two names should return two uppercase initials."""
        result = extract_initials("John Doe")
        assert result == "JD"

    def test_three_names_returns_three_initials(self):
        """Three names should return three uppercase initials."""
        result = extract_initials("John Paul Doe")
        assert result == "JPD"

    def test_lowercase_names_return_uppercase_initials(self):
        """Lowercase names should return uppercase initials."""
        result = extract_initials("john doe")
        assert result == "JD"

    def test_multiple_spaces_between_names_handled(self):
        """Multiple spaces between names should be handled correctly."""
        result = extract_initials("John    Doe")
        assert result == "JD"

    def test_leading_trailing_spaces_handled(self):
        """Leading and trailing spaces should be handled correctly."""
        result = extract_initials("  John Doe  ")
        assert result == "JD"

    def test_empty_string_raises_value_error(self):
        """Empty string should raise ValueError."""
        with pytest.raises(ValueError, match="Name cannot be empty"):
            extract_initials("")

    def test_only_whitespace_raises_value_error(self):
        """String with only whitespace should raise ValueError."""
        with pytest.raises(ValueError, match="Name cannot be empty"):
            extract_initials("   ")

    def test_non_string_raises_type_error(self):
        """Non-string input should raise TypeError."""
        with pytest.raises(TypeError, match="Expected string, got int"):
            extract_initials(123)


class TestFormatDisplayName:
    """Tests for format_display_name function."""

    def test_basic_name_formatting(self):
        """Basic first and last name should be formatted correctly."""
        result = format_display_name("John", "Doe")
        assert result["full"] == "John Doe"
        assert result["initials"] == "JD"
        assert result["first_initial_last"] == "J. Doe"
        assert result["last_first"] == "Doe, John"

    def test_names_with_extra_whitespace(self):
        """Names with extra whitespace should be normalized."""
        result = format_display_name("  John  ", "  Doe  ")
        assert result["full"] == "John Doe"
        assert result["initials"] == "JD"
        assert result["first_initial_last"] == "J. Doe"
        assert result["last_first"] == "Doe, John"

    def test_custom_max_length(self):
        """Custom max_length should be respected in full name."""
        result = format_display_name("John", "Doe", max_length=5)
        assert result["full"] == "Jo..."
        assert result["initials"] == "JD"

    def test_short_name_not_truncated(self):
        """Short name within max_length should not be truncated."""
        result = format_display_name("Al", "Li", max_length=20)
        assert result["full"] == "Al Li"
        assert result["initials"] == "AL"
        assert result["first_initial_last"] == "A. Li"
        assert result["last_first"] == "Li, Al"

    def test_names_with_tabs_and_newlines(self):
        """Names with tabs and newlines should be normalized."""
        result = format_display_name("John\t\n", "Doe\r\n")
        assert result["full"] == "John Doe"
        assert result["initials"] == "JD"
