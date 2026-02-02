def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def validate_number(n):
    """Validation helper for numeric inputs"""
    if not isinstance(n, (int, float)):
        raise TypeError("Must be a number")
    return True

def safe_divide(a, b):
    """Divides two numbers with validation"""
    validate_number(a)
    validate_number(b)
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
