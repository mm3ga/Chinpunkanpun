import random
import requests

URL = "https://api.tatoeba.org/v1/sentences"

params = {
    "lang":"jpn",
    "list": 506,
    "sort": "random",
    "limit": 5

}
#
#KNOWN BUG: fresh passage logic needs to move inside function
#

#number = random.randint(0, 4)
response=requests.get(URL, params=params)

data = response.json()


#len(data["data"]) #print(data["data"][0]["text"])

chosen = random.choice(data["data"])

def Bbuttonlogic():
    hold = chosen["text"]

    return hold
