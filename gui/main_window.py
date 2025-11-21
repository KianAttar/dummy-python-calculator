"""Main window for the calculator GUI."""

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
import sys
from gui.display import Display
from gui.buttons import ButtonGrid
from gui.calculator_logic import CalculatorLogic


class CalculatorWindow(QMainWindow):
    """Main calculator window."""
    
    def __init__(self):
        """Initialize the calculator window."""
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(420, 650)
        
        # Initialize calculator logic
        self.calc_logic = CalculatorLogic()
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create main layout
        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)
        central_widget.setLayout(layout)
        
        # Setup UI components
        self.setup_ui(layout)
        self.connect_signals()
    
    def setup_ui(self, layout):
        """Setup the user interface."""
        # Create display
        self.display = Display()
        layout.addWidget(self.display)
        
        # Create button grid
        self.button_grid = ButtonGrid()
        layout.addWidget(self.button_grid)
    
    def connect_signals(self):
        """Connect button signals to handlers."""
        self.button_grid.digit_clicked.connect(self.on_digit_clicked)
        self.button_grid.operator_clicked.connect(self.on_operator_clicked)
        self.button_grid.function_clicked.connect(self.on_function_clicked)
    
    def on_digit_clicked(self, digit):
        """Handle digit button clicks."""
        if digit == '.':
            result = self.calc_logic.handle_decimal()
        else:
            result = self.calc_logic.handle_digit(digit)
        self.display.set_value(result)
    
    def on_operator_clicked(self, operator):
        """Handle operator button clicks."""
        result = self.calc_logic.handle_operator(operator)
        self.display.set_value(result)
    
    def on_function_clicked(self, function):
        """Handle function button clicks."""
        if function == 'C':
            result = self.calc_logic.handle_clear()
            self.display.set_value(result)
        elif function == '⌫':
            result = self.calc_logic.handle_backspace()
            self.display.set_value(result)
        elif function == '±':
            result = self.calc_logic.handle_sign_change()
            self.display.set_value(result)
        elif function == '%':
            result = self.calc_logic.handle_percent()
            self.display.set_value(result)


def run_gui():
    """Run the calculator GUI application."""
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run_gui()

