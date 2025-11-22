"""Scientific calculator button panel."""

from PySide6.QtWidgets import QWidget, QGridLayout
from PySide6.QtCore import Signal
from gui.buttons import FunctionButton


class ScientificPanel(QWidget):
    """Panel with scientific calculator buttons."""
    
    # Signal for scientific function clicks
    scientific_clicked = Signal(str)
    
    def __init__(self, parent=None):
        """Initialize scientific panel."""
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the scientific button panel."""
        layout = QGridLayout()
        layout.setSpacing(5)
        self.setLayout(layout)
        
        # Define scientific buttons
        buttons = [
            ['sin', 'cos', 'tan', 'π'],
            ['asin', 'acos', 'atan', 'e'],
            ['log', 'ln', 'exp', 'n!'],
            ['√', '∛', 'x²', 'x³'],
        ]
        
        # Create and place buttons
        for row, button_row in enumerate(buttons):
            for col, text in enumerate(button_row):
                button = FunctionButton(text)
                
                # Map button text to function names
                func_map = {
                    'sin': 'sin', 'cos': 'cos', 'tan': 'tan',
                    'asin': 'asin', 'acos': 'acos', 'atan': 'atan',
                    'log': 'log', 'ln': 'ln', 'exp': 'exp',
                    '√': 'sqrt', '∛': 'cbrt',
                    'x²': 'x²', 'x³': 'x³',
                    'π': 'π', 'e': 'e', 'n!': 'n!'
                }
                
                func_name = func_map.get(text, text)
                button.clicked.connect(
                    lambda checked, f=func_name: self.scientific_clicked.emit(f)
                )
                
                layout.addWidget(button, row, col)

