def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def _validate_number(n):
    """Private validation helper"""
    if not isinstance(n, (int, float)):
        raise TypeError("Must be a number")
    return True

def safe_divide(a, b):
    """Divides two numbers with validation"""
    _validate_number(a)
    _validate_number(b)
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
