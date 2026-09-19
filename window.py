from PySide6.QtWidgets import QMainWindow, QStackedWidget, QMessageBox
from PySide6.QtCore import QThread, Qt, Signal
from passages import PassageWorker
from screens import KanaHelpScreen, MainMenu, PracticeScreen, BeginnerMenu, SettingsScreen, ExtrasScreen
from translation import TranslationWorker
from study_support import analyze_sentence

class MainWindow(QMainWindow):
    request_passage = Signal(str)
    request_translation = Signal(str)
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chinpunkanpun")

        self.setWindowFlags(
            Qt.Dialog
            | Qt.WindowTitleHint
            | Qt.WindowCloseButtonHint
        )

        self.setFixedSize(1000, 700)
        self.current_help_data = None
        self.current_passage = None
        self.current_mode = None
        self.current_translation = None
        self.showing_translation = False
        self.loading_passage = False
        self.main_menu = MainMenu()
        self.practice_screen = PracticeScreen()
        self.beginner_menu = BeginnerMenu()
        self.kana_help_screen = KanaHelpScreen()
        self.settings_screen = SettingsScreen()
        self.extras_screen = ExtrasScreen()
        self.worker = PassageWorker()
        self.translation_worker = TranslationWorker()
        self.stack = QStackedWidget()
        self.stack.addWidget(self.main_menu)
        self.stack.addWidget(self.practice_screen)
        self.stack.addWidget(self.beginner_menu)
        self.stack.addWidget(self.kana_help_screen)
        self.stack.addWidget(self.settings_screen)
        self.stack.addWidget(self.extras_screen)
        self.setCentralWidget(self.stack)
        self.practice_screen.new_passage_button.clicked.connect(self.new_passage)
        self.practice_screen.study_help_button.clicked.connect(self.study_help_show)
        self.main_menu.intermediate_button.clicked.connect(self.load_intermediate)
        self.main_menu.beginner_button.clicked.connect(self.open_beginner_menu)
        self.main_menu.settings_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.settings_screen))
        self.settings_screen.back_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.main_menu))
        self.main_menu.extras_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.extras_screen))
        self.extras_screen.back_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.main_menu))
        self.beginner_menu.practice_button.clicked.connect(self.load_beginner)
        self.beginner_menu.kana_button.clicked.connect(self.open_kana_help)
        self.beginner_menu.back_button.clicked.connect(self.go_back_to_main)
        self.kana_help_screen.back_button.clicked.connect(self.go_back_to_beginner)
        self.practice_screen.back_button.clicked.connect(self.go_back_stack)
        self.practice_screen.translate_button.clicked.connect(self.translate_current)
        self.thread: QThread = QThread(self)
        self.request_passage.connect(self.worker.do_work)
        self.worker.signal.connect(self.recieve_sig)
        self.worker.moveToThread(self.thread)
        self.thread.start()
        self.translation_thread: QThread = QThread(self)
        self.request_translation.connect(self.translation_worker.do_translate)
        self.translation_worker.finished.connect(self.recieve_translation)
        self.translation_worker.moveToThread(self.translation_thread)
        self.translation_thread.start()

    def switch_stack(self):
        self.stack.setCurrentWidget(self.practice_screen)
    def go_back_stack(self):
        self.stack.setCurrentWidget(self.main_menu)
    def new_passage(self):
        if self.current_mode is None:
            return

        if self.loading_passage:
            return

        self.loading_passage = True
        self.practice_screen.new_passage_button.setEnabled(False)
        self.request_passage.emit(self.current_mode)
    def open_beginner_menu(self):
        self.stack.setCurrentWidget(self.beginner_menu)
    def open_kana_help(self):
        self.stack.setCurrentWidget(self.kana_help_screen)
    def go_back_to_main(self):
        self.stack.setCurrentWidget(self.main_menu)
    def go_back_to_beginner(self):
        self.stack.setCurrentWidget(self.beginner_menu)
    def load_beginner(self):
        self.current_mode = "beginner"
        self.stack.setCurrentWidget(self.practice_screen)
    def load_intermediate(self):
        self.current_mode = "intermediate"
        self.stack.setCurrentWidget(self.practice_screen)
    def study_help_show(self):
        if not self.current_help_data:
                return

        lines = []

        for item in self.current_help_data:
            meanings = ", ".join(item["meaning"])

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
    def recieve_sig(self, text):
        self.loading_passage = False
        self.current_passage = text
        self.current_translation = None
        self.showing_translation = False
        self.practice_screen.new_passage_button.setEnabled(True)
        self.practice_screen.passage_box.setText(text)
        if self.current_mode == "beginner":
            self.current_help_data = analyze_sentence(text)
            print("HELP DATA:", self.current_help_data)
        else:
            self.current_help_data = None
    def translate_current(self):
        if self.showing_translation == True:
            self.practice_screen.passage_box.setText(self.current_passage)
            self.showing_translation = False
        elif self.showing_translation == False and self.current_translation is None:
            self.request_translation.emit(self.current_passage)
        else:
            self.practice_screen.passage_box.setText(self.current_translation)
            self.showing_translation = True
    def recieve_translation(self, translation):
        self.current_translation = translation
        self.showing_translation = True
        self.practice_screen.passage_box.setText(self.current_translation)
    def closeEvent(self, event):
        self.thread.quit()
        self.translation_thread.quit()
        self.thread.wait()
        self.translation_thread.wait()
        event.accept()
