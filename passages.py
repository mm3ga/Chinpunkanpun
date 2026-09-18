import random
from PySide6.QtCore import QObject, Signal
import requests
from sudachipy import Dictionary
from openjlpt import get_vocab

URL = "https://api.tatoeba.org/v1/sentences"

params = {
    "lang":"jpn",
    #"list": 506,
    "sort": "random",
    "limit": 25
}

tokenizer = Dictionary().create()

n5_vocab = get_vocab("N5")

n5_words = set()

for entry in n5_vocab:
    forms = [entry.word, entry.reading]

    for form in forms:
        for variant in form.replace("/", " ").split():
            n5_words.add(variant.strip())


def is_intermediate_sentence(text):
    advanced_patterns = [
        "いたしました",
        "でございます",
        "させていただ",
        "なければならない",
        "わけではない",
        "てもら",
        "のである",
        "なぜなら"
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

    words = tokenizer.tokenize(text)

    unknown_words = 0
    unknown_kanji_words = 0

    for word in words:
        pos = word.part_of_speech()[0]
        dictionary_word = word.dictionary_form()

        if pos in ["名詞", "動詞", "形容詞"]:
            if word.dictionary_form() not in n5_words:
                unknown_words += 1

                if any("\u4e00" <= char <= "\u9fff" for char in dictionary_word):
                    unknown_kanji_words += 1

    if unknown_words >= 3:
        return False

    if unknown_kanji_words >= 1:
        return False

    return True


def get_intermediate_passage():
    for attempt in range(5):
        intermediate_sentences = []

        response = requests.get(URL, params=params)
        data = response.json()

        for item in data["data"]:
            text = item["text"]

            if is_intermediate_sentence(text):
                intermediate_sentences.append(item)

        print("SURVIVORS:", len(intermediate_sentences))

        if intermediate_sentences:
            chosen = random.choice(intermediate_sentences)
            return chosen["text"]

    return "今日は何をしようかな。"

def get_beginner_passage():
    beginner_passages = [
        "猫が好きです。",
        "今日は暑いです。",
        "学校に行きます。",
    ]
    return random.choice(beginner_passages)


class PassageWorker(QObject):
    signal = Signal(str)

    def __init__(self):
        super().__init__()

    def do_work(self, mode):
        if mode == "beginner":
            result = get_beginner_passage()
        elif mode == "intermediate":
            result = get_intermediate_passage()
        else:
            return
        self.signal.emit(result)
