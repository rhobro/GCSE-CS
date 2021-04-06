import requests as rq
from bs4 import BeautifulSoup as Soup

# scrape club list from bbc teams for 190 teams
clubs = rq.get("https://www.bbc.co.uk/sport/football/teams")
clubs = Soup(clubs.content, "html.parser")
clubs = [t.text for t in clubs.select(r"div.qa-story-body.story-body.gel-pica > table > tbody > tr > td > a > span")]

# write to text file
with open("teams.txt", "w") as f:
    f.write("\n".join(clubs))
