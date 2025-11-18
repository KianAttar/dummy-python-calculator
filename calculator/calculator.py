"""Calculator class for managing calculation state and operations."""

from calculator.operations import add, subtract, multiply, divide


class Calculator:
    """Basic calculator with operation history."""
    
    def __init__(self):
        """Initialize calculator with empty state."""
        self.current_value = 0
        self.history = []
    
    def add(self, value):
        """Add value to current value."""
        self.current_value = add(self.current_value, value)
        self.history.append(f"+ {value} = {self.current_value}")
        return self.current_value
    
    def subtract(self, value):
        """Subtract value from current value."""
        self.current_value = subtract(self.current_value, value)
        self.history.append(f"- {value} = {self.current_value}")
        return self.current_value
    
    def multiply(self, value):
        """Multiply current value by value."""
        self.current_value = multiply(self.current_value, value)
        self.history.append(f"× {value} = {self.current_value}")
        return self.current_value
    
    def divide(self, value):
        """Divide current value by value."""
        self.current_value = divide(self.current_value, value)
        self.history.append(f"÷ {value} = {self.current_value}")
        return self.current_value
    
    def clear(self):
        """Clear current value and history."""
        self.current_value = 0
        self.history = []
    
    def get_value(self):
        """Get current value."""
        return self.current_value
    
    def set_value(self, value):
        """Set current value."""
        self.current_value = value
    
    def get_history(self):
        """Get calculation history."""
        return self.history

