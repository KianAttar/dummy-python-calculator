"""Scientific calculator operations."""

import math


def sin(x, degrees=True):
    """Calculate sine of x.
    
    Args:
        x: Input value
        degrees: If True, treat x as degrees; otherwise radians
        
    Returns:
        float: Sine of x
    """
    if degrees:
        x = math.radians(x)
    return math.sin(x)


def cos(x, degrees=True):
    """Calculate cosine of x.
    
    Args:
        x: Input value
        degrees: If True, treat x as degrees; otherwise radians
        
    Returns:
        float: Cosine of x
    """
    if degrees:
        x = math.radians(x)
    return math.cos(x)


def tan(x, degrees=True):
    """Calculate tangent of x.
    
    Args:
        x: Input value
        degrees: If True, treat x as degrees; otherwise radians
        
    Returns:
        float: Tangent of x
    """
    if degrees:
        x = math.radians(x)
    return math.tan(x)


def asin(x, degrees=True):
    """Calculate arcsine of x.
    
    Args:
        x: Input value between -1 and 1
        degrees: If True, return result in degrees; otherwise radians
        
    Returns:
        float: Arcsine of x
    """
    result = math.asin(x)
    if degrees:
        result = math.degrees(result)
    return result


def acos(x, degrees=True):
    """Calculate arccosine of x.
    
    Args:
        x: Input value between -1 and 1
        degrees: If True, return result in degrees; otherwise radians
        
    Returns:
        float: Arccosine of x
    """
    result = math.acos(x)
    if degrees:
        result = math.degrees(result)
    return result


def atan(x, degrees=True):
    """Calculate arctangent of x.
    
    Args:
        x: Input value
        degrees: If True, return result in degrees; otherwise radians
        
    Returns:
        float: Arctangent of x
    """
    result = math.atan(x)
    if degrees:
        result = math.degrees(result)
    return result


def log(x, base=10):
    """Calculate logarithm of x.
    
    Args:
        x: Input value (must be positive)
        base: Base of logarithm (default 10)
        
    Returns:
        float: Logarithm of x
    """
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers")
    return math.log(x, base)


def ln(x):
    """Calculate natural logarithm of x.
    
    Args:
        x: Input value (must be positive)
        
    Returns:
        float: Natural logarithm of x
    """
    if x <= 0:
        raise ValueError("Logarithm undefined for non-positive numbers")
    return math.log(x)


def exp(x):
    """Calculate e raised to the power x.
    
    Args:
        x: Exponent
        
    Returns:
        float: e^x
    """
    return math.exp(x)


def power(x, y):
    """Calculate x raised to the power y.
    
    Args:
        x: Base
        y: Exponent
        
    Returns:
        float: x^y
    """
    return math.pow(x, y)


def sqrt(x):
    """Calculate square root of x.
    
    Args:
        x: Input value (must be non-negative)
        
    Returns:
        float: Square root of x
    """
    if x < 0:
        raise ValueError("Square root undefined for negative numbers")
    return math.sqrt(x)


def cbrt(x):
    """Calculate cube root of x.
    
    Args:
        x: Input value
        
    Returns:
        float: Cube root of x
    """
    if x >= 0:
        return math.pow(x, 1/3)
    else:
        return -math.pow(-x, 1/3)


def factorial(n):
    """Calculate factorial of n.
    
    Args:
        n: Non-negative integer
        
    Returns:
        int: n!
    """
    if n < 0:
        raise ValueError("Factorial undefined for negative numbers")
    if not isinstance(n, int) or (isinstance(n, float) and not n.is_integer()):
        raise ValueError("Factorial only defined for integers")
    return math.factorial(int(n))


# Constants
PI = math.pi
E = math.e

