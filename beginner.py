import random
import requests

URL = "https://api.tatoeba.org/v1/sentences"

params = {
    "lang":"jpn",
    "list": 506,
    "sort": "random",
    "limit": 5

}

#number = random.randint(0, 4)
response=requests.get(URL, params=params)

data = response.json()


len(data["data"]) #print(data["data"][0]["text"])

chosen = random.choice(data["data"])
def beginnerb():
    print(chosen["text"])
