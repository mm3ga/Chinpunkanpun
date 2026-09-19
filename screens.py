from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QHBoxLayout,
    QSizePolicy,
    QGridLayout,
    QStackedWidget,
    QFrame,
    QScrollArea
)
from PySide6.QtCore import Qt, Signal
from kana_data import KANA_DATA
from topics import TOPICS

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

        self.setObjectName("practiceScreen")
        self.setAttribute(Qt.WA_StyledBackground, True)

        # ==================================================
        # Header widgets
        # ==================================================

        self.back_button = QPushButton("← Back")
        self.back_button.setObjectName("backButton")

        self.mode_label = QLabel("Japanese Practice")
        self.mode_label.setObjectName("modeLabel")

        self.title = QLabel("Practice")
        self.title.setObjectName("practiceTitle")

        self.subtitle = QLabel("Read at your own pace.")
        self.subtitle.setObjectName("practiceSubtitle")

        # ==================================================
        # Passage
        # ==================================================

        self.passage_box = QTextEdit()
        self.passage_box.setObjectName("passageBox")

        # ==================================================
        # Study Help panel
        # ==================================================

        self.study_help_panel = QFrame()
        self.study_help_panel.setObjectName("studyHelpPanel")
        self.study_help_panel.setFixedWidth(300)

        self.study_help_title = QLabel("Study Help")
        self.study_help_title.setObjectName("studyHelpTitle")

        self.study_help_subtitle = QLabel(
            "Readings and meanings"
        )
        self.study_help_subtitle.setObjectName(
            "studyHelpSubtitle"
        )

        self.study_help_scroll = QScrollArea()
        self.study_help_scroll.setObjectName(
            "studyHelpScroll"
        )
        self.study_help_scroll.setWidgetResizable(True)

        self.study_help_content = QWidget()
        self.study_help_content.setObjectName(
            "studyHelpContent"
        )

        self.study_help_layout = QVBoxLayout()
        self.study_help_layout.setSpacing(10)

        self.study_help_layout.setContentsMargins(
            8,
            8,
            8,
            8
        )

        self.study_help_content.setLayout(
            self.study_help_layout
        )

        self.study_help_scroll.setWidget(
            self.study_help_content
        )

        help_panel_layout = QVBoxLayout()

        help_panel_layout.addWidget(
            self.study_help_title
        )

        help_panel_layout.addWidget(
            self.study_help_subtitle
        )

        help_panel_layout.addSpacing(8)

        help_panel_layout.addWidget(
            self.study_help_scroll
        )

        help_panel_layout.setContentsMargins(
            18,
            18,
            18,
            18
        )

        self.study_help_panel.setLayout(
            help_panel_layout
        )

        # Hidden until Study Help is clicked.
        self.study_help_panel.hide()

        # ==================================================
        # Action buttons
        # ==================================================

        self.new_passage_button = QPushButton(
            "New Passage"
        )

        self.study_help_button = QPushButton(
            "Study Help"
        )

        self.translate_button = QPushButton(
            "Translate"
        )

        self.new_passage_button.setObjectName(
            "actionButton"
        )

        self.study_help_button.setObjectName(
            "actionButton"
        )

        self.translate_button.setObjectName(
            "actionButton"
        )

        # ==================================================
        # Top bar
        # ==================================================

        top_layout = QHBoxLayout()

        top_layout.addWidget(
            self.back_button
        )

        top_layout.addStretch()

        top_layout.addWidget(
            self.mode_label
        )

        # ==================================================
        # Reading area
        # ==================================================

        reading_layout = QHBoxLayout()

        reading_layout.addWidget(
            self.passage_box,
            stretch=1
        )

        reading_layout.addWidget(
            self.study_help_panel
        )

        reading_layout.setSpacing(16)

        # ==================================================
        # Action bar
        # ==================================================

        action_layout = QHBoxLayout()

        action_layout.addStretch()

        action_layout.addWidget(
            self.new_passage_button
        )

        action_layout.addWidget(
            self.study_help_button
        )

        action_layout.addWidget(
            self.translate_button
        )

        action_layout.addStretch()

        action_layout.setSpacing(16)

        # ==================================================
        # Main layout
        # ==================================================

        main_layout = QVBoxLayout()

        main_layout.addLayout(
            top_layout
        )

        main_layout.addSpacing(35)

        main_layout.addWidget(
            self.title
        )

        main_layout.addWidget(
            self.subtitle
        )

        main_layout.addSpacing(24)

        main_layout.addLayout(
            reading_layout
        )

        main_layout.addSpacing(22)

        main_layout.addLayout(
            action_layout
        )

        main_layout.addStretch()

        main_layout.setContentsMargins(
            55,
            35,
            55,
            40
        )

        main_layout.setSpacing(7)

        self.setLayout(main_layout)

        # ==================================================
        # Styling
        # ==================================================

        self.setStyleSheet("""
            QWidget#practiceScreen {
                background-color: #ffe1f5;
                color: #4d3845;
                font-family: Sans Serif;
            }

            QLabel {
                background: transparent;
            }

            QLabel#practiceTitle {
                font-size: 38px;
                font-weight: 800;
                color: #563847;
            }

            QLabel#practiceSubtitle {
                font-size: 16px;
                color: #876676;
            }

            QLabel#modeLabel {
                font-size: 15px;
                font-weight: 600;
                color: #b84f7d;
            }

            QTextEdit#passageBox {
                background-color: #fffafd;
                color: #3f3038;

                border: 2px solid #f3a1c4;
                border-radius: 20px;

                padding: 30px;

                font-size: 26px;
            }

            QPushButton#actionButton {
                background-color: #fff1f6;
                color: #7a3f5c;

                border: 2px solid #f04f98;
                border-radius: 14px;

                padding: 11px 22px;

                font-size: 16px;
                font-weight: 600;
            }

            QPushButton#actionButton:hover {
                background-color: #ffddeb;
            }

            QPushButton#actionButton:pressed {
                background-color: #ffcde1;
            }

            QPushButton#backButton {
                background-color: transparent;
                color: #7a3f5c;

                border: none;

                padding: 8px 10px;

                font-size: 16px;
                font-weight: 600;
            }

            QPushButton#backButton:hover {
                color: #d34484;
            }

            QFrame#studyHelpPanel {
                background-color: #fff8fb;

                border: 2px solid #f3a1c4;
                border-radius: 18px;
            }

            QLabel#studyHelpTitle {
                font-size: 22px;
                font-weight: 800;
                color: #563847;
            }

            QLabel#studyHelpSubtitle {
                font-size: 14px;
                color: #987383;
            }

            QScrollArea#studyHelpScroll {
                background: transparent;
                border: none;
            }

            QWidget#studyHelpContent {
                background: transparent;
            }

            QFrame#helpWordCard {
                background-color: #fffdfd;

                border: 1px solid #efb5ce;
                border-radius: 12px;
            }

            QLabel#helpWord {
                font-size: 21px;
                font-weight: 700;
                color: #613b50;
            }

            QLabel#helpReading {
                font-size: 15px;
                color: #c05888;
            }

            QLabel#helpMeaning {
                font-size: 14px;
                color: #725965;
            }

            QLabel#helpEmpty {
                font-size: 14px;
                color: #987383;
            }
        """)

    # ==================================================
    # Study Help
    # ==================================================

    def toggle_study_help(self, help_data):
        if self.study_help_panel.isVisible():
            self.study_help_panel.hide()
            return

        self.populate_study_help(
            help_data
        )

        self.study_help_panel.show()

    def populate_study_help(self, help_data):
        # Remove cards from the previous passage.
        while self.study_help_layout.count():
            layout_item = self.study_help_layout.takeAt(0)

            widget = layout_item.widget()

            if widget is not None:
                widget.deleteLater()

        # Nothing available.
        if not help_data:
            empty_label = QLabel(
                "No study help available."
            )

            empty_label.setObjectName(
                "helpEmpty"
            )

            self.study_help_layout.addWidget(
                empty_label
            )

            self.study_help_layout.addStretch()

            return

        # Create one card per analyzed word.
        for item in help_data:
            card = QFrame()
            card.setObjectName(
                "helpWordCard"
            )

            word = QLabel(
                item["surface"]
            )

            word.setObjectName(
                "helpWord"
            )

            reading = QLabel(
                item["reading"]
            )

            reading.setObjectName(
                "helpReading"
            )

            if item["meaning"]:
                meaning_text = ", ".join(
                    item["meaning"]
                )

            else:
                meaning_text = (
                    "Meaning unavailable"
                )

            meaning = QLabel(
                meaning_text
            )

            meaning.setObjectName(
                "helpMeaning"
            )

            meaning.setWordWrap(True)

            card_layout = QVBoxLayout()

            card_layout.addWidget(
                word
            )

            card_layout.addWidget(
                reading
            )

            card_layout.addSpacing(4)

            card_layout.addWidget(
                meaning
            )

            card_layout.setContentsMargins(
                14,
                12,
                14,
                12
            )

            card.setLayout(
                card_layout
            )

            self.study_help_layout.addWidget(
                card
            )

        self.study_help_layout.addStretch()

class BeginnerMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("beginnerMenu")
        self.setAttribute(Qt.WA_StyledBackground, True)

        # =========================
        # Main widgets
        # =========================

        self.back_button = QPushButton("← Back")
        self.back_button.setObjectName("backButton")

        self.title = QLabel("Beginner")
        self.title.setObjectName("beginnerTitle")

        self.japanese_subtitle = QLabel("ゆっくり、たのしく。")
        self.japanese_subtitle.setObjectName("japaneseSubtitle")

        self.description = QLabel(
            "Build confidence with supported Japanese."
        )
        self.description.setObjectName("description")

        # =========================
        # Practice card
        # =========================

        practice_card = QFrame()
        practice_card.setObjectName("studyCard")

        practice_title = QLabel("Practice")
        practice_title.setObjectName("cardTitle")

        practice_description = QLabel(
            "Read short Japanese passages\n"
            "with study support."
        )
        practice_description.setObjectName("cardDescription")

        self.practice_button = QPushButton("Open →")
        self.practice_button.setObjectName("cardButton")

        practice_layout = QVBoxLayout()
        practice_layout.addWidget(practice_title)
        practice_layout.addSpacing(8)
        practice_layout.addWidget(practice_description)
        practice_layout.addStretch()
        practice_layout.addWidget(self.practice_button)

        practice_layout.setContentsMargins(28, 25, 28, 25)

        practice_card.setLayout(practice_layout)

        # =========================
        # Kana card
        # =========================

        kana_card = QFrame()
        kana_card.setObjectName("studyCard")

        kana_title = QLabel("Kana Help")
        kana_title.setObjectName("cardTitle")

        kana_description = QLabel(
            "Hiragana and Katakana\n"
            "reference and practice."
        )
        kana_description.setObjectName("cardDescription")

        self.kana_button = QPushButton("Open →")
        self.kana_button.setObjectName("cardButton")

        kana_layout = QVBoxLayout()
        kana_layout.addWidget(kana_title)
        kana_layout.addSpacing(8)
        kana_layout.addWidget(kana_description)
        kana_layout.addStretch()
        kana_layout.addWidget(self.kana_button)

        kana_layout.setContentsMargins(28, 25, 28, 25)

        kana_card.setLayout(kana_layout)

        #Topics
        topics_card = QFrame()
        topics_card.setObjectName("topicsCard")

        topics_title = QLabel("Topics")
        topics_title.setObjectName("topicsTitle")

        topics_description = QLabel(
            "Fantasy, Romance, Horror, Comedy, or Random."
        )
        topics_description.setObjectName("topicsDescription")

        self.topics_button = QPushButton("Choose →")
        self.topics_button.setObjectName("topicsButton")

        topics_layout = QHBoxLayout()

        topics_layout.addWidget(topics_title)
        topics_layout.addSpacing(18)
        topics_layout.addWidget(topics_description)

        topics_layout.addStretch()

        topics_layout.addWidget(self.topics_button)

        topics_layout.setContentsMargins(
            26,
            18,
            22,
            18
        )

        topics_card.setLayout(topics_layout)

        # =========================
        # Layout
        # =========================

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.back_button)
        top_layout.addStretch()

        cards_layout = QHBoxLayout()
        cards_layout.addWidget(practice_card)
        cards_layout.addWidget(kana_card)
        cards_layout.setSpacing(24)

        main_layout = QVBoxLayout()

        main_layout.addLayout(top_layout)
        main_layout.addSpacing(45)

        main_layout.addWidget(self.title)
        main_layout.addWidget(self.japanese_subtitle)
        main_layout.addSpacing(5)
        main_layout.addWidget(self.description)

        main_layout.addLayout(cards_layout)

        main_layout.addSpacing(18)
        main_layout.addWidget(topics_card)

        main_layout.addStretch()

        main_layout.setContentsMargins(55, 35, 55, 45)

        self.setLayout(main_layout)

        # =========================
        # Styling
        # =========================

        self.setStyleSheet("""
            QWidget#beginnerMenu {
                background-color: #ffe1f5;
                color: #4d3845;
                font-family: Sans Serif;
            }

            QLabel {
                background: transparent;
            }

            QLabel#beginnerTitle {
                font-size: 42px;
                font-weight: 800;
                color: #563847;
            }

            QLabel#japaneseSubtitle {
                font-size: 21px;
                font-weight: 600;
                color: #b84f7d;
            }

            QLabel#description {
                font-size: 16px;
                color: #7a5d6c;
            }

            QFrame#studyCard {
                background-color: #fff8fb;
                border: 2px solid #f39ac1;
                border-radius: 20px;
                min-height: 230px;
            }

            QLabel#cardTitle {
                font-size: 25px;
                font-weight: 700;
                color: #7a3f5c;
            }

            QLabel#cardDescription {
                font-size: 16px;
                color: #705763;
                line-height: 1.4;
            }

            QPushButton#cardButton {
                background-color: #fff1f6;
                color: #7a3f5c;

                border: 2px solid #f04f98;
                border-radius: 13px;

                padding: 11px 18px;

                font-size: 16px;
                font-weight: 600;
            }

            QPushButton#cardButton:hover {
                background-color: #ffddeb;
            }

            QPushButton#cardButton:pressed {
                background-color: #ffcde1;
            }

            QPushButton#backButton {
                background-color: transparent;
                color: #7a3f5c;

                border: none;
                padding: 8px 10px;

                font-size: 16px;
                font-weight: 600;
            }

            QPushButton#backButton:hover {
                color: #d34484;
            }

            QFrame#topicsCard {
                background-color: #fff8fb;

                border: 2px solid #f39ac1;
                border-radius: 16px;
            }

            QLabel#topicsTitle {
                font-size: 20px;
                font-weight: 700;
                color: #7a3f5c;
            }

            QLabel#topicsDescription {
                font-size: 15px;
                color: #705763;
            }

            QPushButton#topicsButton {
                background-color: #fff1f6;
                color: #7a3f5c;

                border: 2px solid #f04f98;
                border-radius: 12px;

                padding: 9px 18px;

                font-size: 15px;
                font-weight: 600;
            }

            QPushButton#topicsButton:hover {
                background-color: #ffddeb;
            }

            QPushButton#topicsButton:pressed {
                background-color: #ffcde1;
            }
        """)

class KanaHelpScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("kanaHelpScreen")
        self.setAttribute(Qt.WA_StyledBackground, True)

        # =========================
        # Navigation
        # =========================

        self.back_button = QPushButton("← Back")
        self.back_button.setObjectName("backButton")

        self.title = QLabel("Kana Help")
        self.title.setObjectName("kanaTitle")

        self.subtitle = QLabel("ひらがな・カタカナ")
        self.subtitle.setObjectName("kanaSubtitle")

        # =========================
        # Section buttons
        # =========================

        self.kana_section_button = QPushButton("Kana")
        self.dakuten_section_button = QPushButton("Dakuten")
        self.combo_section_button = QPushButton("Combinations")
        self.extra_section_button = QPushButton("Extra Sounds")

        section_buttons = [
            self.kana_section_button,
            self.dakuten_section_button,
            self.combo_section_button,
            self.extra_section_button,
        ]

        for button in section_buttons:
            button.setObjectName("sectionButton")

        # =========================
        # Content pages
        # =========================

        self.content_stack = QStackedWidget()
        self.content_stack.setObjectName("kanaStack")

        self.kana_page = self.create_kana_page(
            "Basic Kana",
            "basic"
        )

        self.dakuten_page = self.create_kana_page(
            "Dakuten & Handakuten",
            "dakuten"
        )

        self.combo_page = self.create_kana_page(
            "Combinations",
            "yoon"
        )

        self.extra_page = self.create_extra_page()

        self.content_stack.addWidget(self.kana_page)
        self.content_stack.addWidget(self.dakuten_page)
        self.content_stack.addWidget(self.combo_page)
        self.content_stack.addWidget(self.extra_page)

        # Kana is always the default.
        self.content_stack.setCurrentWidget(self.kana_page)

        # =========================
        # Section switching
        # =========================

        self.kana_section_button.clicked.connect(
            lambda: self.content_stack.setCurrentWidget(
                self.kana_page
            )
        )

        self.dakuten_section_button.clicked.connect(
            lambda: self.content_stack.setCurrentWidget(
                self.dakuten_page
            )
        )

        self.combo_section_button.clicked.connect(
            lambda: self.content_stack.setCurrentWidget(
                self.combo_page
            )
        )

        self.extra_section_button.clicked.connect(
            lambda: self.content_stack.setCurrentWidget(
                self.extra_page
            )
        )

        # =========================
        # Right-side section menu
        # =========================

        section_layout = QVBoxLayout()

        section_layout.addWidget(self.kana_section_button)
        section_layout.addWidget(self.dakuten_section_button)
        section_layout.addWidget(self.combo_section_button)
        section_layout.addWidget(self.extra_section_button)

        section_layout.addStretch()

        section_layout.setSpacing(10)

        # =========================
        # Main content area
        # =========================

        content_layout = QHBoxLayout()

        content_layout.addWidget(
            self.content_stack,
            stretch=1
        )

        content_layout.addSpacing(18)

        content_layout.addLayout(section_layout)

        # =========================
        # Main layout
        # =========================

        main_layout = QVBoxLayout()

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.back_button)
        top_layout.addStretch()

        main_layout.addLayout(top_layout)

        main_layout.addWidget(self.title)
        main_layout.addWidget(self.subtitle)

        main_layout.addSpacing(12)

        main_layout.addLayout(content_layout)

        main_layout.setContentsMargins(
            35,
            25,
            35,
            30
        )

        self.setLayout(main_layout)

        # TEMPORARY styling.
        # The rainy flower-field insanity comes later.
        self.setStyleSheet("""
            QWidget#kanaHelpScreen {
                background-color: #f7f4f2;
                color: #453d42;
                font-family: Sans Serif;
            }

            QLabel {
                background: transparent;
            }

            QLabel#kanaTitle {
                font-size: 32px;
                font-weight: 800;
            }

            QLabel#kanaSubtitle {
                font-size: 18px;
                color: #806d78;
            }

            QLabel#pageTitle {
                font-size: 22px;
                font-weight: 700;
                color: #55464e;
            }

            QLabel#chartTitle {
                font-size: 18px;
                font-weight: 700;
                color: #6f5965;
            }

            QFrame#kanaChart {
                background-color: rgba(255, 255, 255, 215);

                border: 1px solid #d8ccd2;
                border-radius: 16px;
            }

            QPushButton#kanaTile {
                background-color: rgba(255, 255, 255, 225);
                color: #453740;

                border: 1px solid #d8cbd1;
                border-radius: 9px;

                font-size: 14px;
                font-weight: 600;
            }

            QPushButton#kanaTile:hover {
                background-color: #ffffff;
                border-color: #a98b99;
            }

            QPushButton#sectionButton {
                background-color: transparent;
                color: #69545f;

                border: none;
                border-left: 3px solid #c6aab7;

                padding: 10px 13px;

                font-size: 14px;
                font-weight: 600;

                text-align: left;
            }

            QPushButton#sectionButton:hover {
                background-color: rgba(255, 255, 255, 100);
                border-left-color: #826574;
            }

            QPushButton#backButton {
                background: transparent;
                border: none;

                color: #69545f;

                font-size: 15px;
                font-weight: 600;
            }
        """)

    def create_kana_page(self, title_text, section_name):
        page = QWidget()

        page_layout = QVBoxLayout()

        title = QLabel(title_text)
        title.setObjectName("pageTitle")

        page_layout.addWidget(title)
        page_layout.addSpacing(8)

        charts_layout = QHBoxLayout()

        hiragana_chart = self.create_chart(
            "Hiragana",
            "hiragana",
            section_name
        )

        katakana_chart = self.create_chart(
            "Katakana",
            "katakana",
            section_name
        )

        charts_layout.addWidget(hiragana_chart)
        charts_layout.addWidget(katakana_chart)

        charts_layout.setSpacing(18)

        page_layout.addLayout(charts_layout)

        page.setLayout(page_layout)

        return page

    def create_chart(
        self,
        title_text,
        script_name,
        section_name
    ):
        chart = QFrame()
        chart.setObjectName("kanaChart")

        layout = QVBoxLayout()

        title = QLabel(title_text)
        title.setObjectName("chartTitle")

        layout.addWidget(title)

        grid = QGridLayout()
        grid.setSpacing(4)

        section = KANA_DATA[script_name][section_name]

        columns = section["columns"]
        items = section["items"]

        for index, item in enumerate(items):

            row = index // columns
            column = index % columns

            if item is None:
                continue

            kana, romaji = item

            tile = QPushButton(
                f"{kana}\n{romaji}"
            )

            tile.setObjectName("kanaTile")

            tile.setFixedHeight(42)

            # Future audio system can use these.
            tile.setProperty("kana", kana)
            tile.setProperty("romaji", romaji)

            grid.addWidget(
                tile,
                row,
                column
            )

        layout.addLayout(grid)

        layout.setContentsMargins(
            16,
            14,
            16,
            16
        )

        chart.setLayout(layout)

        return chart

    def create_extra_page(self):
        page = QWidget()

        layout = QVBoxLayout()

        title = QLabel("Extra Sounds")
        title.setObjectName("pageTitle")

        description = QLabel(
            "Extended Katakana and additional sounds "
            "will live here."
        )

        layout.addWidget(title)
        layout.addWidget(description)

        layout.addStretch()

        page.setLayout(layout)

        return page

class SettingsScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("settingsScreen")
        self.setAttribute(Qt.WA_StyledBackground, True)

        # =========================
        # Header
        # =========================

        self.back_button = QPushButton("← Back")
        self.back_button.setObjectName("backButton")

        self.title = QLabel("Settings")
        self.title.setObjectName("settingsTitle")

        self.subtitle = QLabel("Make Chinpunkanpun yours.")
        self.subtitle.setObjectName("settingsSubtitle")

        # =========================
        # Cards
        # =========================

        appearance_card = self.create_card(
            "✦  Appearance",
            [
                "Theme",
                "Background",
                "Fonts",
            ]
        )

        reading_card = self.create_card(
            "Aa  Reading",
            [
                "Text Size",
                "Furigana",
                "Study Support",
            ]
        )

        audio_card = self.create_card(
            "♪  Audio",
            [
                "Voice",
                "Music",
                "Volume",
            ]
        )

        general_card = self.create_card(
            "⚙  General",
            [
                "Defaults",
                "Startup",
                "Other",
            ]
        )

        # =========================
        # Layout
        # =========================

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.back_button)
        top_layout.addStretch()

        cards_layout = QGridLayout()

        cards_layout.addWidget(appearance_card, 0, 0)
        cards_layout.addWidget(reading_card, 0, 1)
        cards_layout.addWidget(audio_card, 1, 0)
        cards_layout.addWidget(general_card, 1, 1)

        cards_layout.setHorizontalSpacing(22)
        cards_layout.setVerticalSpacing(22)

        main_layout = QVBoxLayout()

        main_layout.addLayout(top_layout)

        main_layout.addSpacing(35)

        main_layout.addWidget(self.title)
        main_layout.addWidget(self.subtitle)

        main_layout.addSpacing(30)

        main_layout.addLayout(cards_layout)

        main_layout.addStretch()

        main_layout.setContentsMargins(55, 35, 55, 45)
        main_layout.setSpacing(6)

        self.setLayout(main_layout)

        # =========================
        # Styling
        # =========================

        self.setStyleSheet("""
            QWidget#settingsScreen {
                background-color: #17151c;
                color: #eeeaf2;
                font-family: Sans Serif;
            }

            QLabel {
                background: transparent;
            }

            QLabel#settingsTitle {
                font-size: 40px;
                font-weight: 800;
                color: #f3eff6;
            }

            QLabel#settingsSubtitle {
                font-size: 16px;
                color: #a9a1b0;
            }

            QFrame#settingsCard {
                background-color: #211e28;

                border: 1px solid #3c3548;
                border-radius: 18px;

                min-height: 170px;
            }

            QLabel#cardTitle {
                font-size: 21px;
                font-weight: 700;
                color: #a996e8;
            }

            QLabel#settingItem {
                font-size: 16px;
                color: #d2ccd7;

                padding: 4px 0px;
            }

            QPushButton#backButton {
                background-color: transparent;
                color: #a996e8;

                border: none;

                padding: 8px 10px;

                font-size: 16px;
                font-weight: 600;
            }

            QPushButton#backButton:hover {
                color: #c1b3f2;
            }
        """)

    def create_card(self, title_text, items):
        card = QFrame()
        card.setObjectName("settingsCard")

        title = QLabel(title_text)
        title.setObjectName("cardTitle")

        layout = QVBoxLayout()

        layout.addWidget(title)
        layout.addSpacing(12)

        for item_text in items:
            item = QLabel(item_text)
            item.setObjectName("settingItem")
            layout.addWidget(item)

        layout.addStretch()

        layout.setContentsMargins(24, 22, 24, 22)

        card.setLayout(layout)

        return card

class ExtrasScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("extrasScreen")
        self.setAttribute(Qt.WA_StyledBackground, True)

        # =========================
        # Header
        # =========================

        self.back_button = QPushButton("← Back")
        self.back_button.setObjectName("backButton")

        self.title = QLabel("Extras ✦")
        self.title.setObjectName("extrasTitle")

        self.subtitle = QLabel(
            "Things that definitely belong in a language app."
        )
        self.subtitle.setObjectName("extrasSubtitle")

        # =========================
        # Cards
        # =========================

        chaos_card = self.create_extra_card(
            "CHAOS MODE",
            "Bad decisions.\nGreat Japanese.",
            "Locked",
            "chaosCard"
        )

        credits_card = self.create_extra_card(
            "CREDITS",
            "Humans behind\nthe madness.",
            "Open →",
            "creditsCard"
        )

        mystery_card = self.create_extra_card(
            "???",
            "Something is\nhiding here.",
            "???",
            "mysteryCard"
        )

        # =========================
        # Layout
        # =========================

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.back_button)
        top_layout.addStretch()

        cards_layout = QHBoxLayout()

        cards_layout.addWidget(chaos_card)
        cards_layout.addWidget(credits_card)
        cards_layout.addWidget(mystery_card)

        cards_layout.setSpacing(18)

        main_layout = QVBoxLayout()

        main_layout.addLayout(top_layout)

        main_layout.addSpacing(45)

        main_layout.addWidget(self.title)
        main_layout.addWidget(self.subtitle)

        main_layout.addSpacing(35)

        main_layout.addLayout(cards_layout)

        main_layout.addSpacing(24)

        footer = QLabel(
            "More questionable ideas coming later."
        )
        footer.setObjectName("extrasFooter")

        main_layout.addWidget(
            footer,
            alignment=Qt.AlignHCenter
        )

        main_layout.addStretch()

        main_layout.setContentsMargins(
            55,
            35,
            55,
            45
        )

        self.setLayout(main_layout)

        # =========================
        # Styling
        # =========================

        self.setStyleSheet("""
            QWidget#extrasScreen {
                background-color: #142326;
                color: #f5efe3;
                font-family: Sans Serif;
            }

            QLabel {
                background: transparent;
            }

            QLabel#extrasTitle {
                font-size: 42px;
                font-weight: 800;
                color: #f5efe3;
            }

            QLabel#extrasSubtitle {
                font-size: 16px;
                color: #aebfba;
            }

            QLabel#extrasFooter {
                font-size: 14px;
                color: #718985;
            }

            QFrame#extraCard {
                background-color: #1c3032;

                border: 1px solid #43615d;
                border-radius: 20px;

                min-height: 240px;
            }

            QFrame#extraCard:hover {
                background-color: #22383a;
                border-color: #c5a967;
            }

            QLabel#extraCardTitle {
                font-size: 22px;
                font-weight: 800;
                color: #d6bd78;
            }

            QLabel#extraCardDescription {
                font-size: 16px;
                color: #d8e0dc;
            }

            QPushButton#extraCardButton {
                background-color: #263f40;
                color: #ead8a4;

                border: 1px solid #9e8953;
                border-radius: 12px;

                padding: 10px 16px;

                font-size: 15px;
                font-weight: 600;
            }

            QPushButton#extraCardButton:hover {
                background-color: #304c4c;
                border-color: #d6bd78;
            }

            QPushButton#extraCardButton:pressed {
                background-color: #1e3334;
            }

            QPushButton#backButton {
                background-color: transparent;
                color: #d6bd78;

                border: none;

                padding: 8px 10px;

                font-size: 16px;
                font-weight: 600;
            }

            QPushButton#backButton:hover {
                color: #f2dda1;
            }
        """)

    def create_extra_card(
        self,
        title_text,
        description_text,
        button_text,
        card_name
    ):
        card = QFrame()
        card.setObjectName("extraCard")

        title = QLabel(title_text)
        title.setObjectName("extraCardTitle")

        description = QLabel(description_text)
        description.setObjectName("extraCardDescription")

        button = QPushButton(button_text)
        button.setObjectName("extraCardButton")

        # Save these for future functionality.
        if card_name == "chaosCard":
            self.chaos_button = button

        elif card_name == "creditsCard":
            self.credits_button = button

        elif card_name == "mysteryCard":
            self.mystery_button = button

        layout = QVBoxLayout()

        layout.addWidget(title)
        layout.addSpacing(14)

        layout.addWidget(description)

        layout.addStretch()

        layout.addWidget(button)

        layout.setContentsMargins(
            24,
            24,
            24,
            24
        )

        card.setLayout(layout)

        return card

