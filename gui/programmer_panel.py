"""Programmer calculator button panel."""

from PySide6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QLabel
from PySide6.QtCore import Signal
from gui.buttons import FunctionButton, OperatorButton


class ProgrammerPanel(QWidget):
    """Panel with programmer calculator buttons and base displays."""
    
    # Signals
    bitwise_clicked = Signal(str)
    base_conversion_clicked = Signal(int)
    
    def __init__(self, parent=None):
        """Initialize programmer panel."""
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the programmer button panel."""
        main_layout = QVBoxLayout()
        main_layout.setSpacing(5)
        self.setLayout(main_layout)
        
        # Base display section
        self.create_base_displays(main_layout)
        
        # Button grid
        button_layout = QGridLayout()
        button_layout.setSpacing(5)
        main_layout.addLayout(button_layout)
        
        # Define programmer buttons
        buttons = [
            [('BIN', 'base'), ('OCT', 'base'), ('DEC', 'base'), ('HEX', 'base')],
            [('AND', 'bit'), ('OR', 'bit'), ('XOR', 'bit'), ('NOT', 'bit')],
            [('<<', 'bit'), ('>>', 'bit'), ('', ''), ('', '')],
        ]
        
        # Create and place buttons
        for row, button_row in enumerate(buttons):
            for col, (text, btn_type) in enumerate(button_row):
                if not text:  # Skip empty cells
                    continue
                    
                if btn_type == 'base':
                    button = OperatorButton(text)
                    base_map = {'BIN': 2, 'OCT': 8, 'DEC': 10, 'HEX': 16}
                    base = base_map.get(text, 10)
                    button.clicked.connect(
                        lambda checked, b=base: self.base_conversion_clicked.emit(b)
                    )
                elif btn_type == 'bit':
                    button = FunctionButton(text)
                    button.clicked.connect(
                        lambda checked, t=text: self.bitwise_clicked.emit(t)
                    )
                else:
                    continue
                
                button_layout.addWidget(button, row, col)
    
    def create_base_displays(self, layout):
        """Create displays for different number bases."""
        self.bin_label = QLabel("BIN: 0")
        self.oct_label = QLabel("OCT: 0")
        self.hex_label = QLabel("HEX: 0")
        
        style = """
            QLabel {
                background-color: #2c3e50;
                color: #ecf0f1;
                padding: 5px;
                border-radius: 3px;
                font-family: monospace;
                font-size: 12px;
            }
        """
        
        self.bin_label.setStyleSheet(style)
        self.oct_label.setStyleSheet(style)
        self.hex_label.setStyleSheet(style)
        
        layout.addWidget(self.bin_label)
        layout.addWidget(self.oct_label)
        layout.addWidget(self.hex_label)
    
    def update_base_displays(self, decimal_value):
        """Update the base conversion displays.
        
        Args:
            decimal_value: Decimal value to display in different bases
        """
        try:
            value = int(float(decimal_value))
            self.bin_label.setText(f"BIN: {bin(value)}")
            self.oct_label.setText(f"OCT: {oct(value)}")
            self.hex_label.setText(f"HEX: {hex(value).upper()}")
        except (ValueError, OverflowError):
            self.bin_label.setText("BIN: Error")
            self.oct_label.setText("OCT: Error")
            self.hex_label.setText("HEX: Error")

