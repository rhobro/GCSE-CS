import json

from raw_vocab import *

type_map = {
    "v": "verb",
    "n": "noun",
    "a": "adjective",
    "p": "preposition",
    "r": "pronoun",
    "d": "adverb",
    "x": "misc"
}

new = []
for w in vocab:
    s = w.split("#")
    n = {
        "qLa": s[0],
        "aLa": s[3].split(":"),
        "qEn": s[1],
        "aEn": s[4].split(":"),
        "type": [type_map[t] for t in s[2]],
        "stage": int(s[5])
    }
    new.append(n)

print(json.dumps(new, indent="    "))
