print("LOADING SCREENS FROM:", __file__)
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QHBoxLayout,
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
         #self.beginner_button.clicked.connect(self.handle_beginner)

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

class PracticeScreen(QWidget):
    def __init__(self):
        super().__init__()
        #passage_box = QTextEdit()
        #passage_box.setReadOnly(True)
        #passage_box.setPlaceholderText("Your Japanese passage will appear here...")
        print("PRACTICE SCREEN CREATED")

        new_passage_button = QPushButton("New Passage")
        translate_button = QPushButton("Translate")
        self.back_button: QPushButton = QPushButton("Back")
        self.back_button.clicked.connect(lambda: print("LOCAL BACK WORKS"))

        #Create layouts
        top_layout = QHBoxLayout()
        top_layout.addWidget(new_passage_button)
        top_layout.addWidget(translate_button)
        top_layout.addWidget(self.back_button)
        self.setLayout(top_layout)
