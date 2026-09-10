import random
from PySide6.QtCore import QObject, Signal
import requests

URL = "https://api.tatoeba.org/v1/sentences"

params = {
    "lang":"jpn",
    #"list": 506,
    "sort": "random",
    "limit": 5
}

def is_beginner_sentence(text):
    advanced_patterns = [
        "いたしました",
        "でございます",
        "させていただ",
        "なければならない",
        "わけではない",
    ]

    kanji_count = 0

    for char in text:
        if "\u4e00" <= char <= "\u9fff":
            kanji_count += 1

    for pattern in advanced_patterns:
        if pattern in text:
            return False

    if len(text) >= 25:
        return False

    if kanji_count >= 5:
        return False

    return True





def Bbuttonlogic():

    beginner_sentences = [

    ]

    response=requests.get(URL, params=params)
    data = response.json()

    for item in data["data"]:
        text = item["text"]
        if is_beginner_sentence(text) == True:
            beginner_sentences.append(item)

    chosen = random.choice(beginner_sentences)

    hold = chosen["text"]
    return hold


class PassageWorker(QObject):
    signal = Signal(str)
    def __init__(self):
        super().__init__()
    def do_work(self):
        result = Bbuttonlogic()
        self.signal.emit(result)
