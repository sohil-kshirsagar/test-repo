import pytest
from utils.string_utils import capitalize_first_letter

def test_capitalize_first_letter_normal_string():
    """Test capitalize_first_letter with normal lowercase string"""
    assert capitalize_first_letter("hello") == "Hello"
    assert capitalize_first_letter("world") == "World"

def test_capitalize_first_letter_already_capitalized():
    """Test capitalize_first_letter with already capitalized string"""
    assert capitalize_first_letter("Hello") == "Hello"
    assert capitalize_first_letter("World") == "World"

def test_capitalize_first_letter_single_character():
    """Test capitalize_first_letter with single character"""
    assert capitalize_first_letter("a") == "A"
    assert capitalize_first_letter("z") == "Z"

def test_capitalize_first_letter_single_character_already_capital():
    """Test capitalize_first_letter with single capital character"""
    assert capitalize_first_letter("A") == "A"
    assert capitalize_first_letter("Z") == "Z"

def test_capitalize_first_letter_mixed_case():
    """Test capitalize_first_letter with mixed case strings"""
    assert capitalize_first_letter("hELLO") == "HELLO"
    assert capitalize_first_letter("wORLD") == "WORLD"

def test_capitalize_first_letter_with_spaces():
    """Test capitalize_first_letter with strings containing spaces"""
    assert capitalize_first_letter("hello world") == "Hello world"
    assert capitalize_first_letter("test string") == "Test string"

def test_capitalize_first_letter_with_numbers():
    """Test capitalize_first_letter with strings starting with numbers"""
    # This will fail because the function tries to uppercase a number
    # but we're testing the actual behavior
    assert capitalize_first_letter("123abc") == "123abc"

def test_capitalize_first_letter_empty_string():
    """Test capitalize_first_letter with empty string - expects IndexError"""
    with pytest.raises(IndexError):
        capitalize_first_letter("")
