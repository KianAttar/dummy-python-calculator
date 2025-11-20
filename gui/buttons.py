"""Button widgets and layouts for the calculator."""

from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QFont


class CalculatorButton(QPushButton):
    """Custom button for calculator."""
    
    def __init__(self, text, parent=None):
        """Initialize button."""
        super().__init__(text, parent)
        self.setup_ui()
    
    def setup_ui(self):
        """Setup button appearance."""
        font = QFont("Arial", 14, QFont.Bold)
        self.setFont(font)
        self.setMinimumSize(80, 60)
        
        self.setStyleSheet("""
            QPushButton {
                background-color: #e0e0e0;
                border: 2px solid #cccccc;
                border-radius: 8px;
                padding: 10px;
                color: #333333;
            }
            QPushButton:hover {
                background-color: #d0d0d0;
            }
            QPushButton:pressed {
                background-color: #c0c0c0;
            }
        """)


class OperatorButton(CalculatorButton):
    """Button for operators."""
    
    def setup_ui(self):
        """Setup operator button appearance."""
        super().setup_ui()
        self.setStyleSheet("""
            QPushButton {
                background-color: #ff9500;
                border: 2px solid #e08500;
                border-radius: 8px;
                padding: 10px;
                color: white;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #e08500;
            }
            QPushButton:pressed {
                background-color: #c07500;
            }
        """)


class FunctionButton(CalculatorButton):
    """Button for functions."""
    
    def setup_ui(self):
        """Setup function button appearance."""
        super().setup_ui()
        self.setStyleSheet("""
            QPushButton {
                background-color: #505050;
                border: 2px solid #404040;
                border-radius: 8px;
                padding: 10px;
                color: white;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #606060;
            }
            QPushButton:pressed {
                background-color: #404040;
            }
        """)


class ButtonGrid(QWidget):
    """Grid of calculator buttons."""
    
    # Signals for button clicks
    digit_clicked = Signal(str)
    operator_clicked = Signal(str)
    function_clicked = Signal(str)
    
    def __init__(self, parent=None):
        """Initialize button grid."""
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the button grid."""
        layout = QGridLayout()
        layout.setSpacing(5)
        self.setLayout(layout)
        
        # Define button layout
        buttons = [
            [('C', 'func'), ('±', 'func'), ('%', 'func'), ('÷', 'op')],
            [('7', 'num'), ('8', 'num'), ('9', 'num'), ('×', 'op')],
            [('4', 'num'), ('5', 'num'), ('6', 'num'), ('-', 'op')],
            [('1', 'num'), ('2', 'num'), ('3', 'num'), ('+', 'op')],
            [('0', 'num'), ('.', 'num'), ('⌫', 'func'), ('=', 'op')],
        ]
        
        # Create and place buttons
        for row, button_row in enumerate(buttons):
            for col, (text, btn_type) in enumerate(button_row):
                if btn_type == 'num':
                    button = CalculatorButton(text)
                    button.clicked.connect(lambda checked, t=text: self.digit_clicked.emit(t))
                elif btn_type == 'op':
                    button = OperatorButton(text)
                    button.clicked.connect(lambda checked, t=text: self.operator_clicked.emit(t))
                else:  # func
                    button = FunctionButton(text)
                    button.clicked.connect(lambda checked, t=text: self.function_clicked.emit(t))
                
                layout.addWidget(button, row, col)

