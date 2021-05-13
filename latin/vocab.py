import json


# helper word class
class Word:
    def __init__(self, json: dict):
        self.q_la = json["qLa"]  # question text in latin
        self.q_en = json["qEn"]  # question text in english
        self.a_la = json["aLa"]  # answer text in latin
        self.a_en = json["aEn"]  # answer text in latin
        self.types = json["type"]
        self.stage = json["stage"]

    def get_a_latin(self) -> str:
        return ", ".join(self.a_la)

    def get_a_english(self) -> str:
        return ", ".join(self.a_en)

    def get_types(self) -> str:
        return ", ".join(self.types)


# instantiate words from json dict
def parse() -> list:
    intermediate = []
    with open("words.txt", "r") as f:
        raw = json.loads(f.read())

    for r in raw:
        intermediate.append(Word(r))

    return intermediate


words = parse()
