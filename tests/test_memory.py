"""Tests for calculator memory functions."""

import pytest
from calculator.calculator import Calculator


def test_memory_initialization():
    """Test that memory initializes to zero."""
    calc = Calculator()
    assert calc.memory_recall() == 0


def test_memory_store():
    """Test storing value in memory."""
    calc = Calculator()
    calc.set_value(42)
    calc.memory_store()
    assert calc.memory_recall() == 42


def test_memory_store_explicit():
    """Test storing explicit value in memory."""
    calc = Calculator()
    calc.memory_store(99)
    assert calc.memory_recall() == 99


def test_memory_add():
    """Test adding to memory."""
    calc = Calculator()
    calc.memory_store(10)
    calc.set_value(5)
    calc.memory_add()
    assert calc.memory_recall() == 15


def test_memory_subtract():
    """Test subtracting from memory."""
    calc = Calculator()
    calc.memory_store(20)
    calc.set_value(8)
    calc.memory_subtract()
    assert calc.memory_recall() == 12


def test_memory_clear():
    """Test clearing memory."""
    calc = Calculator()
    calc.memory_store(100)
    calc.memory_clear()
    assert calc.memory_recall() == 0


def test_memory_operations_sequence():
    """Test sequence of memory operations."""
    calc = Calculator()
    calc.set_value(10)
    calc.memory_store()
    calc.set_value(5)
    calc.memory_add()
    calc.set_value(3)
    calc.memory_subtract()
    assert calc.memory_recall() == 12  # 10 + 5 - 3

