"""Calculator core module.

This module provides the core calculator functionality including basic operations,
scientific functions, and programmer mode operations.

Main Components:
    - Calculator: Main calculator class with state management
    - Basic Operations: add, subtract, multiply, divide
    - Scientific Operations: trigonometric, logarithmic, exponential functions
    - Programmer Operations: base conversions, bitwise operations
    - Validators: input validation utilities
"""

from calculator.calculator import Calculator
from calculator.operations import add, subtract, multiply, divide
from calculator.validator import validate_number, validate_operation, is_valid_expression

__all__ = [
    'Calculator',
    'add',
    'subtract',
    'multiply',
    'divide',
    'validate_number',
    'validate_operation',
    'is_valid_expression',
]

__version__ = '1.0.0'
