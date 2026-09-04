from PySide6.QtWidgets import QMainWindow, QPushButton, QStackedWidget
from PySide6.QtCore import Qt
from screens import MainMenu, PracticeScreen

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
        self.practice_screen = PracticeScreen()
        self.stack = QStackedWidget()
        self.stack.addWidget(self.main_menu)
        self.stack.addWidget(self.practice_screen)
        self.setCentralWidget(self.stack)
        self.main_menu.beginner_button.clicked.connect(self.switch_stack)
        self.practice_screen.back_button.clicked.connect(self.go_back_stack)
        print("MAINWINDOW CONNECTED BACK")
    def switch_stack(self):
        self.stack.setCurrentWidget(self.practice_screen)
    def go_back_stack(self):
        print("BACK BUTTON FIRED")
        self.stack.setCurrentWidget(self.main_menu)
