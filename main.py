import sys
from beginner import Bbuttonlogic
from window import MainWindow
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)

#Create QT Application
app = QApplication(sys.argv)

# Create the window
window = MainWindow()

#Show Everything
window.show()

sys.exit(app.exec())
