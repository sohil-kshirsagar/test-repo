import pytest
from utils.calculator import add, factorial

def test_add():
    assert add(1, 2) == 3

def test_factorial_base_case_zero():
    """Test factorial of 0 returns 1"""
    assert factorial(0) == 1

def test_factorial_base_case_one():
    """Test factorial of 1 returns 1"""
    assert factorial(1) == 1

def test_factorial_small_values():
    """Test factorial with small positive integers"""
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120

def test_factorial_larger_values():
    """Test factorial with larger values"""
    assert factorial(6) == 720
    assert factorial(7) == 5040
    assert factorial(10) == 3628800

def test_factorial_edge_case_large_number():
    """Test factorial with a larger number to verify computation logic"""
    # 15! = 1307674368000
    assert factorial(15) == 1307674368000
