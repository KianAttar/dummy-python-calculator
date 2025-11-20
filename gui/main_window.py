"""Main window for the calculator GUI."""

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
import sys
from gui.display import Display
from gui.buttons import ButtonGrid


class CalculatorWindow(QMainWindow):
    """Main calculator window."""
    
    def __init__(self):
        """Initialize the calculator window."""
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(420, 650)
        
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
    
    def setup_ui(self, layout):
        """Setup the user interface."""
        # Create display
        self.display = Display()
        layout.addWidget(self.display)
        
        # Create button grid
        self.button_grid = ButtonGrid()
        layout.addWidget(self.button_grid)
        
        # Placeholder for signal connections - will be implemented next
        # self.connect_signals()


def run_gui():
    """Run the calculator GUI application."""
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run_gui()

