import pytest
from utils.string_utils import capitalize_first_letter


def test_capitalize_first_letter_normal_string():
    """Test capitalizing a normal lowercase string"""
    assert capitalize_first_letter("hello") == "Hello"


def test_capitalize_first_letter_already_capitalized():
    """Test string that is already capitalized"""
    assert capitalize_first_letter("Hello") == "Hello"


def test_capitalize_first_letter_none_input():
    """Test that None input returns empty string per docstring"""
    assert capitalize_first_letter(None) == ""


def test_capitalize_first_letter_empty_string():
    """Test that empty string returns empty string per docstring"""
    assert capitalize_first_letter("") == ""


def test_capitalize_first_letter_single_character():
    """Test single character string"""
    assert capitalize_first_letter("a") == "A"


def test_capitalize_first_letter_string_starting_with_space():
    """Test string starting with whitespace - should capitalize first actual letter"""
    # According to docstring: "Capitalize the first letter of a string"
    # This suggests it should find and capitalize the first LETTER, not just uppercase the first character
    assert capitalize_first_letter(" hello") == " Hello"


def test_capitalize_first_letter_string_with_number():
    """Test string starting with number"""
    assert capitalize_first_letter("123abc") == "123abc"


def test_capitalize_first_letter_all_uppercase():
    """Test string that is already all uppercase"""
    assert capitalize_first_letter("HELLO") == "HELLO"


def test_capitalize_first_letter_mixed_case():
    """Test string with mixed case"""
    assert capitalize_first_letter("hELLO") == "HELLO"
