import math as mt
import random as rand

import requests as rq
from bs4 import BeautifulSoup as Soup

# scrape club list from premier league website
clubs = rq.get("https://www.premierleague.com/clubs", verify=False)
clubs = Soup(clubs.content, "html.parser")
clubs = [e.text for e in clubs.select("div.indexSection > div > ul > li > a > div.indexInfo > div.nameContainer > h4")]
clubs = clubs[:2 ** mt.floor(mt.log2(len(clubs)))]


# arrange fixtures
def arrange(clb):
    cb = clb.copy()
    fx = []
    for i in range(len(cb) // 2):
        home = rand.choice(cb)
        cb.remove(home)
        away = rand.choice(cb)
        cb.remove(away)
        fx.append((home, away))

    return fx


fixtures = arrange(clubs)


def fix(fx, rn):
    if len(fx) == 1:
        wnr = rand.choice(fx[0])
        print(f"""\n\n############################################
FINALS
############################################""")
        print(f"{fx[0][0]} plays {fx[0][1]} | {wnr} won!")
        return

    print(f"""\n\n############################################
Round {rn}
############################################""")
    winners = []
    for f in fx:
        wnr = rand.choice(f)
        print(f"{f[0]} plays {f[1]} | {wnr} won!")
        winners.append(rand.choice(f))
    fx = arrange(winners)
    fix(fx, rn - 1)


fix(fixtures, int(mt.log2(len(clubs))))
