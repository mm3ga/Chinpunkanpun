import sys
from PySide6.QtWidgets import QApplication
from window import MainWindow

#Create QT Application
app = QApplication(sys.argv)

# Create the window
window = MainWindow()

#Show Everything
window.show()

sys.exit(app.exec())
