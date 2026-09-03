import random
import requests

URL = "https://api.tatoeba.org/v1/sentences"

params = {
    "lang":"jpn",
    "list": 506,
    "sort": "random",
    "limit": 10

}

number = random.randint(0, 10)
response=requests.get(URL, params=params)

data = response.json()

sentence = [
    data["data"][number]["text"] #print(data["data"][0]["text"])
]

final = random.choice(sentence)

def full():
    print(final)
    return final

full()
