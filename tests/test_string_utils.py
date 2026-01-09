import pytest
from utils.string_utils import capitalize_first_letter


def test_capitalize_first_letter_normal_string():
    """Test capitalizing a normal lowercase string"""
    assert capitalize_first_letter("hello") == "Hello"


def test_capitalize_first_letter_already_capitalized():
    """Test a string that's already capitalized"""
    assert capitalize_first_letter("Hello") == "Hello"


def test_capitalize_first_letter_all_caps():
    """Test a string that's all uppercase"""
    assert capitalize_first_letter("HELLO") == "HELLO"


def test_capitalize_first_letter_single_lowercase_char():
    """Test a single lowercase character"""
    assert capitalize_first_letter("a") == "A"


def test_capitalize_first_letter_single_uppercase_char():
    """Test a single uppercase character"""
    assert capitalize_first_letter("A") == "A"


def test_capitalize_first_letter_empty_string():
    """Test empty string - should handle gracefully"""
    # Empty string should either return empty or raise appropriate error
    with pytest.raises(IndexError):
        capitalize_first_letter("")


def test_capitalize_first_letter_none_input():
    """Test None input - docstring says should return empty string"""
    # According to docstring: "If string is None, return empty string"
    assert capitalize_first_letter(None) == ""


def test_capitalize_first_letter_with_spaces():
    """Test string starting with space"""
    assert capitalize_first_letter(" hello") == " hello"


def test_capitalize_first_letter_number_first():
    """Test string starting with a number"""
    assert capitalize_first_letter("123abc") == "123abc"


def test_capitalize_first_letter_special_char_first():
    """Test string starting with special character"""
    assert capitalize_first_letter("!hello") == "!hello"


def test_capitalize_first_letter_mixed_case():
    """Test string with mixed case"""
    assert capitalize_first_letter("hELLO") == "HELLO"


def test_capitalize_first_letter_multiword():
    """Test multi-word string - should only capitalize first letter"""
    assert capitalize_first_letter("hello world") == "Hello world"


def test_capitalize_first_letter_with_newline():
    """Test string starting with newline"""
    assert capitalize_first_letter("\nhello") == "\nhello"


def test_capitalize_first_letter_unicode():
    """Test with unicode characters"""
    assert capitalize_first_letter("über") == "Über"
