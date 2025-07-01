import pytest
from utils.calculator import divide

def test_divide_positive_integers():
    """Test that divide correctly handles division of two positive integers."""
    # Arrange
    a = 10
    b = 2
    
    # Act
    result = divide(a, b)
    
    # Assert
    assert result == 5

def test_divide_floating_point_numbers():
    """Test that divide correctly handles division of two floating-point numbers."""
    # Arrange
    a = 5.5
    b = 2.5
    
    # Act
    result = divide(a, b)
    
    # Assert
    assert result == 2.2

def test_divide_by_one():
    """Test that divide returns the numerator when the denominator is 1."""
    # Arrange
    test_cases = [
        (5, 1, 5),         # Integer case
        (7.5, 1, 7.5)      # Float case
    ]
    
    for numerator, denominator, expected in test_cases:
        # Act
        result = divide(numerator, denominator)
        
        # Assert
        assert result == expected, f"Expected {numerator} / {denominator} to equal {expected}, got {result}"

def test_divide_by_zero():
    """Test that divide raises a ZeroDivisionError when the denominator is zero."""
    # Arrange
    a = 10
    b = 0
    
    # Act & Assert
    with pytest.raises(ZeroDivisionError):
        divide(a, b)

def test_divide_by_very_small_number():
    """Test that divide correctly handles division by a number extremely close to zero."""
    # Arrange
    a = 1
    b = 1e-308  # A number extremely close to zero but not zero
    
    # Act
    result = divide(a, b)
    
    # Assert
    assert result > 1e307  # Result should be very large
    assert result != float('inf')  # Result should not be infinity
    assert isinstance(result, float)  # Result should be a float
    assert result < float('inf')  # Explicitly check it's less than infinity

def test_divide_non_numeric_types():
    """Test that divide raises TypeError when non-numeric types are provided."""
    # Test cases with different non-numeric types
    test_cases = [
        ("string", 5),  # String divided by number
        (10, "string"),  # Number divided by string
        ([1, 2, 3], 2),  # List divided by number
        (10, [1, 2, 3]),  # Number divided by list
        ({}, 5),  # Empty dict divided by number
        (5, {}),  # Number divided by empty dict
    ]
    
    # Test each case
    for a, b in test_cases:
        with pytest.raises(TypeError):
            divide(a, b)
