"""Display widget for the calculator."""

from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


class Display(QLineEdit):
    """Calculator display widget."""
    
    def __init__(self, parent=None):
        """Initialize the display."""
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the display UI."""
        self.setReadOnly(True)
        self.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.setFixedHeight(80)
        self.setText("0")
        
        # Style the display
        font = QFont("Arial", 24, QFont.Bold)
        self.setFont(font)
        
        self.setStyleSheet("""
            QLineEdit {
                background-color: #f0f0f0;
                border: 2px solid #cccccc;
                border-radius: 8px;
                padding: 10px;
                color: #333333;
            }
        """)
    
    def get_value(self):
        """Get the current display value."""
        return self.text()
    
    def set_value(self, value):
        """Set the display value."""
        if isinstance(value, float):
            # Format float values nicely
            if value.is_integer():
                self.setText(str(int(value)))
            else:
                self.setText(f"{value:.8g}")
        else:
            self.setText(str(value))
    
    def clear_display(self):
        """Clear the display."""
        self.setText("0")
    
    def append_digit(self, digit):
        """Append a digit to the display."""
        current = self.text()
        if current == "0":
            self.setText(str(digit))
        else:
            self.setText(current + str(digit))
    
    def append_decimal(self):
        """Append decimal point if not already present."""
        current = self.text()
        if '.' not in current:
            self.setText(current + '.')

