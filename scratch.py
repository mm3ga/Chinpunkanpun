from openjlpt import get_vocab

n5_vocab = get_vocab("N5")

beginner_words = set()

for entry in n5_vocab:
    for variant in entry.word.split("/"):
        beginner_words.add(variant.strip())

print(len(beginner_words))
print("いい" in beginner_words)
print("よい" in beginner_words)
print("川" in beginner_words)
print("河" in beginner_words)