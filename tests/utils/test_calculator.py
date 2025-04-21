import pytest
import math
from utils.calculator import divide

def test_divide_positive_integers():
    """Test that divide returns the correct quotient when dividing two positive integers."""
    # Arrange
    a = 10
    b = 2
    
    # Act
    result = divide(a, b)
    
    # Assert
    assert result == 5

def test_divide_floating_point_numbers():
    """Test that divide returns the correct quotient when dividing two floating-point numbers."""
    # Arrange
    a = 5.5
    b = 2.2
    expected_result = 2.5  # 5.5 / 2.2 = 2.5
    
    # Act
    result = divide(a, b)
    
    # Assert
    assert result == expected_result

def test_divide_zero_numerator():
    """Test that divide returns 0 when the numerator is 0 and the denominator is non-zero."""
    # Arrange
    a = 0
    b = 5  # Any non-zero number
    
    # Act
    result = divide(a, b)
    
    # Assert
    assert result == 0

def test_divide_by_zero():
    """Test that divide raises a ZeroDivisionError when dividing by zero."""
    # Arrange
    a = 10
    b = 0
    
    # Act & Assert
    with pytest.raises(ZeroDivisionError):
        divide(a, b)

def test_divide_with_very_small_denominator():
    """Test that divide handles division with a very small denominator resulting in a very large number."""
    # Arrange
    a = 1.0
    b = 1e-308  # Very small number close to zero but not zero
    
    # Act
    result = divide(a, b)
    
    # Assert
    assert result > 1e307  # Result should be a very large number
    assert math.isfinite(result) or result == float('inf')  # Result should be either finite or infinity
    # Note: On some systems with different floating-point precision, 
    # this might return float('inf') if it exceeds the maximum representable value

def test_divide_non_numeric_arguments():
    """Test that divide raises TypeError when non-numeric arguments are provided."""
    
    # Test with string arguments
    with pytest.raises(TypeError):
        divide("10", "2")
    
    # Test with None values
    with pytest.raises(TypeError):
        divide(None, 5)
    
    with pytest.raises(TypeError):
        divide(10, None)
    
    # Test with mixed numeric and non-numeric arguments
    with pytest.raises(TypeError):
        divide(10, "2")
    
    with pytest.raises(TypeError):
        divide("10", 2)
