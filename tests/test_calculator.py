import pytest
from utils.calculator import add, divide

def test_add():
    assert add(1, 2) == 3

def test_divide():
    assert divide(10, 2) == 5
    
    # Edge case: repeating decimal
    result = divide(1, 3)
    assert round(result, 10) == 0.3333333333, f"Expected 0.3333333333, but got {result}"
    
    # Edge case: very small number
    result = divide(1, 1000000)
    assert round(result, 10) == 0.000001, f"Expected 0.000001, but got {result}"

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
