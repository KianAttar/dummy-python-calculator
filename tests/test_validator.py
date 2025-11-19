"""Tests for validator module."""

import pytest
from calculator.validator import validate_number, validate_operation, is_valid_expression


def test_validate_number():
    """Test number validation."""
    assert validate_number(5) == 5.0
    assert validate_number("3.14") == 3.14
    assert validate_number("-10") == -10.0
    assert validate_number(0) == 0.0


def test_validate_number_invalid():
    """Test invalid number validation."""
    with pytest.raises(ValueError):
        validate_number("abc")
    with pytest.raises(ValueError):
        validate_number(None)


def test_validate_operation():
    """Test operation validation."""
    assert validate_operation('+') == '+'
    assert validate_operation('-') == '-'
    assert validate_operation('*') == '*'
    assert validate_operation('/') == '/'
    assert validate_operation('×') == '×'
    assert validate_operation('÷') == '÷'


def test_validate_operation_invalid():
    """Test invalid operation validation."""
    with pytest.raises(ValueError):
        validate_operation('%')
    with pytest.raises(ValueError):
        validate_operation('abc')


def test_is_valid_expression():
    """Test expression validation."""
    assert is_valid_expression("2 + 2") == True
    assert is_valid_expression("(1 + 2) * 3") == True
    assert is_valid_expression("") == False
    assert is_valid_expression(None) == False


def test_is_valid_expression_unbalanced():
    """Test unbalanced parentheses detection."""
    assert is_valid_expression("(1 + 2") == False
    assert is_valid_expression("1 + 2)") == False
    assert is_valid_expression("((1 + 2)") == False

