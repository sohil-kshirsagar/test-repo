import pytest
from utils.string_utils import capitalize_first_letter


def test_capitalize_first_letter_normal_string():
    """Test capitalizing a normal lowercase string"""
    assert capitalize_first_letter("hello") == "Hello"


def test_capitalize_first_letter_special_characters():
    """Test capitalizing a string starting with special character"""
    assert capitalize_first_letter("!hello") == "!hello"


def test_capitalize_first_letter_empty_string():
    """Test capitalizing an empty string - should raise IndexError"""
    with pytest.raises(IndexError):
        capitalize_first_letter("")


def test_capitalize_first_letter_none():
    """Test capitalizing None - docstring says should return empty string"""
    # According to docstring: "If string is None, return empty string"
    # This test documents the expected behavior per specification
    assert capitalize_first_letter(None) == ""


def test_capitalize_first_letter_mixed_case():
    """Test capitalizing a string with mixed case"""
    assert capitalize_first_letter("hELLO") == "HELLO"


def test_capitalize_first_letter_with_newline():
    """Test capitalizing a string starting with newline"""
    assert capitalize_first_letter("\nhello") == "\nhello"
