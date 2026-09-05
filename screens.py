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

         #Layouts
         button_layout = QHBoxLayout()
         main_layout = QVBoxLayout()

         # widgets for layouts
         button_layout.addWidget(self.beginner_button)
         button_layout.addWidget(self.intermediate_button)
         button_layout.addWidget(self.master_button)
         main_layout.addWidget(self.title)
         main_layout.addLayout(button_layout)

         self.setLayout(main_layout)



class PracticeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.passage_box = QTextEdit()
        self.passage_box.setMinimumHeight(300)
        self.passage_box.setReadOnly(True)
        self.passage_box.setPlaceholderText("Your Japanese passage will appear here...")

        self.new_passage_button = QPushButton("New Passage")
        self.translate_button = QPushButton("Translate")
        self.back_button: QPushButton = QPushButton("Back")

        #Create layouts
        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        #Add widgets
        main_layout.addWidget(self.passage_box)
        main_layout.addLayout(button_layout)
        button_layout.addWidget(self.new_passage_button)
        button_layout.addWidget(self.translate_button)
        button_layout.addWidget(self.back_button)

        self.setLayout(main_layout)
