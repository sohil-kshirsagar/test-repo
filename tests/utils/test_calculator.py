import pytest
import sys
from utils.calculator import multiply, subtract

def test_multiply_positive_integers():
    """Test that multiply returns the correct product of two positive integers."""
    # Arrange
    a = 3
    b = 4
    expected_result = 12
    
    # Act
    result = multiply(a, b)
    
    # Assert
    assert result == expected_result

def test_multiply_with_zero():
    """Test that multiply returns zero when one of the inputs is zero."""
    # Arrange
    a = 5
    b = 0
    expected_result = 0
    
    # Act
    result1 = multiply(a, b)  # Testing when second argument is zero
    result2 = multiply(b, a)  # Testing when first argument is zero
    
    # Assert
    assert result1 == expected_result
    assert result2 == expected_result

def test_multiply_positive_and_negative():
    """Test that multiply returns the correct product when one input is positive and the other is negative."""
    # Arrange
    a = 5
    b = -3
    expected_result = -15
    
    # Act
    result = multiply(a, b)
    
    # Assert
    assert result == expected_result
    
    # Also test with the negative number as the first argument
    a = -7
    b = 4
    expected_result = -28
    
    result = multiply(a, b)
    
    assert result == expected_result

def test_multiply_floating_point_numbers():
    """Test that multiply returns the correct product of two floating-point numbers."""
    # Arrange
    a = 2.5
    b = 3.5
    expected_result = 8.75
    
    # Act
    result = multiply(a, b)
    
    # Assert
    assert result == expected_result

def test_multiply_floating_point_edge_cases():
    """Test that multiply handles very small and very large floating point numbers correctly."""
    # Arrange
    # Very small positive numbers
    tiny_number = sys.float_info.min
    small_number = 1e-200
    
    # Very large numbers
    large_number = 1e200
    very_large_number = sys.float_info.max / 2  # Half of max to avoid overflow in test itself
    
    # Act & Assert
    
    # Test underflow scenario
    # When multiplying two very small numbers, we expect a result close to zero
    # but not exactly zero due to floating point representation
    result_tiny = multiply(tiny_number, tiny_number)
    assert result_tiny >= 0, "Result should be positive or zero"
    
    # Test with one small and one normal number
    result_small_normal = multiply(small_number, 2.0)
    assert result_small_normal == small_number * 2.0, "Should handle small number multiplication correctly"
    
    # Test with large numbers
    result_large = multiply(large_number, 2.0)
    assert result_large == large_number * 2.0, "Should handle large number multiplication correctly"
    
    # Test with very large numbers that don't overflow
    result_very_large = multiply(very_large_number, 0.5)
    assert result_very_large == very_large_number * 0.5, "Should handle very large number multiplication correctly"
    
    # Test potential overflow scenario
    # This is a valid operation in Python as it handles overflow by converting to inf
    result_overflow = multiply(very_large_number, very_large_number)
    assert result_overflow == very_large_number * very_large_number, "Should handle potential overflow correctly"

def test_subtract_positive_integers():
    """Test that subtract correctly calculates the difference between two positive integers."""
    # Arrange
    a = 5
    b = 3
    expected_result = 2
    
    # Act
    result = subtract(a, b)
    
    # Assert
    assert result == expected_result

def test_subtract_negative_integers():
    """Test that subtract correctly calculates the difference between two negative integers."""
    # Arrange
    a = -5
    b = -3
    expected_result = -2
    
    # Act
    result = subtract(a, b)
    
    # Assert
    assert result == expected_result

def test_subtract_zero():
    """Test that subtract returns the same number when subtracting zero from it."""
    # Arrange
    a_positive = 10
    a_negative = -7
    b = 0
    expected_result_positive = 10
    expected_result_negative = -7
    
    # Act
    result_positive = subtract(a_positive, b)
    result_negative = subtract(a_negative, b)
    
    # Assert
    assert result_positive == expected_result_positive
    assert result_negative == expected_result_negative

def test_subtract_smaller_from_larger():
    """Test that subtract returns a negative result when the first number is smaller than the second."""
    # Arrange
    a = 3
    b = 5
    expected_result = -2
    
    # Act
    result = subtract(a, b)
    
    # Assert
    assert result == expected_result

def test_subtract_floating_point_numbers():
    """Test that subtract correctly calculates the difference between two floating-point numbers."""
    # Arrange
    a = 5.5
    b = 2.2
    expected_result = 3.3
    
    # Act
    result = subtract(a, b)
    
    # Assert
    # Using pytest.approx to handle potential floating-point precision issues
    assert result == pytest.approx(expected_result)
