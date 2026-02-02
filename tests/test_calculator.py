import pytest
from utils.calculator import add, subtract, safe_divide, _validate_number

def test_add():
    assert add(1, 2) == 3

# Tests for subtract
def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_negative_result():
    assert subtract(3, 5) == -2

def test_subtract_with_negative_numbers():
    assert subtract(-5, -3) == -2
    assert subtract(-3, 5) == -8

def test_subtract_with_floats():
    assert subtract(5.5, 2.3) == pytest.approx(3.2)

def test_subtract_zero():
    assert subtract(5, 0) == 5
    assert subtract(0, 5) == -5

# Tests for _validate_number
def test_validate_number_with_int():
    assert _validate_number(5) == True

def test_validate_number_with_float():
    assert _validate_number(5.5) == True

def test_validate_number_with_negative():
    assert _validate_number(-10) == True

def test_validate_number_with_zero():
    assert _validate_number(0) == True

def test_validate_number_with_string_raises_error():
    with pytest.raises(TypeError, match="Must be a number"):
        _validate_number("5")

def test_validate_number_with_none_raises_error():
    with pytest.raises(TypeError, match="Must be a number"):
        _validate_number(None)

def test_validate_number_with_list_raises_error():
    with pytest.raises(TypeError, match="Must be a number"):
        _validate_number([1, 2, 3])

# Tests for safe_divide
def test_safe_divide_basic():
    assert safe_divide(10, 2) == 5.0

def test_safe_divide_with_floats():
    assert safe_divide(7.5, 2.5) == 3.0

def test_safe_divide_negative_numbers():
    assert safe_divide(-10, 2) == -5.0
    assert safe_divide(10, -2) == -5.0
    assert safe_divide(-10, -2) == 5.0

def test_safe_divide_results_in_float():
    assert safe_divide(5, 2) == 2.5

def test_safe_divide_by_zero_raises_error():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        safe_divide(10, 0)

def test_safe_divide_with_invalid_first_argument():
    with pytest.raises(TypeError, match="Must be a number"):
        safe_divide("10", 2)

def test_safe_divide_with_invalid_second_argument():
    with pytest.raises(TypeError, match="Must be a number"):
        safe_divide(10, "2")

def test_safe_divide_with_both_invalid_arguments():
    with pytest.raises(TypeError, match="Must be a number"):
        safe_divide("10", "2")
