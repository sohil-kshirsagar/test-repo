import pytest
from utils.calculator import add, divide

def test_add():
    assert add(1, 2) == 3

def test_divide():
    assert divide(10, 2) == 5
