from bs4 import BeautifulSoup as Soup
import requests as rq
import random as rd

print("Initialising...")

# init
# scrape adjectives
page = rq.get("https://grammar.yourdictionary.com/parts-of-speech/adjectives/list-of-adjective-words.html")
soup = Soup(page.text, "html.parser")
adjectives = [e.getText().title() for e in soup.select("td")]

# scrape animals
page = rq.get("https://list.fandom.com/wiki/List_of_common_animals")
soup = Soup(page.text, "html.parser")
animals = [e.getText().title().replace(" ", "") for e in soup.select("td > ul > li > a")]

def rand_name():
    return adjectives[rd.randint(0, len(adjectives) - 1)] + animals[rd.randint(0, len(animals) - 1)]


# lobby start
print("\n\n\n\nWelcome to the Kahoot Lobby\n")
nPlayers = int(input("Number of Players: "))
print()

for i in range(1, nPlayers + 1):
    print(f"Player {i}: {rand_name()}")