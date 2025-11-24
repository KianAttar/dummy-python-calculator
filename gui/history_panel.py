"""History panel for displaying calculation history."""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QListWidget, 
    QPushButton, QLabel, QHBoxLayout
)
from PySide6.QtCore import Signal


class HistoryPanel(QWidget):
    """Panel displaying calculation history."""
    
    # Signal for when history item is clicked
    history_item_clicked = Signal(str)
    
    def __init__(self, parent=None):
        """Initialize history panel."""
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the history panel UI."""
        layout = QVBoxLayout()
        layout.setSpacing(5)
        self.setLayout(layout)
        
        # Title
        title = QLabel("History")
        title.setStyleSheet("""
            QLabel {
                font-size: 14px;
                font-weight: bold;
                color: #333;
                padding: 5px;
            }
        """)
        layout.addWidget(title)
        
        # History list
        self.history_list = QListWidget()
        self.history_list.setStyleSheet("""
            QListWidget {
                background-color: #f9f9f9;
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 5px;
                font-family: monospace;
            }
            QListWidget::item {
                padding: 5px;
                border-bottom: 1px solid #eee;
            }
            QListWidget::item:hover {
                background-color: #e8e8e8;
            }
        """)
        self.history_list.itemClicked.connect(self.on_item_clicked)
        layout.addWidget(self.history_list)
        
        # Clear button
        clear_button = QPushButton("Clear History")
        clear_button.clicked.connect(self.clear_history)
        clear_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                border: none;
                padding: 8px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #da190b;
            }
        """)
        layout.addWidget(clear_button)
    
    def add_history_item(self, item):
        """Add an item to the history.
        
        Args:
            item: History item string
        """
        self.history_list.addItem(item)
        # Auto-scroll to bottom
        self.history_list.scrollToBottom()
    
    def clear_history(self):
        """Clear all history items."""
        self.history_list.clear()
    
    def on_item_clicked(self, item):
        """Handle history item click.
        
        Args:
            item: Clicked list item
        """
        # Extract the result value from history item
        text = item.text()
        if '=' in text:
            result = text.split('=')[-1].strip()
            self.history_item_clicked.emit(result)
    
    def get_history(self):
        """Get all history items.
        
        Returns:
            list: List of history item strings
        """
        return [
            self.history_list.item(i).text()
            for i in range(self.history_list.count())
        ]

