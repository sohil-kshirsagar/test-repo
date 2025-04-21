import pytest
from utils.calculator import add, divide

def test_add():
    assert add(1, 2) == 3

def test_divide_positive_integers():
    assert divide(10, 2) == 5.0

def test_divide_decimals():
    assert divide(5.5, 2.0) == 2.75

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_divide_with_negative_values():
    # Negative numerator, positive denominator
    assert divide(-10, 2) == -5.0
    # Positive numerator, negative denominator
    assert divide(10, -2) == -5.0
    # Both numerator and denominator negative
    assert divide(-10, -2) == 5.0
