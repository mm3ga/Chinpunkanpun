from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QHBoxLayout,
    QSizePolicy,
)
from PySide6.QtCore import Qt


class MainMenu(QWidget):
    def __init__(self):
        super().__init__()

        # =========================
        # Widgets
        # =========================
        self.setObjectName("mainMenu")
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.title = QLabel("🌸 Chinpunkanpun 🌸")
        self.title.setObjectName("title")

        self.subtitle = QLabel("Kawaii Nihongo!")
        self.subtitle.setObjectName("subtitle")

        self.beginner_button = QPushButton("Beginner")
        self.intermediate_button = QPushButton("Intermediate")
        self.master_button = QPushButton("Master")

        self.settings_button = QPushButton("⚙ Settings")
        self.extras_button = QPushButton("✦ Extras")

        self.beginner_button.setObjectName("modeButton")
        self.intermediate_button.setObjectName("modeButton")
        self.master_button.setObjectName("modeButton")

        self.settings_button.setObjectName("utilityButton")
        self.extras_button.setObjectName("utilityButton")

        # Don't let title/subtitle become gigantic vertical rectangles
        self.title.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Maximum
        )

        self.subtitle.setSizePolicy(
            QSizePolicy.Preferred,
            QSizePolicy.Maximum
        )

        # Keep main mode buttons from stretching across the universe
        self.beginner_button.setFixedWidth(220)
        self.intermediate_button.setFixedWidth(220)
        self.master_button.setFixedWidth(220)

        # =========================
        # Layouts
        # =========================

        main_layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        button_layout = QHBoxLayout()

        # Top utility buttons
        top_layout.addWidget(self.settings_button)
        top_layout.addStretch()
        top_layout.addWidget(self.extras_button)

        # Main mode buttons
        button_layout.addStretch()
        button_layout.addWidget(self.beginner_button)
        button_layout.addWidget(self.intermediate_button)
        button_layout.addWidget(self.master_button)
        button_layout.addStretch()

        button_layout.setSpacing(18)

        # Assemble main screen
        main_layout.addLayout(top_layout)

        # Push title slightly south from the top utility bar
        main_layout.addSpacing(55)

        main_layout.addWidget(
            self.title,
            alignment=Qt.AlignHCenter
        )

        main_layout.addWidget(
            self.subtitle,
            alignment=Qt.AlignHCenter
        )

        # Gap between subtitle and mode buttons
        main_layout.addSpacing(55)

        main_layout.addLayout(button_layout)

        # Everything else becomes breathing room underneath
        main_layout.addStretch()

        main_layout.setContentsMargins(40, 30, 40, 30)
        main_layout.setSpacing(10)

        self.setLayout(main_layout)

        # =========================
        # Styling
        # =========================

        self.setStyleSheet("""
            QWidget#mainMenu {
                background-color: #ffe1f5;
            }

            QWidget {
                color: #402c3a;
                font-family: Sans Serif;
            }

            QLabel#title {
                font-size: 48px;
                font-weight: 800;
                color: #48283a;
                background: transparent;
            }

            QLabel#subtitle {
                font-size: 22px;
                font-weight: 500;
                color: #bd4f82;
                background: transparent;
            }

            QPushButton#modeButton {
                background-color: #fff1f6;
                color: #7a3f5c;

                border: 2px solid #f04f98;
                border-radius: 16px;

                padding: 14px 22px;

                font-size: 18px;
                font-weight: 500;
            }

            QPushButton#modeButton:hover {
                background-color: #fff0f7;
                border-color: #d93682;
            }

            QPushButton#modeButton:pressed {
                background-color: #ffdce9;
            }

            QPushButton#utilityButton {
                background-color: #fff1f6;
                color: #613b50;

                border: 2px solid #f04f98;
                border-radius: 14px;

                padding: 10px 18px;

                font-size: 16px;
                font-weight: 500;
            }

            QPushButton#utilityButton:hover {
                background-color: #fff0f7;
                border-color: #d93682;
            }
        """)



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
        self.study_help_button: QPushButton = QPushButton("Study Help")

        #Create layouts
        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        #Add widgets
        main_layout.addWidget(self.passage_box)
        main_layout.addLayout(button_layout)
        button_layout.addWidget(self.new_passage_button)
        button_layout.addWidget(self.translate_button)
        button_layout.addWidget(self.back_button)
        button_layout.addWidget(self.study_help_button)

        self.setLayout(main_layout)

class BeginnerMenu(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.practice_button = QPushButton("Practice")
        self.kana_button = QPushButton("Kana Help")
        self.back_button = QPushButton("Back")

        layout.addWidget(self.practice_button)
        layout.addWidget(self.kana_button)
        layout.addWidget(self.back_button)


        self.setLayout(layout)

class KanaHelpScreen(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.kana_help = QPushButton("Kana Help")

        self.hiragana = "I display HIRAGANA"
        self.katakana = "I display KATAKANA"

        self.back_button = QPushButton("Back")

        layout.addWidget(self.back_button)

        self.setLayout(layout)
