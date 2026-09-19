import random

from PySide6.QtCore import QObject, Signal, Slot

from passage_bank import PASSAGE_BANK


def get_passage(mode, topic):
    mode_bank = PASSAGE_BANK.get(mode)

    if mode_bank is None:
        return "No passages available for this mode yet."

    topic_bank = mode_bank.get(topic)

    if not topic_bank:
        topic_bank = mode_bank.get("random", [])

    if not topic_bank:
        return "No passages available yet."

    return random.choice(topic_bank)


class PassageWorker(QObject):
    signal = Signal(str)

    @Slot(str, str)
    def do_work(self, mode, topic):
        result = get_passage(mode, topic)
        self.signal.emit(result)
