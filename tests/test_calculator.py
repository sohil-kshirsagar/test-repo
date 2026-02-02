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

def test_subtract_floats():
    assert subtract(5.5, 2.3) == pytest.approx(3.2)

# Tests for safe_divide
def test_safe_divide_positive_numbers():
    assert safe_divide(10, 2) == 5.0

def test_safe_divide_negative_numbers():
    assert safe_divide(-10, 2) == -5.0

def test_safe_divide_floats():
    assert safe_divide(7.5, 2.5) == 3.0

def test_safe_divide_by_zero_raises_error():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        safe_divide(10, 0)

def test_safe_divide_invalid_first_argument():
    with pytest.raises(TypeError, match="Must be a number"):
        safe_divide("10", 2)

def test_safe_divide_invalid_second_argument():
    with pytest.raises(TypeError, match="Must be a number"):
        safe_divide(10, "2")

# Tests for validate_number
def test_validate_number_with_int():
    assert validate_number(42) == True

def test_validate_number_with_float():
    assert validate_number(3.14) == True

def test_validate_number_with_string_raises_error():
    with pytest.raises(TypeError, match="Must be a number"):
        validate_number("not a number")

def test_validate_number_with_none_raises_error():
    with pytest.raises(TypeError, match="Must be a number"):
        validate_number(None)

def test_validate_number_with_list_raises_error():
    with pytest.raises(TypeError, match="Must be a number"):
        validate_number([1, 2, 3])