class TopicsScreen(QWidget):

    topic_selected = Signal(str)

    def __init__(self):
        super().__init__()

        self.setObjectName("topicsScreen")
        self.setAttribute(Qt.WA_StyledBackground, True)

        # =========================
        # Header
        # =========================

        self.back_button = QPushButton("← Back")
        self.back_button.setObjectName("backButton")

        self.title = QLabel("Choose a Topic")
        self.title.setObjectName("topicsTitle")

        self.subtitle = QLabel(
            "What kind of world do you want to read today?"
        )
        self.subtitle.setObjectName("topicsSubtitle")

        # =========================
        # Topic cards
        # =========================

        topics_layout = QGridLayout()

        topics_layout.setHorizontalSpacing(18)
        topics_layout.setVerticalSpacing(18)

        positions = [
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 0),
            (1, 1),
        ]

        self.topic_buttons = {}

        for (topic_key, topic_data), position in zip(
            TOPICS.items(),
            positions
        ):
            card = self.create_topic_card(
                topic_key,
                topic_data["name"],
                topic_data["description"],
            )

            topics_layout.addWidget(
                card,
                position[0],
                position[1]
            )

        # Make Random sit centered on the bottom row.
        topics_layout.setColumnStretch(0, 1)
        topics_layout.setColumnStretch(1, 1)
        topics_layout.setColumnStretch(2, 1)

        # =========================
        # Main layout
        # =========================

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.back_button)
        top_layout.addStretch()

        main_layout = QVBoxLayout()

        main_layout.addLayout(top_layout)

        main_layout.addSpacing(30)

        main_layout.addWidget(self.title)
        main_layout.addWidget(self.subtitle)

        main_layout.addSpacing(30)

        main_layout.addLayout(topics_layout)

        main_layout.addStretch()

        main_layout.setContentsMargins(
            55,
            35,
            55,
            45
        )

        self.setLayout(main_layout)

        # =========================
        # Styling
        # =========================

        self.setStyleSheet("""
            QWidget#topicsScreen {
                background-color: #eee8f5;
                color: #403747;
                font-family: Sans Serif;
            }

            QLabel {
                background: transparent;
            }

            QLabel#topicsTitle {
                font-size: 40px;
                font-weight: 800;
                color: #403747;
            }

            QLabel#topicsSubtitle {
                font-size: 16px;
                color: #766a7d;
            }

            QFrame#topicCard {
                background-color: #faf8fc;

                border: 1px solid #cfc4da;
                border-radius: 18px;

                min-height: 155px;
            }

            QLabel#topicName {
                font-size: 23px;
                font-weight: 700;
                color: #5f4a69;
            }

            QLabel#topicDescription {
                font-size: 15px;
                color: #75697b;
            }

            QPushButton#topicButton {
                background-color: #f2edf6;
                color: #654f70;

                border: 1px solid #b7a4c4;
                border-radius: 11px;

                padding: 9px 15px;

                font-size: 15px;
                font-weight: 600;
            }

            QPushButton#topicButton:hover {
                background-color: #e6dced;
                border-color: #8f759f;
            }

            QPushButton#topicButton:pressed {
                background-color: #dbcee5;
            }

            QPushButton#backButton {
                background: transparent;
                border: none;

                color: #695774;

                padding: 8px 10px;

                font-size: 16px;
                font-weight: 600;
            }

            QPushButton#backButton:hover {
                color: #45354e;
            }
        """)

    def create_topic_card(
        self,
        topic_key,
        name,
        description
    ):
        card = QFrame()
        card.setObjectName("topicCard")

        title = QLabel(name)
        title.setObjectName("topicName")

        description_label = QLabel(description)
        description_label.setObjectName(
            "topicDescription"
        )

        button = QPushButton("Choose →")
        button.setObjectName("topicButton")

        self.topic_buttons[topic_key] = button

        button.clicked.connect(
            lambda checked=False, key=topic_key:
                self.topic_selected.emit(key)
        )

        layout = QVBoxLayout()

        layout.addWidget(title)
        layout.addSpacing(7)
        layout.addWidget(description_label)

        layout.addStretch()

        layout.addWidget(button)

        layout.setContentsMargins(
            22,
            20,
            22,
            20
        )

        card.setLayout(layout)

        return card
