from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QMessageBox,
)

from PySide6.QtCore import (
    QThread,
    Qt,
    Signal,
)

from passages import PassageWorker

from screens import (
    KanaHelpScreen,
    MainMenu,
    PracticeScreen,
    BeginnerMenu,
    SettingsScreen,
    ExtrasScreen,
    TopicsScreen,
)

from translation import TranslationWorker
from study_support import analyze_sentence


class MainWindow(QMainWindow):
    request_passage = Signal(str, str)
    request_translation = Signal(str)

    def __init__(self):
        super().__init__()

        # =========================
        # Window
        # =========================

        self.setWindowTitle("Chinpunkanpun")

        self.setWindowFlags(
            Qt.Dialog
            | Qt.WindowTitleHint
            | Qt.WindowCloseButtonHint
        )

        self.setFixedSize(1000, 700)

        # =========================
        # App state
        # =========================

        self.current_help_data = None
        self.current_passage = None
        self.current_mode = None
        self.current_topic = "random"
        self.current_translation = None

        self.showing_translation = False
        self.loading_passage = False

        # =========================
        # Screens
        # =========================

        self.main_menu = MainMenu()
        self.practice_screen = PracticeScreen()
        self.beginner_menu = BeginnerMenu()
        self.kana_help_screen = KanaHelpScreen()
        self.settings_screen = SettingsScreen()
        self.extras_screen = ExtrasScreen()
        self.topics_screen = TopicsScreen()

        # Practice needs a dynamic return destination.
        self.practice_return_screen = self.main_menu

        # =========================
        # Stack
        # =========================

        self.stack = QStackedWidget()

        self.stack.addWidget(self.main_menu)
        self.stack.addWidget(self.practice_screen)
        self.stack.addWidget(self.beginner_menu)
        self.stack.addWidget(self.kana_help_screen)
        self.stack.addWidget(self.settings_screen)
        self.stack.addWidget(self.extras_screen)
        self.stack.addWidget(self.topics_screen)

        self.setCentralWidget(self.stack)

        # =========================
        # Main menu navigation
        # =========================

        self.main_menu.beginner_button.clicked.connect(
            self.open_beginner_menu
        )

        self.main_menu.intermediate_button.clicked.connect(
            self.load_intermediate
        )

        self.main_menu.settings_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(
                self.settings_screen
            )
        )

        self.main_menu.extras_button.clicked.connect(
            lambda: self.stack.setCurrentWidget(
                self.extras_screen
            )
        )

        # =========================
        # Beginner navigation
        # =========================

        self.beginner_menu.practice_button.clicked.connect(
            self.load_beginner
        )

        self.beginner_menu.kana_button.clicked.connect(
            self.open_kana_help
        )

        self.beginner_menu.topics_button.clicked.connect(
            self.open_beginner_topics
        )

        self.beginner_menu.back_button.clicked.connect(
            self.go_back_to_main
        )

        # =========================
        # Child-screen back buttons
        # =========================

        self.kana_help_screen.back_button.clicked.connect(
            self.go_back_to_beginner
        )

        self.topics_screen.back_button.clicked.connect(
            self.go_back_to_beginner
        )

        self.settings_screen.back_button.clicked.connect(
            self.go_back_to_main
        )

        self.extras_screen.back_button.clicked.connect(
            self.go_back_to_main
        )

        self.practice_screen.back_button.clicked.connect(
            self.back_from_practice
        )

        # =========================
        # Topic selection
        # =========================

        self.topics_screen.topic_selected.connect(
            self.select_topic
        )

        # =========================
        # Practice controls
        # =========================

        self.practice_screen.new_passage_button.clicked.connect(
            self.new_passage
        )

        self.practice_screen.study_help_button.clicked.connect(
            self.study_help_show
        )

        self.practice_screen.translate_button.clicked.connect(
            self.translate_current
        )

        # =========================
        # Passage worker
        # =========================

        self.worker = PassageWorker()

        self.thread = QThread(self)

        self.request_passage.connect(
            self.worker.do_work
        )

        self.worker.signal.connect(
            self.recieve_sig
        )

        self.worker.moveToThread(
            self.thread
        )

        self.thread.start()

        # =========================
        # Translation worker
        # =========================

        self.translation_worker = TranslationWorker()

        self.translation_thread = QThread(self)

        self.request_translation.connect(
            self.translation_worker.do_translate
        )

        self.translation_worker.finished.connect(
            self.recieve_translation
        )

        self.translation_worker.moveToThread(
            self.translation_thread
        )

        self.translation_thread.start()

    # ==================================================
    # Navigation
    # ==================================================

    def open_beginner_menu(self):
        self.stack.setCurrentWidget(
            self.beginner_menu
        )

    def open_kana_help(self):
        self.stack.setCurrentWidget(
            self.kana_help_screen
        )

    def open_beginner_topics(self):
        self.current_mode = "beginner"

        self.stack.setCurrentWidget(
            self.topics_screen
        )

    def go_back_to_main(self):
        self.stack.setCurrentWidget(
            self.main_menu
        )

    def go_back_to_beginner(self):
        self.stack.setCurrentWidget(
            self.beginner_menu
        )

    def back_from_practice(self):
        self.stack.setCurrentWidget(
            self.practice_return_screen
        )

    # ==================================================
    # Practice entry
    # ==================================================

    def load_beginner(self):
        self.current_mode = "beginner"
        self.current_topic = "random"

        self.practice_return_screen = self.beginner_menu

        self.update_practice_context()

        self.stack.setCurrentWidget(
            self.practice_screen
        )

    def load_intermediate(self):
        self.current_mode = "intermediate"
        self.current_topic = "random"

        # Intermediate currently opens directly
        # from Main Menu.
        self.practice_return_screen = self.main_menu

        self.update_practice_context()

        self.stack.setCurrentWidget(
            self.practice_screen
        )

    def select_topic(self, topic):
        self.current_topic = topic

        # If Practice was entered through Topics,
        # Back should return to Topics.
        self.practice_return_screen = self.topics_screen

        self.update_practice_context()

        self.stack.setCurrentWidget(
            self.practice_screen
        )

    def update_practice_context(self):
        if self.current_mode is None:
            return

        mode_name = self.current_mode.capitalize()
        topic_name = self.current_topic.capitalize()

        self.practice_screen.mode_label.setText(
            f"{mode_name} Practice"
        )

        self.practice_screen.subtitle.setText(
            f"Topic: {topic_name}"
        )

    # ==================================================
    # Passage system
    # ==================================================

    def new_passage(self):
        if self.current_mode is None:
            return

        if self.loading_passage:
            return

        self.loading_passage = True

        self.practice_screen.new_passage_button.setEnabled(
            False
        )

        self.request_passage.emit(
            self.current_mode,
            self.current_topic
        )

    def recieve_sig(self, text):
        self.loading_passage = False

        self.current_passage = text
        self.current_translation = None
        self.showing_translation = False

        self.practice_screen.new_passage_button.setEnabled(
            True
        )

        self.practice_screen.passage_box.setText(
            text
        )

        if self.current_mode == "beginner":
            self.current_help_data = analyze_sentence(
                text
            )

        else:
            self.current_help_data = None

    # ==================================================
    # Study help
    # ==================================================

    def study_help_show(self):
        if not self.current_help_data:
            return

        lines = []

        for item in self.current_help_data:
            if item["meaning"]:
                meanings = ", ".join(
                    item["meaning"]
                )

            else:
                meanings = "Meaning unavailable"

            line = (
                f'{item["surface"]} — '
                f'{item["reading"]} — '
                f'{meanings}'
            )

            lines.append(line)

        piss = "\n".join(lines)

        QMessageBox.information(
            self,
            "Study Help",
            piss
        )

    # ==================================================
    # Translation
    # ==================================================

    def translate_current(self):
        # Nothing to translate yet.
        if not self.current_passage:
            return

        if self.showing_translation:
            self.practice_screen.passage_box.setText(
                self.current_passage
            )

            self.showing_translation = False

        elif self.current_translation is None:
            self.request_translation.emit(
                self.current_passage
            )

        else:
            self.practice_screen.passage_box.setText(
                self.current_translation
            )

            self.showing_translation = True

    def recieve_translation(self, translation):
        self.current_translation = translation
        self.showing_translation = True

        self.practice_screen.passage_box.setText(
            self.current_translation
        )

    # ==================================================
    # Shutdown
    # ==================================================

    def closeEvent(self, event):
        self.thread.quit()
        self.translation_thread.quit()

        self.thread.wait()
        self.translation_thread.wait()

        event.accept()
