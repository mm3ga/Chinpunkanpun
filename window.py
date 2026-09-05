from unittest import result

from PySide6.QtWidgets import QMainWindow, QPushButton, QStackedWidget
from PySide6.QtCore import QObject, QThread, Qt, Signal
from passages import Bbuttonlogic, PassageWorker
from screens import MainMenu, PracticeScreen

class MainWindow(QMainWindow):
    request_passage = Signal()
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chinpunkanpun")

        self.setWindowFlags(
            Qt.Dialog
            | Qt.WindowTitleHint
            | Qt.WindowCloseButtonHint
        )

        self.setFixedSize(1000, 700)
        self.loading_passage = False
        self.main_menu = MainMenu()
        self.practice_screen = PracticeScreen()
        self.worker = PassageWorker()
        self.stack = QStackedWidget()
        self.stack.addWidget(self.main_menu)
        self.stack.addWidget(self.practice_screen)
        self.setCentralWidget(self.stack)
        self.practice_screen.new_passage_button.clicked.connect(self.load_beginner)
        self.main_menu.beginner_button.clicked.connect(self.switch_stack)
        self.practice_screen.back_button.clicked.connect(self.go_back_stack)
        self.thread: QThread = QThread(self)
        self.request_passage.connect(self.worker.do_work)
        self.worker.signal.connect(self.recieve_sig)
        self.worker.moveToThread(self.thread)
        self.thread.start()
    def switch_stack(self):
        self.stack.setCurrentWidget(self.practice_screen)
    def go_back_stack(self):
        self.stack.setCurrentWidget(self.main_menu)
    def load_beginner(self):
        #bval = Bbuttonlogic()
        #self.practice_screen.passage_box.setText(bval)
        self.request_passage.emit()
        if self.loading_passage:
            return
        else:
            self.loading_passage = True,
            self.practice_screen.new_passage_button.setEnabled(False),
            self.request_passage.emit()
    def recieve_sig(self, text):
        #self.worker.signal.connect(self.worker.do_work)
        #print(text)
        self.loading_passage = False
        self.practice_screen.new_passage_button.setEnabled(True)
        self.practice_screen.passage_box.setText(text)
    def closeEvent(self, event):
        self.thread.quit()
        self.thread.wait()
        event.accept()
