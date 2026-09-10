from PySide6.QtWidgets import QMainWindow, QPushButton, QStackedWidget
from PySide6.QtCore import QObject, QThread, Qt, Signal
from passages import Bbuttonlogic, PassageWorker
from screens import MainMenu, PracticeScreen
from translation import TranslationWorker

class MainWindow(QMainWindow):
    request_passage = Signal()
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
        self.current_passage = None
        self.current_translation = None
        self.showing_translation = False
        self.loading_passage = False
        self.main_menu = MainMenu()
        self.practice_screen = PracticeScreen()
        self.worker = PassageWorker()
        self.translation_worker = TranslationWorker()
        self.stack = QStackedWidget()
        self.stack.addWidget(self.main_menu)
        self.stack.addWidget(self.practice_screen)
        self.setCentralWidget(self.stack)
        self.practice_screen.new_passage_button.clicked.connect(self.load_beginner)
        self.main_menu.beginner_button.clicked.connect(self.switch_stack)
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
    def load_beginner(self):
        #bval = Bbuttonlogic()
        #self.practice_screen.passage_box.setText(bval)
        if self.loading_passage:
            return

        self.loading_passage = True
        self.practice_screen.new_passage_button.setEnabled(False)
        self.request_passage.emit()
    def recieve_sig(self, text):
        #self.worker.signal.connect(self.worker.do_work)
        #print(text)
        self.loading_passage = False
        self.current_passage = text
        self.current_translation = None
        self.showing_translation = False
        self.practice_screen.new_passage_button.setEnabled(True)
        self.practice_screen.passage_box.setText(text)
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
