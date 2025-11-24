"""Tests for programmer calculator operations."""

import pytest
from calculator.programmer import (
    to_binary, to_octal, to_hexadecimal,
    from_binary, from_octal, from_hexadecimal,
    bitwise_and, bitwise_or, bitwise_xor, bitwise_not,
    left_shift, right_shift, convert_base
)


def test_to_binary():
    """Test conversion to binary."""
    assert to_binary(0) == '0'
    assert to_binary(10) == '1010'
    assert to_binary(255) == '11111111'


def test_to_octal():
    """Test conversion to octal."""
    assert to_octal(0) == '0'
    assert to_octal(8) == '10'
    assert to_octal(64) == '100'


def test_to_hexadecimal():
    """Test conversion to hexadecimal."""
    assert to_hexadecimal(0) == '0'
    assert to_hexadecimal(15) == 'F'
    assert to_hexadecimal(255) == 'FF'


def test_from_binary():
    """Test conversion from binary."""
    assert from_binary('0') == 0
    assert from_binary('1010') == 10
    assert from_binary('0b1010') == 10
    assert from_binary('11111111') == 255


def test_from_octal():
    """Test conversion from octal."""
    assert from_octal('0') == 0
    assert from_octal('10') == 8
    assert from_octal('0o10') == 8
    assert from_octal('100') == 64


def test_from_hexadecimal():
    """Test conversion from hexadecimal."""
    assert from_hexadecimal('0') == 0
    assert from_hexadecimal('F') == 15
    assert from_hexadecimal('0xF') == 15
    assert from_hexadecimal('FF') == 255


def test_bitwise_and():
    """Test bitwise AND operation."""
    assert bitwise_and(12, 10) == 8  # 1100 & 1010 = 1000
    assert bitwise_and(15, 7) == 7   # 1111 & 0111 = 0111


def test_bitwise_or():
    """Test bitwise OR operation."""
    assert bitwise_or(12, 10) == 14  # 1100 | 1010 = 1110
    assert bitwise_or(8, 4) == 12    # 1000 | 0100 = 1100


def test_bitwise_xor():
    """Test bitwise XOR operation."""
    assert bitwise_xor(12, 10) == 6  # 1100 ^ 1010 = 0110
    assert bitwise_xor(15, 7) == 8   # 1111 ^ 0111 = 1000


def test_bitwise_not():
    """Test bitwise NOT operation."""
    assert bitwise_not(0) == -1
    assert bitwise_not(1) == -2
    assert bitwise_not(-1) == 0


def test_left_shift():
    """Test left shift operation."""
    assert left_shift(1, 1) == 2   # 1 << 1 = 10
    assert left_shift(1, 4) == 16  # 1 << 4 = 10000
    assert left_shift(5, 2) == 20  # 101 << 2 = 10100


def test_right_shift():
    """Test right shift operation."""
    assert right_shift(8, 1) == 4   # 1000 >> 1 = 100
    assert right_shift(16, 4) == 1  # 10000 >> 4 = 1
    assert right_shift(20, 2) == 5  # 10100 >> 2 = 101


def test_convert_base():
    """Test base conversion."""
    assert convert_base('1010', 2, 10) == '10'
    assert convert_base('10', 10, 2) == '1010'
    assert convert_base('FF', 16, 10) == '255'
    assert convert_base('255', 10, 16) == 'FF'
    assert convert_base('77', 8, 10) == '63'

