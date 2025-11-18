"""Tests for Calculator class."""

import pytest
from calculator.calculator import Calculator


def test_calculator_init():
    """Test calculator initialization."""
    calc = Calculator()
    assert calc.get_value() == 0
    assert calc.get_history() == []


def test_calculator_add():
    """Test calculator addition."""
    calc = Calculator()
    calc.set_value(5)
    result = calc.add(3)
    assert result == 8
    assert calc.get_value() == 8


def test_calculator_subtract():
    """Test calculator subtraction."""
    calc = Calculator()
    calc.set_value(10)
    result = calc.subtract(4)
    assert result == 6
    assert calc.get_value() == 6


def test_calculator_multiply():
    """Test calculator multiplication."""
    calc = Calculator()
    calc.set_value(5)
    result = calc.multiply(3)
    assert result == 15
    assert calc.get_value() == 15


def test_calculator_divide():
    """Test calculator division."""
    calc = Calculator()
    calc.set_value(20)
    result = calc.divide(4)
    assert result == 5
    assert calc.get_value() == 5


def test_calculator_divide_by_zero():
    """Test that calculator handles division by zero."""
    calc = Calculator()
    calc.set_value(10)
    with pytest.raises(ValueError):
        calc.divide(0)


def test_calculator_clear():
    """Test calculator clear function."""
    calc = Calculator()
    calc.set_value(100)
    calc.add(50)
    calc.clear()
    assert calc.get_value() == 0
    assert calc.get_history() == []


def test_calculator_history():
    """Test that calculator maintains history."""
    calc = Calculator()
    calc.set_value(10)
    calc.add(5)
    calc.subtract(3)
    calc.multiply(2)
    
    history = calc.get_history()
    assert len(history) == 3
    assert "+ 5 = 15" in history

