import pytest
from utils.string_utils import capitalize_first_letter


def test_capitalize_first_letter_normal_string():
    """Test capitalizing a normal lowercase string"""
    assert capitalize_first_letter("hello") == "Hello"


def test_capitalize_first_letter_already_capitalized():
    """Test that already capitalized string remains unchanged"""
    assert capitalize_first_letter("Hello") == "Hello"


def test_capitalize_first_letter_single_char():
    """Test capitalizing a single character"""
    assert capitalize_first_letter("a") == "A"


def test_capitalize_first_letter_none_input():
    """Test that None input returns empty string as per docstring"""
    assert capitalize_first_letter(None) == ""


def test_capitalize_first_letter_empty_string():
    """Test that empty string returns empty string"""
    assert capitalize_first_letter("") == ""
