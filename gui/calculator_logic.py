"""Calculator logic handler for GUI."""

from calculator import Calculator


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
        
        if operator == '+':
            return self.calculator.add(right)
        elif operator == '-':
            return self.calculator.subtract(right)
        elif operator == '×' or operator == '*':
            return self.calculator.multiply(right)
        elif operator == '÷' or operator == '/':
            try:
                return self.calculator.divide(right)
            except ValueError:
                return "Error"
        return left
    
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

