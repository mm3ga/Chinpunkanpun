import random
from PySide6.QtCore import QObject, Signal, SignalInstance
import requests

URL = "https://api.tatoeba.org/v1/sentences"

params = {
    "lang":"jpn",
    "list": 506,
    "sort": "random",
    "limit": 5
}

#KNOWN BUG: fresh passage logic needs to move inside function


def Bbuttonlogic():

    response=requests.get(URL, params=params)
    data = response.json()
    chosen = random.choice(data["data"])
    hold = chosen["text"]

    return hold

class PassageWorker(QObject):
    signal = Signal(str)
    def __init__(self):
        super().__init__()
    def do_work(self):
        result = Bbuttonlogic()
        self.signal.emit(result)
