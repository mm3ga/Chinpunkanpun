from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
from screens import MainMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chinpunkanpun")

        self.setWindowFlags(
            Qt.Dialog
            | Qt.WindowTitleHint
            | Qt.WindowCloseButtonHint
        )

        self.setFixedSize(1000, 700)

        self.main_menu = MainMenu()
        self.setCentralWidget(self.main_menu)
