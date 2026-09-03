import sys
import random
import requests
from window import MainWindow

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)


app = QApplication(sys.argv)

# CREATE the window
window = MainWindow()


title = QLabel("🌸 Chinpunkanpun: Kawaii Nihongo! 🌸")
title.setStyleSheet("font-size: 30px; font-weight: bold;")

beginner_button = QPushButton("Beginner Button")
intermediate_button = QPushButton("Intermediate Button")
master_button = QPushButton("Master Button")

passage_box = QTextEdit()
passage_box.setReadOnly(True)
passage_box.setPlaceholderText("Your Japanese passage will appear here...")

new_passage_button = QPushButton("New Passage")
translate_button = QPushButton("Translate")


top_layout = QHBoxLayout()
top_layout.addWidget(new_passage_button)
top_layout.addWidget(translate_button)

bottom_layout = QHBoxLayout()
bottom_layout.addWidget(beginner_button)
bottom_layout.addWidget(intermediate_button)
bottom_layout.addWidget(master_button)

main_layout = QVBoxLayout()
main_layout.addWidget(title)
main_layout.addLayout(top_layout)
main_layout.addWidget(passage_box)
main_layout.addLayout(bottom_layout)

container = QWidget()
container.setLayout(main_layout)

window.setCentralWidget(container)

window.show()

sys.exit(app.exec())
