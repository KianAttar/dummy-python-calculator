"""Main window for the calculator GUI."""

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, 
    QVBoxLayout, QHBoxLayout, QPushButton
)
from PySide6.QtCore import Qt
import sys
from gui.display import Display
from gui.buttons import ButtonGrid
from gui.calculator_logic import CalculatorLogic
from gui.scientific_panel import ScientificPanel


class CalculatorWindow(QMainWindow):
    """Main calculator window."""
    
    def __init__(self):
        """Initialize the calculator window."""
        super().__init__()
        self.setWindowTitle("Calculator")
        
        # Initialize calculator logic
        self.calc_logic = CalculatorLogic()
        
        # Mode state
        self.scientific_mode = False
        
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
        
        # Set initial size
        self.adjustSize()
    
    def setup_ui(self, layout):
        """Setup the user interface."""
        # Create mode toggle button
        self.mode_button = QPushButton("Scientific Mode")
        self.mode_button.setCheckable(True)
        self.mode_button.clicked.connect(self.toggle_mode)
        self.mode_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 8px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:checked {
                background-color: #2196F3;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        layout.addWidget(self.mode_button)
        
        # Create display
        self.display = Display()
        layout.addWidget(self.display)
        
        # Create scientific panel (hidden by default)
        self.scientific_panel = ScientificPanel()
        self.scientific_panel.setVisible(False)
        layout.addWidget(self.scientific_panel)
        
        # Create button grid
        self.button_grid = ButtonGrid()
        layout.addWidget(self.button_grid)
    
    def connect_signals(self):
        """Connect button signals to handlers."""
        self.button_grid.digit_clicked.connect(self.on_digit_clicked)
        self.button_grid.operator_clicked.connect(self.on_operator_clicked)
        self.button_grid.function_clicked.connect(self.on_function_clicked)
        self.scientific_panel.scientific_clicked.connect(self.on_scientific_clicked)
    
    def toggle_mode(self):
        """Toggle between basic and scientific modes."""
        self.scientific_mode = not self.scientific_mode
        self.scientific_panel.setVisible(self.scientific_mode)
        
        if self.scientific_mode:
            self.mode_button.setText("Basic Mode")
        else:
            self.mode_button.setText("Scientific Mode")
        
        # Adjust window size
        self.adjustSize()
    
    def on_scientific_clicked(self, function):
        """Handle scientific function button clicks."""
        result = self.calc_logic.handle_scientific_function(function)
        self.display.set_value(result)
    
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
    
    def keyPressEvent(self, event):
        """Handle keyboard input."""
        key = event.text()
        
        # Handle digits
        if key.isdigit():
            self.on_digit_clicked(key)
        # Handle decimal
        elif key == '.':
            self.on_digit_clicked('.')
        # Handle operators
        elif key == '+':
            self.on_operator_clicked('+')
        elif key == '-':
            self.on_operator_clicked('-')
        elif key == '*':
            self.on_operator_clicked('×')
        elif key == '/':
            self.on_operator_clicked('÷')
        elif key in ('=', '\r', '\n'):  # Enter key
            self.on_operator_clicked('=')
        # Handle functions
        elif key.lower() == 'c':
            self.on_function_clicked('C')
        elif event.key() == Qt.Key_Backspace:
            self.on_function_clicked('⌫')
        elif event.key() == Qt.Key_Escape:
            self.on_function_clicked('C')
        elif key == '%':
            self.on_function_clicked('%')
        else:
            super().keyPressEvent(event)


def run_gui():
    """Run the calculator GUI application."""
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run_gui()

