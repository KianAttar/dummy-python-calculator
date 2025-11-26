"""Input validation utilities for calculator.

This module provides validation functions to ensure calculator inputs
are properly formatted and within acceptable ranges.
"""


def validate_number(value):
    """Validate that a value can be converted to a number.
    
    Args:
        value: The value to validate
        
    Returns:
        float: The validated number
        
    Raises:
        ValueError: If the value cannot be converted to a number
    """
    if value is None:
        raise ValueError("Value cannot be None")
    
    try:
        result = float(value)
        # Check for infinity and NaN
        if not (-1e308 <= result <= 1e308):
            raise ValueError(f"Number out of range: {value}")
        return result
    except (ValueError, TypeError):
        raise ValueError(f"Invalid number: {value}")


def validate_operation(operation):
    """Validate that an operation is supported.
    
    Args:
        operation: The operation to validate
        
    Returns:
        str: The validated operation
        
    Raises:
        ValueError: If the operation is not supported
    """
    valid_operations = ['+', '-', '*', '/', '×', '÷']
    if operation not in valid_operations:
        raise ValueError(f"Invalid operation: {operation}")
    return operation


def is_valid_expression(expression):
    """Check if an expression is valid.
    
    Args:
        expression: The expression to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not expression or not isinstance(expression, str):
        return False
    
    # Basic validation - check for balanced parentheses
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    
    return len(stack) == 0

