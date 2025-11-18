"""Tests for basic calculator operations."""

import pytest
from calculator.operations import add, subtract, multiply, divide


def test_add():
    """Test addition operation."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == 4.0


def test_subtract():
    """Test subtraction operation."""
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    assert subtract(0, 5) == -5
    assert subtract(10.5, 0.5) == 10.0


def test_multiply():
    """Test multiplication operation."""
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 100) == 0
    assert multiply(2.5, 2) == 5.0


def test_divide():
    """Test division operation."""
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(-10, 2) == -5
    

def test_divide_by_zero():
    """Test that division by zero raises ValueError."""
    with pytest.raises(ValueError):
        divide(10, 0)

