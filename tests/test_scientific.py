"""Tests for scientific calculator operations."""

import pytest
import math
from calculator.scientific import (
    sin, cos, tan, asin, acos, atan,
    log, ln, exp, power, sqrt, cbrt, factorial,
    PI, E
)


def test_trigonometric_functions():
    """Test trigonometric functions."""
    assert abs(sin(0) - 0) < 1e-10
    assert abs(sin(30) - 0.5) < 1e-10
    assert abs(cos(0) - 1) < 1e-10
    assert abs(tan(45) - 1) < 1e-10


def test_inverse_trigonometric_functions():
    """Test inverse trigonometric functions."""
    assert abs(asin(0) - 0) < 1e-10
    assert abs(asin(0.5) - 30) < 1e-10
    assert abs(acos(1) - 0) < 1e-10
    assert abs(atan(1) - 45) < 1e-10


def test_logarithmic_functions():
    """Test logarithmic functions."""
    assert abs(log(10) - 1) < 1e-10
    assert abs(log(100) - 2) < 1e-10
    assert abs(ln(E) - 1) < 1e-10


def test_logarithm_errors():
    """Test that logarithms handle invalid inputs."""
    with pytest.raises(ValueError):
        log(-1)
    with pytest.raises(ValueError):
        ln(0)


def test_exponential():
    """Test exponential function."""
    assert abs(exp(0) - 1) < 1e-10
    assert abs(exp(1) - E) < 1e-10


def test_power():
    """Test power function."""
    assert power(2, 3) == 8
    assert power(5, 2) == 25
    assert power(10, 0) == 1


def test_roots():
    """Test root functions."""
    assert sqrt(4) == 2
    assert sqrt(9) == 3
    assert abs(cbrt(8) - 2) < 1e-10
    assert abs(cbrt(27) - 3) < 1e-10


def test_sqrt_error():
    """Test that square root handles negative numbers."""
    with pytest.raises(ValueError):
        sqrt(-1)


def test_factorial():
    """Test factorial function."""
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800


def test_factorial_errors():
    """Test factorial error handling."""
    with pytest.raises(ValueError):
        factorial(-1)
    with pytest.raises(ValueError):
        factorial(1.5)


def test_constants():
    """Test mathematical constants."""
    assert abs(PI - math.pi) < 1e-10
    assert abs(E - math.e) < 1e-10

