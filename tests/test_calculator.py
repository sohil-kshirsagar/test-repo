import pytest
from utils.calculator import add, subtract

def test_add():
    assert add(1, 2) == 3

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_negative_result():
    assert subtract(3, 5) == -2

def test_subtract_with_negative_numbers():
    assert subtract(-5, -3) == -2

def test_subtract_zero():
    assert subtract(5, 0) == 5

def test_subtract_from_zero():
    assert subtract(0, 5) == -5
