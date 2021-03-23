import json
import random as rd
import tempfile as tmpf
import time as t

import requests as rq
from bs4 import BeautifulSoup as Soup
from pygame import mixer


def clear():
    for _ in range(1000):
        print()


print("Initialising...")

# init
# scrape adjectives
page = rq.get("https://grammar.yourdictionary.com/parts-of-speech/adjectives/list-of-adjective-words.html")
soup = Soup(page.text, "html.parser")
adjectives = [e.getText().title() for e in soup.select("td")]


# scrape animals
# print("Scraping vocabulary sources")
# page = rq.get("https://list.fandom.com/wiki/List_of_common_animals")
# soup = Soup(page.text, "html.parser")
# animals = [e.getText().title().replace(" ", "") for e in soup.select("td > ul > li > a")]
#
# def rand_name():
#     name = adjectives[rd.randint(0, len(adjectives) - 1)] + animals[rd.randint(0, len(animals) - 1)]
#     while name in names:
#         name = adjectives[rd.randint(0, len(adjectives) - 1)] + animals[rd.randint(0, len(animals) - 1)]
#     names.append(name)
#     return name

# use kahoot api instead
def rand_name():
    name = rq.get("https://apis.kahoot.it/namerator")
    name = json.loads(name.content)
    return name["name"]


# download, save and play music
print("Downloading kahoot theme song")
rsp = rq.get("https://www.privfile.com/download.php?fid=6026499a7309d-NTkzMg==")
fpath = f"{tmpf.gettempdir()}/kahoot.mp3"
with open(fpath, "wb") as f:
    f.write(rsp.content)

mixer.init()
mixer.music.load(fpath)
mixer.music.play()

# globals
names = []


def nth(number):
    if str(number)[-1] == "1":
        return f"{number}st"
    elif str(number)[-1] == "2":
        return f"{number}nd"
    elif str(number)[-1] == "3":
        return f"{number}rd"
    else:
        return f"{number}th"


# lobby start
clear()
print("Welcome to the Kahoot Lobby\n")
nPlayers = 0
while nPlayers < 5:
    nPlayers = int(input("Number of Players (at least 5): "))
nQuestions = 0
while nQuestions < 1:
    nQuestions = int(input("Number of Questions (at least 1): "))
clear()

for i in range(1, nPlayers + 1):
    print(f"Player {i}: {rand_name()}")

t.sleep(2)

finalists = []
for _ in range(5):
    finalists.append(names.pop(rd.randint(0, len(names) - 1)))
final_scores = [0]
for i in range(5):
    final_scores.insert(0, rd.randint(final_scores[0], 200 * (i + 1) * nQuestions))

clear()
for i, n in zip(range(len(finalists), 0, -1), finalists):
    t.sleep(1)
    print(f"in {nth(i)} place: ", end="")
    t.sleep(2)
    print(f"{n} | Score: {final_scores[i - 1]}")

input("\n\nPress enter to quit: ")
