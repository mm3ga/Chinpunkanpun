from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QApplication,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)


class MainMenu(QWidget):
    def __init__(self):
         super().__init__()

         #widgets
         self.title: QLabel = QLabel("🌸 Chinpunkanpun: Kawaii Nihongo! 🌸")
         self.title.setStyleSheet("font-size: 30px; font-weight: bold;")
         self.beginner_button: QPushButton = QPushButton("Beginner Button")
         self.intermediate_button: QPushButton = QPushButton("Intermediate Button")
         self.master_button: QPushButton = QPushButton("Master Button")

         #buttons
         self.beginner_button.clicked.connect(self.handle_beginner)

         #Layouts
         bottom_layout = QHBoxLayout()
         main_layout = QVBoxLayout()

         # widgets for layouts
         bottom_layout.addWidget(self.beginner_button)
         bottom_layout.addWidget(self.intermediate_button)
         bottom_layout.addWidget(self.master_button)
         main_layout.addWidget(self.title)

         main_layout.addLayout(bottom_layout)

         self.setLayout(main_layout)

    #functions
    def handle_beginner(self):
        print("beginner clicker")
        #Bstore = Bbuttonlogic()
        #passage_box.setPlainText(Bstore)
