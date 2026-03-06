import pytest
from utils.calculator import add, safe_divide, validate_number

def test_add():
    assert add(1, 2) == 3


# Tests for validate_number
def test_validate_number_with_valid_float():
    """Test that validate_number accepts valid floats"""
    assert validate_number(3.14) == True


def test_validate_number_with_none_raises_type_error():
    """Test that validate_number raises TypeError for None"""
    with pytest.raises(TypeError, match="Must be a number"):
        validate_number(None)


def test_validate_number_with_list_raises_type_error():
    """Test that validate_number raises TypeError for lists"""
    with pytest.raises(TypeError, match="Must be a number"):
        validate_number([1, 2, 3])


# Tests for safe_divide
def test_safe_divide_with_valid_floats():
    """Test that safe_divide correctly divides two floats"""
    assert safe_divide(10.5, 2.5) == 4.2


def test_safe_divide_with_invalid_first_argument_raises_type_error():
    """Test that safe_divide raises TypeError when first argument is not a number"""
    with pytest.raises(TypeError, match="Must be a number"):
        safe_divide("10", 2)


def test_safe_divide_with_invalid_second_argument_raises_type_error():
    """Test that safe_divide raises TypeError when second argument is not a number"""
    with pytest.raises(TypeError, match="Must be a number"):
        safe_divide(10, "2")
