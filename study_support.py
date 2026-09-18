from sudachipy import Dictionary
from openjlpt import get_vocab

tokenizer = Dictionary().create()
n5_vocab = get_vocab("N5")


def find_meaning(target):
    for entry in n5_vocab:
        for variant in entry.word.replace("/", " ").split():
            if target == variant:
                return entry.meanings

    return None


def katakana_to_hiragana(text):
    result = ""

    for char in text:
        if "\u30A1" <= char <= "\u30F6":
            result += chr(ord(char) - 0x60)
        else:
            result += char

    return result


def analyze_sentence(text):
    words = tokenizer.tokenize(text)
    help_records = []

    for word in words:
        pos = word.part_of_speech()[0]

        if pos in ["名詞", "動詞", "形容詞"]:
            dictionary_word = word.dictionary_form()
            meaning = find_meaning(dictionary_word)

            help_item = {
                "surface": word.surface(),
                "dictionary": dictionary_word,
                "reading": katakana_to_hiragana(word.reading_form()),
                "pos": pos,
                "meaning": meaning
            }

            help_records.append(help_item)

    return help_records
            
#analyze_sentence("今日は学校に行きます")
#print(analyze_sentence("今日は学校に行きます。"))