import pytest
from utils.calculator import add, subtract, safe_divide, validate_number

def test_add():
    assert add(1, 2) == 3

# Tests for subtract
def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_negative_result():
    assert subtract(3, 5) == -2

def test_subtract_with_negative_numbers():
    assert subtract(-5, -3) == -2
    assert subtract(-3, -5) == 2

def test_subtract_with_floats():
    assert subtract(5.5, 2.3) == pytest.approx(3.2)

def test_subtract_zero():
    assert subtract(5, 0) == 5
    assert subtract(0, 5) == -5

# Tests for validate_number
def test_validate_number_with_int():
    assert validate_number(5) == True

def test_validate_number_with_float():
    assert validate_number(5.5) == True

def test_validate_number_with_negative():
    assert validate_number(-5) == True
    assert validate_number(-5.5) == True

def test_validate_number_with_zero():
    assert validate_number(0) == True

def test_validate_number_with_string():
    with pytest.raises(TypeError, match="Must be a number"):
        validate_number("5")

def test_validate_number_with_none():
    with pytest.raises(TypeError, match="Must be a number"):
        validate_number(None)

def test_validate_number_with_list():
    with pytest.raises(TypeError, match="Must be a number"):
        validate_number([5])

# Tests for safe_divide
def test_safe_divide_positive_numbers():
    assert safe_divide(10, 2) == 5.0

def test_safe_divide_negative_numbers():
    assert safe_divide(-10, 2) == -5.0
    assert safe_divide(10, -2) == -5.0
    assert safe_divide(-10, -2) == 5.0

def test_safe_divide_with_floats():
    assert safe_divide(7.5, 2.5) == 3.0
    assert safe_divide(10.0, 3.0) == pytest.approx(3.333333, rel=1e-5)

def test_safe_divide_by_one():
    assert safe_divide(10, 1) == 10.0

def test_safe_divide_zero_numerator():
    assert safe_divide(0, 5) == 0.0

def test_safe_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        safe_divide(10, 0)

def test_safe_divide_invalid_numerator():
    with pytest.raises(TypeError, match="Must be a number"):
        safe_divide("10", 2)

def test_safe_divide_invalid_denominator():
    with pytest.raises(TypeError, match="Must be a number"):
        safe_divide(10, "2")

def test_safe_divide_both_invalid():
    with pytest.raises(TypeError, match="Must be a number"):
        safe_divide("10", "2")
