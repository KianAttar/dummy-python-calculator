"""Calculator logic handler for GUI."""

from calculator import Calculator
from calculator.scientific import (
    sin, cos, tan, asin, acos, atan,
    log, ln, exp, power, sqrt, cbrt, factorial,
    PI, E
)
from calculator.programmer import (
    to_binary, to_octal, to_hexadecimal,
    from_binary, from_octal, from_hexadecimal,
    bitwise_and, bitwise_or, bitwise_xor, bitwise_not,
    left_shift, right_shift
)


class CalculatorLogic:
    """Handles calculator logic for the GUI."""
    
    def __init__(self):
        """Initialize calculator logic."""
        self.calculator = Calculator()
        self.current_input = ""
        self.waiting_for_operand = False
        self.pending_operator = None
        self.pending_value = None
    
    def handle_digit(self, digit):
        """Handle digit input.
        
        Args:
            digit: The digit to add
            
        Returns:
            str: The updated display value
        """
        if self.waiting_for_operand:
            self.current_input = digit
            self.waiting_for_operand = False
        else:
            if self.current_input == "0":
                self.current_input = digit
            else:
                self.current_input += digit
        return self.current_input
    
    def handle_decimal(self):
        """Handle decimal point input.
        
        Returns:
            str: The updated display value
        """
        if self.waiting_for_operand:
            self.current_input = "0."
            self.waiting_for_operand = False
        elif '.' not in self.current_input:
            self.current_input += '.'
        return self.current_input
    
    def handle_operator(self, operator):
        """Handle operator input.
        
        Args:
            operator: The operator (+, -, ×, ÷, =)
            
        Returns:
            str: The result to display
        """
        try:
            current_value = float(self.current_input) if self.current_input else 0
        except ValueError:
            return "Error"
        
        if self.pending_operator and not self.waiting_for_operand:
            # Perform pending operation
            result = self.perform_operation(self.pending_value, current_value, self.pending_operator)
            self.calculator.set_value(result)
            self.current_input = str(result)
        else:
            self.calculator.set_value(current_value)
        
        if operator == '=':
            self.pending_operator = None
            self.pending_value = None
            self.waiting_for_operand = True
        else:
            self.pending_operator = operator
            self.pending_value = float(self.current_input)
            self.waiting_for_operand = True
        
        return self.current_input
    
    def perform_operation(self, left, right, operator):
        """Perform a calculation.
        
        Args:
            left: Left operand
            right: Right operand
            operator: Operator to apply
            
        Returns:
            float: Result of operation
        """
        self.calculator.set_value(left)
        
        try:
            if operator == '+':
                result = self.calculator.add(right)
            elif operator == '-':
                result = self.calculator.subtract(right)
            elif operator == '×' or operator == '*':
                result = self.calculator.multiply(right)
            elif operator == '÷' or operator == '/':
                result = self.calculator.divide(right)
            else:
                return left
            
            # Format result nicely
            if isinstance(result, float) and result.is_integer():
                return int(result)
            return result
        except (ValueError, ZeroDivisionError):
            return "Error"
    
    def handle_clear(self):
        """Handle clear operation.
        
        Returns:
            str: The cleared display value
        """
        self.current_input = "0"
        self.waiting_for_operand = False
        self.pending_operator = None
        self.pending_value = None
        self.calculator.clear()
        return self.current_input
    
    def handle_backspace(self):
        """Handle backspace operation.
        
        Returns:
            str: The updated display value
        """
        if len(self.current_input) > 1:
            self.current_input = self.current_input[:-1]
        else:
            self.current_input = "0"
        return self.current_input
    
    def handle_sign_change(self):
        """Handle sign change (+/-).
        
        Returns:
            str: The updated display value
        """
        try:
            value = float(self.current_input)
            value = -value
            self.current_input = str(value)
        except ValueError:
            pass
        return self.current_input
    
    def handle_percent(self):
        """Handle percent operation.
        
        Returns:
            str: The updated display value
        """
        try:
            value = float(self.current_input)
            value = value / 100
            self.current_input = str(value)
        except ValueError:
            pass
        return self.current_input
    
    def get_history(self):
        """Get calculation history.
        
        Returns:
            list: History of calculations
        """
        return self.calculator.get_history()
    
    def handle_scientific_function(self, func_name):
        """Handle scientific function.
        
        Args:
            func_name: Name of the scientific function
            
        Returns:
            str: The result to display
        """
        try:
            value = float(self.current_input) if self.current_input else 0
            
            if func_name == 'sin':
                result = sin(value)
            elif func_name == 'cos':
                result = cos(value)
            elif func_name == 'tan':
                result = tan(value)
            elif func_name == 'asin':
                result = asin(value)
            elif func_name == 'acos':
                result = acos(value)
            elif func_name == 'atan':
                result = atan(value)
            elif func_name == 'log':
                result = log(value)
            elif func_name == 'ln':
                result = ln(value)
            elif func_name == 'exp':
                result = exp(value)
            elif func_name == 'sqrt':
                result = sqrt(value)
            elif func_name == 'cbrt':
                result = cbrt(value)
            elif func_name == 'x²':
                result = power(value, 2)
            elif func_name == 'x³':
                result = power(value, 3)
            elif func_name == '1/x':
                result = 1 / value
            elif func_name == 'π':
                result = PI
                self.waiting_for_operand = False
            elif func_name == 'e':
                result = E
                self.waiting_for_operand = False
            elif func_name == 'n!':
                result = factorial(value)
            else:
                return self.current_input
            
            # Format result
            if isinstance(result, float) and result.is_integer():
                self.current_input = str(int(result))
            else:
                self.current_input = f"{result:.10g}"
            
            self.waiting_for_operand = True
            return self.current_input
            
        except (ValueError, ZeroDivisionError, OverflowError) as e:
            return "Error"
    
    def handle_base_conversion(self, target_base):
        """Handle base conversion.
        
        Args:
            target_base: Target base (2, 8, 10, 16)
            
        Returns:
            str: The converted value
        """
        try:
            # Assume current input is in decimal
            value = int(float(self.current_input))
            
            if target_base == 2:
                result = to_binary(value)
                self.current_input = result
            elif target_base == 8:
                result = to_octal(value)
                self.current_input = result
            elif target_base == 16:
                result = to_hexadecimal(value)
                self.current_input = result
            else:
                result = str(value)
                self.current_input = result
            
            return self.current_input
        except (ValueError, OverflowError) as e:
            return "Error"
    
    def handle_bitwise_operation(self, operation, operand=None):
        """Handle bitwise operations.
        
        Args:
            operation: The bitwise operation (AND, OR, XOR, NOT, <<, >>)
            operand: The second operand (if needed)
            
        Returns:
            str: The result to display
        """
        try:
            value = int(float(self.current_input)) if self.current_input else 0
            
            if operation == 'NOT':
                result = bitwise_not(value)
            elif operand is not None:
                if operation == 'AND':
                    result = bitwise_and(value, operand)
                elif operation == 'OR':
                    result = bitwise_or(value, operand)
                elif operation == 'XOR':
                    result = bitwise_xor(value, operand)
                elif operation == '<<':
                    result = left_shift(value, operand)
                elif operation == '>>':
                    result = right_shift(value, operand)
                else:
                    return self.current_input
            else:
                return self.current_input
            
            self.current_input = str(result)
            self.waiting_for_operand = True
            return self.current_input
            
        except (ValueError, OverflowError) as e:
            return "Error"

