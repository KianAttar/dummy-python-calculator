"""Programmer calculator operations - base conversions and bitwise operations."""


def to_binary(n):
    """Convert decimal to binary.
    
    Args:
        n: Integer to convert
        
    Returns:
        str: Binary representation (without '0b' prefix)
    """
    if not isinstance(n, int):
        n = int(n)
    return bin(n)[2:]


def to_octal(n):
    """Convert decimal to octal.
    
    Args:
        n: Integer to convert
        
    Returns:
        str: Octal representation (without '0o' prefix)
    """
    if not isinstance(n, int):
        n = int(n)
    return oct(n)[2:]


def to_hexadecimal(n):
    """Convert decimal to hexadecimal.
    
    Args:
        n: Integer to convert
        
    Returns:
        str: Hexadecimal representation (without '0x' prefix), uppercase
    """
    if not isinstance(n, int):
        n = int(n)
    return hex(n)[2:].upper()


def from_binary(binary_str):
    """Convert binary to decimal.
    
    Args:
        binary_str: Binary string (with or without '0b' prefix)
        
    Returns:
        int: Decimal value
    """
    if binary_str.startswith('0b'):
        binary_str = binary_str[2:]
    return int(binary_str, 2)


def from_octal(octal_str):
    """Convert octal to decimal.
    
    Args:
        octal_str: Octal string (with or without '0o' prefix)
        
    Returns:
        int: Decimal value
    """
    if octal_str.startswith('0o'):
        octal_str = octal_str[2:]
    return int(octal_str, 8)


def from_hexadecimal(hex_str):
    """Convert hexadecimal to decimal.
    
    Args:
        hex_str: Hexadecimal string (with or without '0x' prefix)
        
    Returns:
        int: Decimal value
    """
    if hex_str.startswith('0x'):
        hex_str = hex_str[2:]
    return int(hex_str, 16)


def bitwise_and(a, b):
    """Perform bitwise AND operation.
    
    Args:
        a: First integer
        b: Second integer
        
    Returns:
        int: Result of a AND b
    """
    return int(a) & int(b)


def bitwise_or(a, b):
    """Perform bitwise OR operation.
    
    Args:
        a: First integer
        b: Second integer
        
    Returns:
        int: Result of a OR b
    """
    return int(a) | int(b)


def bitwise_xor(a, b):
    """Perform bitwise XOR operation.
    
    Args:
        a: First integer
        b: Second integer
        
    Returns:
        int: Result of a XOR b
    """
    return int(a) ^ int(b)


def bitwise_not(a):
    """Perform bitwise NOT operation.
    
    Args:
        a: Integer to negate
        
    Returns:
        int: Result of NOT a
    """
    return ~int(a)


def left_shift(a, n):
    """Perform left shift operation.
    
    Args:
        a: Integer to shift
        n: Number of positions to shift
        
    Returns:
        int: Result of a << n
    """
    return int(a) << int(n)


def right_shift(a, n):
    """Perform right shift operation.
    
    Args:
        a: Integer to shift
        n: Number of positions to shift
        
    Returns:
        int: Result of a >> n
    """
    return int(a) >> int(n)


def convert_base(value, from_base, to_base):
    """Convert a number from one base to another.
    
    Args:
        value: String representation of the number
        from_base: Source base (2, 8, 10, or 16)
        to_base: Target base (2, 8, 10, or 16)
        
    Returns:
        str: Number in target base
    """
    # First convert to decimal
    if from_base == 2:
        decimal = from_binary(value)
    elif from_base == 8:
        decimal = from_octal(value)
    elif from_base == 10:
        decimal = int(value)
    elif from_base == 16:
        decimal = from_hexadecimal(value)
    else:
        raise ValueError(f"Unsupported base: {from_base}")
    
    # Then convert to target base
    if to_base == 2:
        return to_binary(decimal)
    elif to_base == 8:
        return to_octal(decimal)
    elif to_base == 10:
        return str(decimal)
    elif to_base == 16:
        return to_hexadecimal(decimal)
    else:
        raise ValueError(f"Unsupported base: {to_base}")

