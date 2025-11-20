"""Main window for the calculator GUI."""

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import Qt
import sys


class CalculatorWindow(QMainWindow):
    """Main calculator window."""
    
    def __init__(self):
        """Initialize the calculator window."""
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFixedSize(400, 600)
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create main layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Placeholder for now
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface."""
        # Will be implemented in next commits
        pass


def run_gui():
    """Run the calculator GUI application."""
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run_gui()

