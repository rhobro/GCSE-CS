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
def parse_raw(json) -> list:
    words = []

    for r in json:
        words.append(Word(r))

    return words


raw = [
    {
        "qLa": "\u00c4\u0081, ab + abl (also used as prefix with verbs)",
        "aLa": [
            "a",
            "ab"
        ],
        "qEn": "from, by (as prefix = away)",
        "aEn": [
            "from",
            "by"
        ],
        "type": [
            "preposition"
        ],
        "stage": 21
    },
    {
        "qLa": "absum, abesse",
        "aLa": [
            "absum",
            "abesse"
        ],
        "qEn": "be out, be absent, be away",
        "aEn": [
            "be out",
            "be absent",
            "be away"
        ],
        "type": [
            "verb"
        ],
        "stage": 6
    },
    {
        "qLa": "ac, atque (indecl.)",
        "aLa": [
            "ac",
            "atque",
            "et",
            "-que",
            "que"
        ],
        "qEn": "and",
        "aEn": [
            "and"
        ],
        "type": [
            "misc"
        ],
        "stage": 28
    },
    {
        "qLa": "accid\u00c5\u008d, accidere, accid\u00c4\u00ab",
        "aLa": [
            "accido",
            "accidere"
        ],
        "qEn": "happen",
        "aEn": [
            "happen"
        ],
        "type": [
            "verb"
        ],
        "stage": 25
    },
    {
        "qLa": "accipi\u00c5\u008d, accipere, acc\u00c4\u201cp\u00c4\u00ab, acceptus",
        "aLa": [
            "accipio",
            "accipere"
        ],
        "qEn": "accept, take in, receive",
        "aEn": [
            "accept",
            "take in",
            "receive"
        ],
        "type": [
            "verb"
        ],
        "stage": 10
    },
    {
        "qLa": "ad + acc (also used as prefix with verbs)",
        "aLa": [
            "ad"
        ],
        "qEn": "to, towards, at",
        "aEn": [
            "to",
            "towards",
            "at"
        ],
        "type": [
            "preposition"
        ],
        "stage": 3
    },
    {
        "qLa": "ade\u00c5\u008d (indecl.)",
        "aLa": [
            "adeo"
        ],
        "qEn": "so much, so greatly",
        "aEn": [
            "so much",
            "so greatly"
        ],
        "type": [
            "adverb"
        ],
        "stage": 27
    },
    {
        "qLa": "adiuv\u00c5\u008d, adiuv\u00c4\u0081re, adi\u00c5\u00abv\u00c4\u00ab, adi\u00c5\u00abtus",
        "aLa": [
            "adiuvo",
            "adiuvare"
        ],
        "qEn": "help",
        "aEn": [
            "help"
        ],
        "type": [
            "verb"
        ],
        "stage": 21
    },
    {
        "qLa": "adsum, adesse",
        "aLa": [
            "adsum",
            "adesse"
        ],
        "qEn": "be here, be present",
        "aEn": [
            "be here",
            "be present"
        ],
        "type": [
            "verb"
        ],
        "stage": 5
    },
    {
        "qLa": "adveni\u00c5\u008d, adven\u00c4\u00abre, adv\u00c4\u201cn\u00c4\u00ab",
        "aLa": [
            "advenio",
            "advenire"
        ],
        "qEn": "arrive",
        "aEn": [
            "arrive"
        ],
        "type": [
            "verb"
        ],
        "stage": 13
    },
    {
        "qLa": "ag\u00c5\u008d, agere, \u00c4\u201cg\u00c4\u00ab, \u00c4\u0081ctus",
        "aLa": [
            "ago",
            "agere"
        ],
        "qEn": "do, act, drive",
        "aEn": [
            "do",
            "act",
            "drive"
        ],
        "type": [
            "verb"
        ],
        "stage": 4
    },
    {
        "qLa": "aliquis, aliquid",
        "aLa": [
            "aliquis",
            "aliquid"
        ],
        "qEn": "someone, something",
        "aEn": [
            "someone",
            "something"
        ],
        "type": [
            "pronoun"
        ],
        "stage": 14
    },
    {
        "qLa": "alius, alia, aliud",
        "aLa": [
            "alius"
        ],
        "qEn": "other, another, else",
        "aEn": [
            "other",
            "another",
            "else"
        ],
        "type": [
            "adjective",
            "pronoun"
        ],
        "stage": 15
    },
    {
        "qLa": "alter, altera, alterum",
        "aLa": [
            "alter"
        ],
        "qEn": "the other, another, the second of two",
        "aEn": [
            "the other",
            "another",
            "the second of two",
            "other",
            "second of two"
        ],
        "type": [
            "adjective",
            "pronoun"
        ],
        "stage": 13
    },
    {
        "qLa": "altus, alta, altum",
        "aLa": [
            "altus"
        ],
        "qEn": "high, deep",
        "aEn": [
            "high",
            "deep"
        ],
        "type": [
            "adjective"
        ],
        "stage": 31
    },
    {
        "qLa": "ambul\u00c5\u008d, ambul\u00c4\u0081re, ambul\u00c4\u0081v\u00c4\u00ab",
        "aLa": [
            "ambulo",
            "ambulare"
        ],
        "qEn": "walk",
        "aEn": [
            "walk"
        ],
        "type": [
            "verb"
        ],
        "stage": 5
    },
    {
        "qLa": "am\u00c4\u00abcus, am\u00c4\u00abc\u00c4\u00ab, m.",
        "aLa": [
            "amicus"
        ],
        "qEn": "friend",
        "aEn": [
            "friend"
        ],
        "type": [
            "noun"
        ],
        "stage": 2
    },
    {
        "qLa": "am\u00c5\u008d, am\u00c4\u0081re, am\u00c4\u0081v\u00c4\u00ab, am\u00c4\u0081tus",
        "aLa": [
            "amo",
            "amare",
            "amor"
        ],
        "qEn": "love, like",
        "aEn": [
            "love",
            "like"
        ],
        "type": [
            "verb"
        ],
        "stage": 19
    },
    {
        "qLa": "amor, am\u00c5\u008dris, m.",
        "aLa": [
            "amo",
            "amor"
        ],
        "qEn": "love",
        "aEn": [
            "love"
        ],
        "type": [
            "noun"
        ],
        "stage": 22
    },
    {
        "qLa": "ancilla, ancillae, f.",
        "aLa": [
            "ancilla"
        ],
        "qEn": "slave-girl, maid",
        "aEn": [
            "slave-girl",
            "slave girl",
            "slavegirl",
            "maid"
        ],
        "type": [
            "noun"
        ],
        "stage": 2
    },
    {
        "qLa": "animus, anim\u00c4\u00ab, m.",
        "aLa": [
            "animus"
        ],
        "qEn": "spirit, soul, mind",
        "aEn": [
            "spirit",
            "soul",
            "mind"
        ],
        "type": [
            "noun"
        ],
        "stage": 17
    },
    {
        "qLa": "annus, ann\u00c4\u00ab, m.",
        "aLa": [
            "annus"
        ],
        "qEn": "year",
        "aEn": [
            "year"
        ],
        "type": [
            "noun"
        ],
        "stage": 21
    },
    {
        "qLa": "ante + acc",
        "aLa": [
            "ante"
        ],
        "qEn": "before, in front of",
        "aEn": [
            "before",
            "in front of"
        ],
        "type": [
            "preposition"
        ],
        "stage": 31
    },
    {
        "qLa": "ante\u00c4\u0081 (indecl.)",
        "aLa": [
            "antea"
        ],
        "qEn": "before",
        "aEn": [
            "before"
        ],
        "type": [
            "adverb"
        ],
        "stage": 27
    },
    {
        "qLa": "aperi\u00c5\u008d, aper\u00c4\u00abre, aperu\u00c4\u00ab, apertus",
        "aLa": [
            "aperio",
            "aperire"
        ],
        "qEn": "open",
        "aEn": [
            "open"
        ],
        "type": [
            "verb"
        ],
        "stage": 25
    },
    {
        "qLa": "app\u00c4\u0081re\u00c5\u008d, app\u00c4\u0081r\u00c4\u201cre, app\u00c4\u0081ru\u00c4\u00ab",
        "aLa": [
            "appareo",
            "apparere"
        ],
        "qEn": "appear",
        "aEn": [
            "appear"
        ],
        "type": [
            "verb"
        ],
        "stage": 27
    },
    {
        "qLa": "appropinqu\u00c5\u008d, appropinqu\u00c4\u0081re, appropinqu\u00c4\u0081v\u00c4\u00ab + dat",
        "aLa": [
            "appropinquo",
            "appropinquare"
        ],
        "qEn": "approach, come near to",
        "aEn": [
            "approach",
            "come near to"
        ],
        "type": [
            "verb"
        ],
        "stage": 17
    },
    {
        "qLa": "apud + acc",
        "aLa": [
            "apud"
        ],
        "qEn": "among, with, at the house of",
        "aEn": [
            "among",
            "with",
            "at the house of"
        ],
        "type": [
            "preposition"
        ],
        "stage": 14
    },
    {
        "qLa": "aqua, aquae, f.",
        "aLa": [
            "aqua"
        ],
        "qEn": "water",
        "aEn": [
            "water"
        ],
        "type": [
            "noun"
        ],
        "stage": 15
    },
    {
        "qLa": "aud\u00c4\u0081x, aud\u00c4\u0081cis",
        "aLa": [
            "audax"
        ],
        "qEn": "bold, daring",
        "aEn": [
            "bold",
            "daring"
        ],
        "type": [
            "adjective"
        ],
        "stage": 24
    },
    {
        "qLa": "audi\u00c5\u008d, aud\u00c4\u00abre, aud\u00c4\u00abv\u00c4\u00ab, aud\u00c4\u00abtus",
        "aLa": [
            "audio",
            "audire"
        ],
        "qEn": "hear, listen to",
        "aEn": [
            "hear",
            "listen to"
        ],
        "type": [
            "verb"
        ],
        "stage": 5
    },
    {
        "qLa": "aufer\u00c5\u008d, auferre, abstul\u00c4\u00ab, abl\u00c4\u0081tus",
        "aLa": [
            "aufero",
            "auferre"
        ],
        "qEn": "take away, carry off, steal",
        "aEn": [
            "take away",
            "carry off",
            "steal"
        ],
        "type": [
            "verb"
        ],
        "stage": 26
    },
    {
        "qLa": "aut ... aut (indecl.)",
        "aLa": [
            "aut aut"
        ],
        "qEn": "either ... or ...",
        "aEn": [
            "either or"
        ],
        "type": [
            "misc"
        ],
        "stage": 39
    },
    {
        "qLa": "bellum, bell\u00c4\u00ab, n.",
        "aLa": [
            "bellum"
        ],
        "qEn": "war",
        "aEn": [
            "war"
        ],
        "type": [
            "noun"
        ],
        "stage": 26
    },
    {
        "qLa": "bene (indecl.)",
        "aLa": [
            "bene"
        ],
        "qEn": "well",
        "aEn": [
            "well"
        ],
        "type": [
            "adverb"
        ],
        "stage": 17
    },
    {
        "qLa": "benignus, benigna, benignum",
        "aLa": [
            "benignus"
        ],
        "qEn": "kind, generous",
        "aEn": [
            "kind",
            "generous"
        ],
        "type": [
            "adjective"
        ],
        "stage": 17
    },
    {
        "qLa": "bib\u00c5\u008d, bibere, bib\u00c4\u00ab",
        "aLa": [
            "bibo",
            "bibere"
        ],
        "qEn": "drink",
        "aEn": [
            "drink"
        ],
        "type": [
            "verb"
        ],
        "stage": 3
    },
    {
        "qLa": "bonus, bona, bonum",
        "aLa": [
            "bonus"
        ],
        "qEn": "good",
        "aEn": [
            "good"
        ],
        "type": [
            "adjective"
        ],
        "stage": 16
    },
    {
        "qLa": "brevis, breve",
        "aLa": [
            "brevis"
        ],
        "qEn": "short, brief",
        "aEn": [
            "short",
            "brief"
        ],
        "type": [
            "adjective"
        ],
        "stage": 0
    },
    {
        "qLa": "cad\u00c5\u008d, cadere, cecid\u00c4\u00ab, c\u00c4\u0081sus",
        "aLa": [
            "cado",
            "cadere"
        ],
        "qEn": "fall",
        "aEn": [
            "fall"
        ],
        "type": [
            "verb"
        ],
        "stage": 39
    },
    {
        "qLa": "caelum, cael\u00c4\u00ab, n.",
        "aLa": [
            "caelum"
        ],
        "qEn": "sky, heaven",
        "aEn": [
            "sky",
            "heaven"
        ],
        "type": [
            "noun"
        ],
        "stage": 22
    },
    {
        "qLa": "canis, canis, m.",
        "aLa": [
            "canis"
        ],
        "qEn": "dog",
        "aEn": [
            "dog"
        ],
        "type": [
            "noun"
        ],
        "stage": 1
    },
    {
        "qLa": "capi\u00c5\u008d, capere, c\u00c4\u201cp\u00c4\u00ab, captus",
        "aLa": [
            "capio",
            "capere"
        ],
        "qEn": "take, catch, capture, adopt (a plan)",
        "aEn": [
            "take",
            "catch",
            "capture",
            "adopt"
        ],
        "type": [
            "verb"
        ],
        "stage": 11
    },
    {
        "qLa": "caput, capitis, n.",
        "aLa": [
            "caput"
        ],
        "qEn": "head",
        "aEn": [
            "head"
        ],
        "type": [
            "noun"
        ],
        "stage": 18
    },
    {
        "qLa": "c\u00c4\u0081rus, c\u00c4\u0081ra, c\u00c4\u0081rum",
        "aLa": [
            "carus"
        ],
        "qEn": "dear",
        "aEn": [
            "dear"
        ],
        "type": [
            "adjective"
        ],
        "stage": 19
    },
    {
        "qLa": "celer, celere",
        "aLa": [
            "celer"
        ],
        "qEn": "quick, fast",
        "aEn": [
            "quick",
            "fast"
        ],
        "type": [
            "adjective"
        ],
        "stage": 9
    },
    {
        "qLa": "c\u00c4\u201cl\u00c5\u008d, c\u00c4\u201cl\u00c4\u0081re, c\u00c4\u201cl\u00c4\u0081v\u00c4\u00ab, c\u00c4\u201cl\u00c4\u0081tus",
        "aLa": [
            "celo",
            "celare"
        ],
        "qEn": "hide",
        "aEn": [
            "hide"
        ],
        "type": [
            "verb"
        ],
        "stage": 21
    },
    {
        "qLa": "c\u00c4\u201cna, c\u00c4\u201cnae, f.",
        "aLa": [
            "cena"
        ],
        "qEn": "dinner, meal",
        "aEn": [
            "dinner",
            "meal"
        ],
        "type": [
            "noun"
        ],
        "stage": 2
    },
    {
        "qLa": "centum (indecl.)",
        "aLa": [
            "centum"
        ],
        "qEn": "a hundred",
        "aEn": [
            "a hundred"
        ],
        "type": [
            "adjective"
        ],
        "stage": 28
    },
    {
        "qLa": "c\u00c4\u201cter\u00c4\u00ab, c\u00c4\u201cterae, c\u00c4\u201ctera",
        "aLa": [
            "ceteri"
        ],
        "qEn": "the rest, the others",
        "aEn": [
            "the rest",
            "the others"
        ],
        "type": [
            "adjective"
        ],
        "stage": 13
    },
    {
        "qLa": "cibus, cib\u00c4\u00ab, m.",
        "aLa": [
            "cibus"
        ],
        "qEn": "food",
        "aEn": [
            "food"
        ],
        "type": [
            "noun"
        ],
        "stage": 2
    },
    {
        "qLa": "circum + acc",
        "aLa": [
            "circum"
        ],
        "qEn": "around",
        "aEn": [
            "around"
        ],
        "type": [
            "preposition"
        ],
        "stage": 21
    },
    {
        "qLa": "c\u00c4\u00abvis, c\u00c4\u00abvis, m.f.",
        "aLa": [
            "civis"
        ],
        "qEn": "citizen",
        "aEn": [
            "citizen"
        ],
        "type": [
            "noun"
        ],
        "stage": 11
    },
    {
        "qLa": "cl\u00c4\u0081m\u00c5\u008d, cl\u00c4\u0081m\u00c4\u0081re, cl\u00c4\u0081m\u00c4\u0081v\u00c4\u00ab, cl\u00c4\u0081m\u00c4\u0081tus",
        "aLa": [
            "clamo",
            "clamare",
            "clamor",
            "vox"
        ],
        "qEn": "shout",
        "aEn": [
            "shout"
        ],
        "type": [
            "verb"
        ],
        "stage": 3
    },
    {
        "qLa": "cl\u00c4\u0081mor, cl\u00c4\u0081m\u00c5\u008dris, m.",
        "aLa": [
            "clamo",
            "clamor",
            "vox"
        ],
        "qEn": "shout, shouting, noise",
        "aEn": [
            "shout",
            "shouting",
            "noise"
        ],
        "type": [
            "noun"
        ],
        "stage": 5
    },
    {
        "qLa": "coep\u00c4\u00ab, coepisse, coeptus",
        "aLa": [
            "coepi",
            "coepisse"
        ],
        "qEn": "began (past tenses only)",
        "aEn": [
            "began"
        ],
        "type": [
            "verb"
        ],
        "stage": 18
    },
    {
        "qLa": "c\u00c5\u008dgit\u00c5\u008d, c\u00c5\u008dgit\u00c4\u0081re, c\u00c5\u008dgit\u00c4\u0081v\u00c4\u00ab, c\u00c5\u008dgit\u00c4\u0081tus",
        "aLa": [
            "cogito",
            "cogitare",
            "puto",
            "putare"
        ],
        "qEn": "think, consider",
        "aEn": [
            "think",
            "consider"
        ],
        "type": [
            "verb"
        ],
        "stage": 19
    },
    {
        "qLa": "cogn\u00c5\u008dsc\u00c5\u008d, cogn\u00c5\u008dscere, cogn\u00c5\u008dv\u00c4\u00ab, cognitus",
        "aLa": [
            "cognosco",
            "cognoscere"
        ],
        "qEn": "get to know, find out, learn",
        "aEn": [
            "get to know",
            "find out",
            "learn"
        ],
        "type": [
            "verb"
        ],
        "stage": 18
    },
    {
        "qLa": "c\u00c5\u008dg\u00c5\u008d, c\u00c5\u008dgere, co\u00c4\u201cg\u00c4\u00ab, co\u00c4\u0081ctus",
        "aLa": [
            "cogo",
            "cogere"
        ],
        "qEn": "force, compel",
        "aEn": [
            "force",
            "compel"
        ],
        "type": [
            "verb"
        ],
        "stage": 25
    },
    {
        "qLa": "comes, comitis, m.f.",
        "aLa": [
            "comes"
        ],
        "qEn": "comrade, companion",
        "aEn": [
            "comrade",
            "companion"
        ],
        "type": [
            "noun"
        ],
        "stage": 27
    },
    {
        "qLa": "c\u00c5\u008dnfici\u00c5\u008d, c\u00c5\u008dnficere, c\u00c5\u008dnf\u00c4\u201cc\u00c4\u00ab, c\u00c5\u008dnfectus",
        "aLa": [
            "conficio",
            "conficere"
        ],
        "qEn": "finish; wear out, exhaust",
        "aEn": [
            "finish",
            "wear out",
            "exhaust"
        ],
        "type": [
            "verb"
        ],
        "stage": 19
    },
    {
        "qLa": "c\u00c5\u008dnor, c\u00c5\u008dn\u00c4\u0081r\u00c4\u00ab, c\u00c5\u008dn\u00c4\u0081tus sum",
        "aLa": [
            "conor",
            "conari"
        ],
        "qEn": "try",
        "aEn": [
            "try"
        ],
        "type": [
            "verb"
        ],
        "stage": 34
    },
    {
        "qLa": "c\u00c5\u008dnsilium, c\u00c5\u008dnsili\u00c4\u00ab, n.",
        "aLa": [
            "consilium"
        ],
        "qEn": "plan, idea, advice",
        "aEn": [
            "plan",
            "idea",
            "advice"
        ],
        "type": [
            "noun"
        ],
        "stage": 16
    },
    {
        "qLa": "c\u00c5\u008dnspici\u00c5\u008d, c\u00c5\u008dnspicere, c\u00c5\u008dnspex\u00c4\u00ab, c\u00c5\u008dnspectus",
        "aLa": [
            "conspicio",
            "conspicere"
        ],
        "qEn": "catch sight of, notice",
        "aEn": [
            "catch sight of",
            "notice"
        ],
        "type": [
            "verb"
        ],
        "stage": 7
    },
    {
        "qLa": "c\u00c5\u008dnstitu\u00c5\u008d, c\u00c5\u008dnstituere, c\u00c5\u008dnstitu\u00c4\u00ab, c\u00c5\u008dnstit\u00c5\u00abtus",
        "aLa": [
            "constituo",
            "constituere"
        ],
        "qEn": "decide",
        "aEn": [
            "decide"
        ],
        "type": [
            "verb"
        ],
        "stage": 28
    },
    {
        "qLa": "c\u00c5\u008dns\u00c5\u00abm\u00c5\u008d, c\u00c5\u008dns\u00c5\u00abmere, c\u00c5\u008dns\u00c5\u00abmps\u00c4\u00ab, c\u00c5\u008dns\u00c5\u00abmptus",
        "aLa": [
            "consumo",
            "consumere"
        ],
        "qEn": "eat",
        "aEn": [
            "eat"
        ],
        "type": [
            "verb"
        ],
        "stage": 8
    },
    {
        "qLa": "contr\u00c4\u0081 + acc",
        "aLa": [
            "contra"
        ],
        "qEn": "against",
        "aEn": [
            "against"
        ],
        "type": [
            "preposition"
        ],
        "stage": 33
    },
    {
        "qLa": "corpus, corporis, n.",
        "aLa": [
            "corpus"
        ],
        "qEn": "body",
        "aEn": [
            "body"
        ],
        "type": [
            "noun"
        ],
        "stage": 28
    },
    {
        "qLa": "cr\u00c4\u201cd\u00c5\u008d, cr\u00c4\u201cdere, cr\u00c4\u201cdid\u00c4\u00ab, cr\u00c4\u201cditus + dat",
        "aLa": [
            "credo",
            "credere"
        ],
        "qEn": "believe, trust, have faith in",
        "aEn": [
            "believe",
            "trust",
            "have faith in"
        ],
        "type": [
            "verb"
        ],
        "stage": 11
    },
    {
        "qLa": "cr\u00c5\u00abd\u00c4\u201clis, cr\u00c5\u00abd\u00c4\u201cle",
        "aLa": [
            "crudelis",
            "saevus"
        ],
        "qEn": "cruel",
        "aEn": [
            "cruel"
        ],
        "type": [
            "adjective"
        ],
        "stage": 20
    },
    {
        "qLa": "cum + abl (as prefix col- / com- / con- / cor-)",
        "aLa": [
            "cum"
        ],
        "qEn": "with (as prefix = together)",
        "aEn": [
            "with"
        ],
        "type": [
            "preposition"
        ],
        "stage": 7
    },
    {
        "qLa": "cum (indecl.)",
        "aLa": [
            "cum"
        ],
        "qEn": "when, since",
        "aEn": [
            "when",
            "since"
        ],
        "type": [
            "misc"
        ],
        "stage": 24
    },
    {
        "qLa": "cupi\u00c5\u008d, cupere, cup\u00c4\u00abv\u00c4\u00ab",
        "aLa": [
            "cupio",
            "cupere",
            "volo",
            "velle"
        ],
        "qEn": "want, desire",
        "aEn": [
            "want",
            "desire"
        ],
        "type": [
            "verb"
        ],
        "stage": 9
    },
    {
        "qLa": "c\u00c5\u00abr? (indecl.)",
        "aLa": [
            "cur"
        ],
        "qEn": "why?",
        "aEn": [
            "why"
        ],
        "type": [
            "adverb"
        ],
        "stage": 4
    },
    {
        "qLa": "c\u00c5\u00abra, c\u00c5\u00abrae, f.",
        "aLa": [
            "cura"
        ],
        "qEn": "care, worry",
        "aEn": [
            "care",
            "worry"
        ],
        "type": [
            "noun"
        ],
        "stage": 23
    },
    {
        "qLa": "c\u00c5\u00abr\u00c5\u008d, c\u00c5\u00abr\u00c4\u0081re, c\u00c5\u00abr\u00c4\u0081v\u00c4\u00ab, c\u00c5\u00abr\u00c4\u0081tus",
        "aLa": [
            "curo",
            "curare"
        ],
        "qEn": "look after, care for, supervise",
        "aEn": [
            "look after",
            "care for",
            "supervise"
        ],
        "type": [
            "verb"
        ],
        "stage": 19
    },
    {
        "qLa": "curr\u00c5\u008d, currere, cucurr\u00c4\u00ab, cursus",
        "aLa": [
            "curro",
            "currere"
        ],
        "qEn": "run",
        "aEn": [
            "run"
        ],
        "type": [
            "verb"
        ],
        "stage": 5
    },
    {
        "qLa": "cust\u00c5\u008ds, cust\u00c5\u008ddis, m.f.",
        "aLa": [
            "custos"
        ],
        "qEn": "guard",
        "aEn": [
            "guard"
        ],
        "type": [
            "noun"
        ],
        "stage": 13
    },
    {
        "qLa": "d\u00c4\u201c + abl (also used as prefix with verbs)",
        "aLa": [
            "de"
        ],
        "qEn": "from, down from; about (as prefix = down)",
        "aEn": [
            "from",
            "down from",
            "about"
        ],
        "type": [
            "preposition"
        ],
        "stage": 11
    },
    {
        "qLa": "dea, deae, f.",
        "aLa": [
            "dea"
        ],
        "qEn": "goddess",
        "aEn": [
            "goddess"
        ],
        "type": [
            "noun"
        ],
        "stage": 18
    },
    {
        "qLa": "d\u00c4\u201cbe\u00c5\u008d, d\u00c4\u201cb\u00c4\u201cre, d\u00c4\u201cbu\u00c4\u00ab, d\u00c4\u201cbitus",
        "aLa": [
            "debeo",
            "debere"
        ],
        "qEn": "owe, ought, should, must",
        "aEn": [
            "owe",
            "ought",
            "should",
            "must"
        ],
        "type": [
            "verb"
        ],
        "stage": 15
    },
    {
        "qLa": "decem (indecl.)",
        "aLa": [
            "decem"
        ],
        "qEn": "ten",
        "aEn": [
            "ten"
        ],
        "type": [
            "adjective"
        ],
        "stage": 20
    },
    {
        "qLa": "deinde (indecl.)",
        "aLa": [
            "deinde",
            "tum"
        ],
        "qEn": "then",
        "aEn": [
            "then"
        ],
        "type": [
            "adverb"
        ],
        "stage": 16
    },
    {
        "qLa": "d\u00c4\u201cle\u00c5\u008d, d\u00c4\u201cl\u00c4\u201cre, d\u00c4\u201cl\u00c4\u201cv\u00c4\u00ab, d\u00c4\u201cl\u00c4\u201ctus",
        "aLa": [
            "deleo",
            "delere"
        ],
        "qEn": "destroy",
        "aEn": [
            "destroy"
        ],
        "type": [
            "verb"
        ],
        "stage": 14
    },
    {
        "qLa": "d\u00c4\u201csp\u00c4\u201cr\u00c5\u008d, d\u00c4\u201csp\u00c4\u201cr\u00c4\u0081re, d\u00c4\u201csp\u00c4\u201cr\u00c4\u0081v\u00c4\u00ab, d\u00c4\u201csp\u00c4\u201cr\u00c4\u0081tus",
        "aLa": [
            "despero",
            "desperare"
        ],
        "qEn": "despair",
        "aEn": [
            "despair"
        ],
        "type": [
            "verb"
        ],
        "stage": 20
    },
    {
        "qLa": "deus, de\u00c4\u00ab, m.",
        "aLa": [
            "deus"
        ],
        "qEn": "god",
        "aEn": [
            "god"
        ],
        "type": [
            "noun"
        ],
        "stage": 14
    },
    {
        "qLa": "d\u00c4\u00abc\u00c5\u008d, d\u00c4\u00abcere, d\u00c4\u00abx\u00c4\u00ab, dictus",
        "aLa": [
            "dico",
            "dicere",
            "inquit"
        ],
        "qEn": "say",
        "aEn": [
            "say"
        ],
        "type": [
            "verb"
        ],
        "stage": 13
    },
    {
        "qLa": "di\u00c4\u201cs, di\u00c4\u201c\u00c4\u00ab, m.",
        "aLa": [
            "dies"
        ],
        "qEn": "day",
        "aEn": [
            "day"
        ],
        "type": [
            "noun"
        ],
        "stage": 9
    },
    {
        "qLa": "difficilis, difficile",
        "aLa": [
            "difficilis"
        ],
        "qEn": "difficult",
        "aEn": [
            "difficult"
        ],
        "type": [
            "adjective"
        ],
        "stage": 14
    },
    {
        "qLa": "d\u00c4\u00abrus, d\u00c4\u00abra, d\u00c4\u00abrum",
        "aLa": [
            "dirus"
        ],
        "qEn": "dreadful",
        "aEn": [
            "dreadful"
        ],
        "type": [
            "adjective"
        ],
        "stage": 0
    },
    {
        "qLa": "disc\u00c4\u201cd\u00c5\u008d, disc\u00c4\u201cdere, discess\u00c4\u00ab",
        "aLa": [
            "discedo",
            "discedere",
            "relinquo",
            "relinquere"
        ],
        "qEn": "depart, leave",
        "aEn": [
            "depart",
            "leave"
        ],
        "type": [
            "verb"
        ],
        "stage": 18
    },
    {
        "qLa": "di\u00c5\u00ab (indecl.)",
        "aLa": [
            "diu"
        ],
        "qEn": "for a long time",
        "aEn": [
            "for a long time"
        ],
        "type": [
            "adverb"
        ],
        "stage": 17
    },
    {
        "qLa": "d\u00c4\u00abves, d\u00c4\u00abvitis",
        "aLa": [
            "dives"
        ],
        "qEn": "rich",
        "aEn": [
            "rich"
        ],
        "type": [
            "adjective"
        ],
        "stage": 30
    },
    {
        "qLa": "d\u00c5\u008d, dare, ded\u00c4\u00ab, datus",
        "aLa": [
            "do",
            "dare"
        ],
        "qEn": "give",
        "aEn": [
            "give"
        ],
        "type": [
            "verb"
        ],
        "stage": 9
    },
    {
        "qLa": "dom\u00c4\u00ab",
        "aLa": [
            "domi"
        ],
        "qEn": "at home",
        "aEn": [
            "at home"
        ],
        "type": [
            "adverb"
        ],
        "stage": 0
    },
    {
        "qLa": "domina, dominae, f.",
        "aLa": [
            "domina"
        ],
        "qEn": "mistress",
        "aEn": [
            "mistress"
        ],
        "type": [
            "noun"
        ],
        "stage": 14
    },
    {
        "qLa": "dominus, domin\u00c4\u00ab, m.",
        "aLa": [
            "dominus"
        ],
        "qEn": "master",
        "aEn": [
            "master"
        ],
        "type": [
            "noun"
        ],
        "stage": 2
    },
    {
        "qLa": "domus, dom\u00c5\u00abs, f.",
        "aLa": [
            "domus"
        ],
        "qEn": "home, house",
        "aEn": [
            "home",
            "house"
        ],
        "type": [
            "noun"
        ],
        "stage": 20
    },
    {
        "qLa": "d\u00c5\u008dnum, d\u00c5\u008dn\u00c4\u00ab, n.",
        "aLa": [
            "donum"
        ],
        "qEn": "gift, present",
        "aEn": [
            "gift",
            "present"
        ],
        "type": [
            "noun"
        ],
        "stage": 14
    },
    {
        "qLa": "dormi\u00c5\u008d, dorm\u00c4\u00abre, dorm\u00c4\u00abv\u00c4\u00ab",
        "aLa": [
            "dormio",
            "dormire"
        ],
        "qEn": "sleep",
        "aEn": [
            "sleep"
        ],
        "type": [
            "verb"
        ],
        "stage": 2
    },
    {
        "qLa": "d\u00c5\u00abc\u00c5\u008d, d\u00c5\u00abcere, d\u00c5\u00abx\u00c4\u00ab, ductus",
        "aLa": [
            "duco",
            "ducere"
        ],
        "qEn": "lead, take",
        "aEn": [
            "lead",
            "take"
        ],
        "type": [
            "verb"
        ],
        "stage": 8
    },
    {
        "qLa": "dum",
        "aLa": [
            "dum"
        ],
        "qEn": "while",
        "aEn": [
            "while"
        ],
        "type": [
            "misc"
        ],
        "stage": 34
    },
    {
        "qLa": "duo, duae, duo",
        "aLa": [
            "duo"
        ],
        "qEn": "two",
        "aEn": [
            "two"
        ],
        "type": [
            "adjective"
        ],
        "stage": 12
    },
    {
        "qLa": "d\u00c5\u00abrus, d\u00c5\u00abra, d\u00c5\u00abrum",
        "aLa": [
            "durus"
        ],
        "qEn": "hard, harsh",
        "aEn": [
            "hard",
            "harsh"
        ],
        "type": [
            "adjective"
        ],
        "stage": 21
    },
    {
        "qLa": "dux, ducis, m.",
        "aLa": [
            "dux"
        ],
        "qEn": "leader",
        "aEn": [
            "leader"
        ],
        "type": [
            "noun"
        ],
        "stage": 0
    },
    {
        "qLa": "\u00c4\u201c, ex + abl (also used as prefix with verbs)",
        "aLa": [
            "e",
            "ex"
        ],
        "qEn": "from, out of (as prefix = out, away)",
        "aEn": [
            "from",
            "out of"
        ],
        "type": [
            "preposition"
        ],
        "stage": 4
    },
    {
        "qLa": "effugi\u00c5\u008d, effugere, eff\u00c5\u00abg\u00c4\u00ab",
        "aLa": [
            "effugio",
            "effugere"
        ],
        "qEn": "escape",
        "aEn": [
            "escape"
        ],
        "type": [
            "verb"
        ],
        "stage": 16
    },
    {
        "qLa": "ego, me\u00c4\u00ab",
        "aLa": [
            "ego",
            "mei"
        ],
        "qEn": "I, me",
        "aEn": [
            "I",
            "me"
        ],
        "type": [
            "pronoun"
        ],
        "stage": 4
    },
    {
        "qLa": "\u00c4\u201cgredior, \u00c4\u201cgred\u00c4\u00ab, \u00c4\u201cgressus sum",
        "aLa": [
            "egredior",
            "egredi"
        ],
        "qEn": "go out",
        "aEn": [
            "go out"
        ],
        "type": [
            "verb"
        ],
        "stage": 34
    },
    {
        "qLa": "em\u00c5\u008d, emere, \u00c4\u201cm\u00c4\u00ab, \u00c4\u201cmptus",
        "aLa": [
            "emo",
            "emere"
        ],
        "qEn": "buy",
        "aEn": [
            "buy"
        ],
        "type": [
            "verb"
        ],
        "stage": 6
    },
    {
        "qLa": "enim (indecl.)",
        "aLa": [
            "enim",
            "nam"
        ],
        "qEn": "for",
        "aEn": [
            "for"
        ],
        "type": [
            "misc"
        ],
        "stage": 23
    },
    {
        "qLa": "e\u00c5\u008d, \u00c4\u00abre, i\u00c4\u00ab",
        "aLa": [
            "eo",
            "ire"
        ],
        "qEn": "go",
        "aEn": [
            "go"
        ],
        "type": [
            "verb"
        ],
        "stage": 11
    },
    {
        "qLa": "epistula, epistulae, f.",
        "aLa": [
            "epistula"
        ],
        "qEn": "letter",
        "aEn": [
            "letter"
        ],
        "type": [
            "noun"
        ],
        "stage": 12
    },
    {
        "qLa": "equus, equ\u00c4\u00ab, m.",
        "aLa": [
            "equus"
        ],
        "qEn": "horse",
        "aEn": [
            "horse"
        ],
        "type": [
            "noun"
        ],
        "stage": 15
    },
    {
        "qLa": "et (indecl.)",
        "aLa": [
            "ac",
            "atque",
            "et",
            "-que",
            "que"
        ],
        "qEn": "and",
        "aEn": [
            "and"
        ],
        "type": [
            "misc"
        ],
        "stage": 3
    },
    {
        "qLa": "etiam (indecl.)",
        "aLa": [
            "etiam",
            "quoque"
        ],
        "qEn": "also, even",
        "aEn": [
            "also",
            "even"
        ],
        "type": [
            "adverb"
        ],
        "stage": 15
    },
    {
        "qLa": "exspect\u00c5\u008d, exspect\u00c4\u0081re, exspect\u00c4\u0081v\u00c4\u00ab, exspect\u00c4\u0081tus",
        "aLa": [
            "exspecto",
            "exspectare"
        ],
        "qEn": "wait for",
        "aEn": [
            "wait for"
        ],
        "type": [
            "verb"
        ],
        "stage": 3
    },
    {
        "qLa": "facilis, facile",
        "aLa": [
            "facilis"
        ],
        "qEn": "easy",
        "aEn": [
            "easy"
        ],
        "type": [
            "adjective"
        ],
        "stage": 17
    },
    {
        "qLa": "faci\u00c5\u008d, facere, f\u00c4\u201cc\u00c4\u00ab, factus",
        "aLa": [
            "facio",
            "facere"
        ],
        "qEn": "make, do",
        "aEn": [
            "make",
            "do"
        ],
        "type": [
            "verb"
        ],
        "stage": 7
    },
    {
        "qLa": "f\u00c4\u201cmina, f\u00c4\u201cminae, f.",
        "aLa": [
            "femina"
        ],
        "qEn": "woman",
        "aEn": [
            "woman"
        ],
        "type": [
            "noun"
        ],
        "stage": 5
    },
    {
        "qLa": "fer\u00c5\u008d, ferre, tul\u00c4\u00ab, l\u00c4\u0081tus",
        "aLa": [
            "fero",
            "ferre",
            "porto",
            "portare"
        ],
        "qEn": "bring, carry, bear",
        "aEn": [
            "bring",
            "carry",
            "bear"
        ],
        "type": [
            "verb"
        ],
        "stage": 9
    },
    {
        "qLa": "fer\u00c5\u008dx, fer\u00c5\u008dcis",
        "aLa": [
            "ferox"
        ],
        "qEn": "fierce, ferocious",
        "aEn": [
            "fierce",
            "ferocious"
        ],
        "type": [
            "adjective"
        ],
        "stage": 8
    },
    {
        "qLa": "fest\u00c4\u00abn\u00c5\u008d, fest\u00c4\u00abn\u00c4\u0081re, fest\u00c4\u00abn\u00c4\u0081v\u00c4\u00ab",
        "aLa": [
            "festino",
            "festinare"
        ],
        "qEn": "hurry",
        "aEn": [
            "hurry"
        ],
        "type": [
            "verb"
        ],
        "stage": 6
    },
    {
        "qLa": "fid\u00c4\u201clis, fid\u00c4\u201cle",
        "aLa": [
            "fidelis"
        ],
        "qEn": "faithful, loyal",
        "aEn": [
            "faithful",
            "loyal"
        ],
        "type": [
            "adjective"
        ],
        "stage": 14
    },
    {
        "qLa": "f\u00c4\u00ablia, f\u00c4\u00abliae, f.",
        "aLa": [
            "filia"
        ],
        "qEn": "daughter",
        "aEn": [
            "daughter"
        ],
        "type": [
            "noun"
        ],
        "stage": 19
    },
    {
        "qLa": "f\u00c4\u00ablius, f\u00c4\u00abli\u00c4\u00ab, m.",
        "aLa": [
            "filius"
        ],
        "qEn": "son",
        "aEn": [
            "son"
        ],
        "type": [
            "noun"
        ],
        "stage": 1
    },
    {
        "qLa": "fl\u00c5\u00abmen, fl\u00c5\u00abminis, n.",
        "aLa": [
            "flumen"
        ],
        "qEn": "river",
        "aEn": [
            "river"
        ],
        "type": [
            "noun"
        ],
        "stage": 24
    },
    {
        "qLa": "forte (indecl.)",
        "aLa": [
            "forte"
        ],
        "qEn": "by chance",
        "aEn": [
            "by chance"
        ],
        "type": [
            "adverb"
        ],
        "stage": 19
    },
    {
        "qLa": "fortis, forte",
        "aLa": [
            "fortis"
        ],
        "qEn": "brave",
        "aEn": [
            "brave"
        ],
        "type": [
            "adjective"
        ],
        "stage": 6
    },
    {
        "qLa": "forum, for\u00c4\u00ab, n.",
        "aLa": [
            "forum"
        ],
        "qEn": "forum, market place",
        "aEn": [
            "forum",
            "market place"
        ],
        "type": [
            "noun"
        ],
        "stage": 0
    },
    {
        "qLa": "frang\u00c5\u008d, frangere, fr\u00c4\u201cg\u00c4\u00ab, fr\u00c4\u0081ctus",
        "aLa": [
            "frango",
            "frangere"
        ],
        "qEn": "break",
        "aEn": [
            "break"
        ],
        "type": [
            "verb"
        ],
        "stage": 34
    },
    {
        "qLa": "fr\u00c4\u0081ter, fr\u00c4\u0081tris, m.",
        "aLa": [
            "frater"
        ],
        "qEn": "brother",
        "aEn": [
            "brother"
        ],
        "type": [
            "noun"
        ],
        "stage": 10
    },
    {
        "qLa": "fr\u00c5\u00abstr\u00c4\u0081 (indecl.)",
        "aLa": [
            "frustra"
        ],
        "qEn": "in vain",
        "aEn": [
            "in vain"
        ],
        "type": [
            "adverb"
        ],
        "stage": 12
    },
    {
        "qLa": "fugi\u00c5\u008d, fugere, f\u00c5\u00abg\u00c4\u00ab",
        "aLa": [
            "fugio",
            "fugere"
        ],
        "qEn": "run away, flee",
        "aEn": [
            "run away",
            "flee"
        ],
        "type": [
            "verb"
        ],
        "stage": 12
    },
    {
        "qLa": "ger\u00c5\u008d, gerere, gess\u00c4\u00ab, gestus",
        "aLa": [
            "gero",
            "gerere"
        ],
        "qEn": "wear (clothes), wage (war)",
        "aEn": [
            "wear",
            "wage"
        ],
        "type": [
            "verb"
        ],
        "stage": 23
    },
    {
        "qLa": "gladius, gladi\u00c4\u00ab, m.",
        "aLa": [
            "ferrum",
            "gladius"
        ],
        "qEn": "sword",
        "aEn": [
            "sword"
        ],
        "type": [
            "noun"
        ],
        "stage": 8
    },
    {
        "qLa": "gravis, grave",
        "aLa": [
            "gravis"
        ],
        "qEn": "heavy, serious",
        "aEn": [
            "heavy",
            "serious"
        ],
        "type": [
            "adjective"
        ],
        "stage": 21
    },
    {
        "qLa": "habe\u00c5\u008d, hab\u00c4\u201cre, habu\u00c4\u00ab, habitus",
        "aLa": [
            "habeo",
            "habere"
        ],
        "qEn": "have",
        "aEn": [
            "have"
        ],
        "type": [
            "verb"
        ],
        "stage": 4
    },
    {
        "qLa": "habit\u00c5\u008d, habit\u00c4\u0081re, habit\u00c4\u0081v\u00c4\u00ab, habit\u00c4\u0081tus",
        "aLa": [
            "habito",
            "habitare",
            "vivo",
            "vivere"
        ],
        "qEn": "live",
        "aEn": [
            "live"
        ],
        "type": [
            "verb"
        ],
        "stage": 10
    },
    {
        "qLa": "heri (indecl.)",
        "aLa": [
            "heri"
        ],
        "qEn": "yesterday",
        "aEn": [
            "yesterday"
        ],
        "type": [
            "adverb"
        ],
        "stage": 7
    },
    {
        "qLa": "h\u00c4\u00abc (indecl.)",
        "aLa": [
            "hic"
        ],
        "qEn": "here",
        "aEn": [
            "here"
        ],
        "type": [
            "adverb"
        ],
        "stage": 33
    },
    {
        "qLa": "hic, haec, hoc",
        "aLa": [
            "hic"
        ],
        "qEn": "this",
        "aEn": [
            "this"
        ],
        "type": [
            "pronoun"
        ],
        "stage": 8
    },
    {
        "qLa": "hodi\u00c4\u201c (indecl.)",
        "aLa": [
            "hodie"
        ],
        "qEn": "today",
        "aEn": [
            "today"
        ],
        "type": [
            "adverb"
        ],
        "stage": 5
    },
    {
        "qLa": "hom\u00c5\u008d, hominis, m.",
        "aLa": [
            "homo"
        ],
        "qEn": "man, human being, person",
        "aEn": [
            "man",
            "human being",
            "person"
        ],
        "type": [
            "noun"
        ],
        "stage": 9
    },
    {
        "qLa": "h\u00c5\u008dra, h\u00c5\u008drae, f.",
        "aLa": [
            "hora"
        ],
        "qEn": "hour",
        "aEn": [
            "hour"
        ],
        "type": [
            "noun"
        ],
        "stage": 21
    },
    {
        "qLa": "hortus, hort\u00c4\u00ab, m.",
        "aLa": [
            "hortus"
        ],
        "qEn": "garden",
        "aEn": [
            "garden"
        ],
        "type": [
            "noun"
        ],
        "stage": 1
    },
    {
        "qLa": "hostis, hostis, m.",
        "aLa": [
            "hostis"
        ],
        "qEn": "enemy",
        "aEn": [
            "enemy"
        ],
        "type": [
            "noun"
        ],
        "stage": 22
    },
    {
        "qLa": "iace\u00c5\u008d, iac\u00c4\u201cre, iacu\u00c4\u00ab",
        "aLa": [
            "iaceo",
            "iacere"
        ],
        "qEn": "lie (positional)",
        "aEn": [
            "lie"
        ],
        "type": [
            "verb"
        ],
        "stage": 12
    },
    {
        "qLa": "iaci\u00c5\u008d, iacere, i\u00c4\u201cc\u00c4\u00ab, iactus",
        "aLa": [
            "iacio",
            "iacere"
        ],
        "qEn": "throw",
        "aEn": [
            "throw"
        ],
        "type": [
            "verb"
        ],
        "stage": 23
    },
    {
        "qLa": "iam (indecl.)",
        "aLa": [
            "iam"
        ],
        "qEn": "now, already",
        "aEn": [
            "now",
            "already"
        ],
        "type": [
            "adverb"
        ],
        "stage": 12
    },
    {
        "qLa": "i\u00c4\u0081nua, i\u00c4\u0081nuae, f.",
        "aLa": [
            "ianua"
        ],
        "qEn": "door",
        "aEn": [
            "door"
        ],
        "type": [
            "noun"
        ],
        "stage": 3
    },
    {
        "qLa": "ibi (indecl.)",
        "aLa": [
            "ibi"
        ],
        "qEn": "there",
        "aEn": [
            "there"
        ],
        "type": [
            "adverb"
        ],
        "stage": 18
    },
    {
        "qLa": "igitur (indecl.)",
        "aLa": [
            "igitur",
            "itaque"
        ],
        "qEn": "therefore, and so",
        "aEn": [
            "therefore",
            "and so"
        ],
        "type": [
            "adverb"
        ],
        "stage": 12
    },
    {
        "qLa": "ignis, ignis, m.",
        "aLa": [
            "ignis"
        ],
        "qEn": "fire",
        "aEn": [
            "fire"
        ],
        "type": [
            "noun"
        ],
        "stage": 36
    },
    {
        "qLa": "ille, illa, illud",
        "aLa": [
            "ille"
        ],
        "qEn": "that, he, she, it",
        "aEn": [
            "that",
            "he",
            "she",
            "it"
        ],
        "type": [
            "pronoun"
        ],
        "stage": 9
    },
    {
        "qLa": "imper\u00c4\u0081tor, imper\u00c4\u0081t\u00c5\u008dris, m.",
        "aLa": [
            "imperator"
        ],
        "qEn": "emperor, commander, general",
        "aEn": [
            "emperor",
            "commander",
            "general"
        ],
        "type": [
            "noun"
        ],
        "stage": 16
    },
    {
        "qLa": "imperium, imperi\u00c4\u00ab, n.",
        "aLa": [
            "imperium"
        ],
        "qEn": "empire, power, command",
        "aEn": [
            "empire",
            "power",
            "command"
        ],
        "type": [
            "noun"
        ],
        "stage": 10
    },
    {
        "qLa": "imper\u00c5\u008d, imper\u00c4\u0081re, imper\u00c4\u0081v\u00c4\u00ab, imper\u00c4\u0081tus + dat",
        "aLa": [
            "impero",
            "imperare",
            "iubeo",
            "iubere"
        ],
        "qEn": "order, command",
        "aEn": [
            "order",
            "command"
        ],
        "type": [
            "verb"
        ],
        "stage": 27
    },
    {
        "qLa": "in + acc (also used as prefix with verbs)",
        "aLa": [
            "in"
        ],
        "qEn": "into, onto",
        "aEn": [
            "into",
            "onto"
        ],
        "type": [
            "preposition"
        ],
        "stage": 1
    },
    {
        "qLa": "in + abl (also used as prefix with verbs)",
        "aLa": [
            "in"
        ],
        "qEn": "in, on",
        "aEn": [
            "in",
            "on"
        ],
        "type": [
            "preposition"
        ],
        "stage": 1
    },
    {
        "qLa": "incend\u00c5\u008d, incendere, incend\u00c4\u00ab, inc\u00c4\u201cnsus",
        "aLa": [
            "iincendo"
        ],
        "qEn": "burn, set on fire",
        "aEn": [
            "burn",
            "set on fire"
        ],
        "type": [
            "verb"
        ],
        "stage": 27
    },
    {
        "qLa": "\u00c4\u00abnf\u00c4\u201cl\u00c4\u00abx, \u00c4\u00abnf\u00c4\u201cl\u00c4\u00abcis",
        "aLa": [
            "infelix"
        ],
        "qEn": "unlucky, unhappy",
        "aEn": [
            "unlucky",
            "unhappy"
        ],
        "type": [
            "adjective"
        ],
        "stage": 21
    },
    {
        "qLa": "ing\u00c4\u201cns, ingentis",
        "aLa": [
            "ingens"
        ],
        "qEn": "huge",
        "aEn": [
            "huge"
        ],
        "type": [
            "adjective"
        ],
        "stage": 7
    },
    {
        "qLa": "ingredior, ingred\u00c4\u00ab, ingressus sum",
        "aLa": [
            "ingredior",
            "ingredi"
        ],
        "qEn": "enter",
        "aEn": [
            "enter"
        ],
        "type": [
            "verb"
        ],
        "stage": 34
    },
    {
        "qLa": "inquit",
        "aLa": [
            "dico",
            "dicere",
            "inquit"
        ],
        "qEn": "say, said",
        "aEn": [
            "say",
            "said"
        ],
        "type": [
            "verb"
        ],
        "stage": 4
    },
    {
        "qLa": "\u00c4\u00abnsula, \u00c4\u00abnsulae, f.",
        "aLa": [
            "insula"
        ],
        "qEn": "island, block of flats",
        "aEn": [
            "island",
            "block of flats"
        ],
        "type": [
            "noun"
        ],
        "stage": 17
    },
    {
        "qLa": "intelleg\u00c5\u008d, intellegere, intell\u00c4\u201cx\u00c4\u00ab, intell\u00c4\u201cctus",
        "aLa": [
            "intellego",
            "intellegere"
        ],
        "qEn": "understand, realise",
        "aEn": [
            "understand",
            "realise"
        ],
        "type": [
            "verb"
        ],
        "stage": 7
    },
    {
        "qLa": "inter + acc",
        "aLa": [
            "inter"
        ],
        "qEn": "among, between",
        "aEn": [
            "among",
            "between"
        ],
        "type": [
            "preposition"
        ],
        "stage": 16
    },
    {
        "qLa": "interea (indecl.)",
        "aLa": [
            "interea"
        ],
        "qEn": "meanwhile",
        "aEn": [
            "meanwhile"
        ],
        "type": [
            "adverb"
        ],
        "stage": 24
    },
    {
        "qLa": "intr\u00c5\u008d, intr\u00c4\u0081re, intr\u00c4\u0081v\u00c4\u00ab, intr\u00c4\u0081tus",
        "aLa": [
            "intro",
            "intrare"
        ],
        "qEn": "enter",
        "aEn": [
            "enter"
        ],
        "type": [
            "verb"
        ],
        "stage": 2
    },
    {
        "qLa": "inveni\u00c5\u008d, inven\u00c4\u00abre, inv\u00c4\u201cn\u00c4\u00ab, inventus",
        "aLa": [
            "invenio",
            "invenire"
        ],
        "qEn": "find",
        "aEn": [
            "find"
        ],
        "type": [
            "verb"
        ],
        "stage": 10
    },
    {
        "qLa": "\u00c4\u00abra, \u00c4\u00abrae, f.",
        "aLa": [
            "ira"
        ],
        "qEn": "anger",
        "aEn": [
            "anger"
        ],
        "type": [
            "noun"
        ],
        "stage": 28
    },
    {
        "qLa": "\u00c4\u00abr\u00c4\u0081tus, \u00c4\u00abr\u00c4\u0081ta, \u00c4\u00abr\u00c4\u0081tum",
        "aLa": [
            "iratus"
        ],
        "qEn": "angry",
        "aEn": [
            "angry"
        ],
        "type": [
            "adjective"
        ],
        "stage": 3
    },
    {
        "qLa": "is, ea, id",
        "aLa": [
            "is"
        ],
        "qEn": "this, that, he, she, it, them",
        "aEn": [
            "this",
            "that",
            "he",
            "she",
            "it",
            "them"
        ],
        "type": [
            "pronoun"
        ],
        "stage": 8
    },
    {
        "qLa": "ita (indecl.)",
        "aLa": [
            "ita",
            "sic"
        ],
        "qEn": "in this way, so",
        "aEn": [
            "in this way",
            "so"
        ],
        "type": [
            "adverb"
        ],
        "stage": 16
    },
    {
        "qLa": "ita v\u00c4\u201cr\u00c5\u008d (indecl.)",
        "aLa": [
            "ita vero"
        ],
        "qEn": "yes",
        "aEn": [
            "yes"
        ],
        "type": [
            "adverb"
        ],
        "stage": 13
    },
    {
        "qLa": "itaque (indecl.)",
        "aLa": [
            "igitur",
            "itaque"
        ],
        "qEn": "and so, therefore",
        "aEn": [
            "and so",
            "therefore"
        ],
        "type": [
            "adverb"
        ],
        "stage": 17
    },
    {
        "qLa": "iter, itineris, n.",
        "aLa": [
            "iter"
        ],
        "qEn": "journey, route, way",
        "aEn": [
            "journey",
            "route",
            "way"
        ],
        "type": [
            "noun"
        ],
        "stage": 19
    },
    {
        "qLa": "iterum (indecl.)",
        "aLa": [
            "iterum"
        ],
        "qEn": "again",
        "aEn": [
            "again"
        ],
        "type": [
            "adverb"
        ],
        "stage": 9
    },
    {
        "qLa": "iube\u00c5\u008d, iub\u00c4\u201cre, iuss\u00c4\u00ab, iussus",
        "aLa": [
            "impero",
            "imperare",
            "iubeo",
            "iubere"
        ],
        "qEn": "order",
        "aEn": [
            "order"
        ],
        "type": [
            "verb"
        ],
        "stage": 21
    },
    {
        "qLa": "iuvenis, iuvenis (m.)",
        "aLa": [
            "iuvenis"
        ],
        "qEn": "young; young man",
        "aEn": [
            "young",
            "young man"
        ],
        "type": [
            "adjective",
            "noun"
        ],
        "stage": 5
    },
    {
        "qLa": "labor, lab\u00c5\u008dris, m.",
        "aLa": [
            "labor",
            "laboro"
        ],
        "qEn": "work",
        "aEn": [
            "work"
        ],
        "type": [
            "noun"
        ],
        "stage": 0
    },
    {
        "qLa": "lab\u00c5\u008dr\u00c5\u008d, lab\u00c5\u008dr\u00c4\u0081re, lab\u00c5\u008dr\u00c4\u0081v\u00c4\u00ab",
        "aLa": [
            "labor",
            "laboro",
            "laborare"
        ],
        "qEn": "work",
        "aEn": [
            "work"
        ],
        "type": [
            "verb"
        ],
        "stage": 1
    },
    {
        "qLa": "lacrim\u00c5\u008d, lacrim\u00c4\u0081re, lacrim\u00c4\u0081v\u00c4\u00ab",
        "aLa": [
            "lacrimo",
            "lacrimare"
        ],
        "qEn": "weep, cry",
        "aEn": [
            "weep",
            "cry"
        ],
        "type": [
            "verb"
        ],
        "stage": 7
    },
    {
        "qLa": "laetus, laeta, laetum",
        "aLa": [
            "laetus"
        ],
        "qEn": "happy",
        "aEn": [
            "happy"
        ],
        "type": [
            "adjective"
        ],
        "stage": 2
    },
    {
        "qLa": "l\u00c4\u0081tus, l\u00c4\u0081ta, l\u00c4\u0081tum",
        "aLa": [
            "latus"
        ],
        "qEn": "wide",
        "aEn": [
            "wide"
        ],
        "type": [
            "adjective"
        ],
        "stage": 0
    },
    {
        "qLa": "laud\u00c5\u008d, laud\u00c4\u0081re, laud\u00c4\u0081v\u00c4\u00ab, laud\u00c4\u0081tus",
        "aLa": [
            "laudo",
            "laudare"
        ],
        "qEn": "praise",
        "aEn": [
            "praise"
        ],
        "type": [
            "verb"
        ],
        "stage": 2
    },
    {
        "qLa": "l\u00c4\u201cg\u00c4\u0081tus, l\u00c4\u201cg\u00c4\u0081t\u00c4\u00ab, m.",
        "aLa": [
            "imperator",
            "legatus"
        ],
        "qEn": "commander",
        "aEn": [
            "commander"
        ],
        "type": [
            "noun"
        ],
        "stage": 26
    },
    {
        "qLa": "legi\u00c5\u008d, legi\u00c5\u008dnis, f.",
        "aLa": [
            "legio"
        ],
        "qEn": "legion",
        "aEn": [
            "legion"
        ],
        "type": [
            "noun"
        ],
        "stage": 26
    },
    {
        "qLa": "leg\u00c5\u008d, legere, l\u00c4\u201cg\u00c4\u00ab, l\u00c4\u201cctus",
        "aLa": [
            "lego",
            "legere"
        ],
        "qEn": "read, choose",
        "aEn": [
            "read",
            "choose"
        ],
        "type": [
            "verb"
        ],
        "stage": 11
    },
    {
        "qLa": "lent\u00c4\u201c (indecl.)",
        "aLa": [
            "lente"
        ],
        "qEn": "slowly",
        "aEn": [
            "slowly"
        ],
        "type": [
            "adverb"
        ],
        "stage": 15
    },
    {
        "qLa": "libenter (indecl.)",
        "aLa": [
            "libenter"
        ],
        "qEn": "willingly, gladly",
        "aEn": [
            "willingly",
            "gladly"
        ],
        "type": [
            "adverb"
        ],
        "stage": 18
    },
    {
        "qLa": "l\u00c4\u00abber\u00c4\u00ab, l\u00c4\u00abber\u00c5\u008drum, m.pl.",
        "aLa": [
            "liberi"
        ],
        "qEn": "children",
        "aEn": [
            "children"
        ],
        "type": [
            "noun"
        ],
        "stage": 29
    },
    {
        "qLa": "l\u00c4\u00abber\u00c5\u008d, l\u00c4\u00abber\u00c4\u0081re, l\u00c4\u00abber\u00c4\u0081v\u00c4\u00ab, l\u00c4\u00abber\u00c4\u0081tus",
        "aLa": [
            "libero",
            "liberare"
        ],
        "qEn": "free, set free",
        "aEn": [
            "free",
            "set free"
        ],
        "type": [
            "verb"
        ],
        "stage": 20
    },
    {
        "qLa": "l\u00c4\u00abbertus, l\u00c4\u00abbert\u00c4\u00ab, m.",
        "aLa": [
            "libertus"
        ],
        "qEn": "freedman, ex-slave",
        "aEn": [
            "freedman",
            "ex-slave",
            "ex slave"
        ],
        "type": [
            "noun"
        ],
        "stage": 6
    },
    {
        "qLa": "locus, loc\u00c4\u00ab, m.",
        "aLa": [
            "locus",
            "pono"
        ],
        "qEn": "place",
        "aEn": [
            "place"
        ],
        "type": [
            "noun"
        ],
        "stage": 19
    },
    {
        "qLa": "longus, longa, longum",
        "aLa": [
            "longus"
        ],
        "qEn": "long",
        "aEn": [
            "long"
        ],
        "type": [
            "adjective"
        ],
        "stage": 0
    },
    {
        "qLa": "loquor, loqu\u00c4\u00ab, loc\u00c5\u00abtus sum",
        "aLa": [
            "loquor",
            "loqui"
        ],
        "qEn": "speak",
        "aEn": [
            "speak"
        ],
        "type": [
            "verb"
        ],
        "stage": 34
    },
    {
        "qLa": "l\u00c5\u00abx, l\u00c5\u00abcis, f.",
        "aLa": [
            "lux"
        ],
        "qEn": "light, daylight",
        "aEn": [
            "light",
            "daylight"
        ],
        "type": [
            "noun"
        ],
        "stage": 0
    },
    {
        "qLa": "magnopere (indecl.)",
        "aLa": [
            "magnopere",
            "valde"
        ],
        "qEn": "greatly, very much",
        "aEn": [
            "greatly",
            "very much"
        ],
        "type": [
            "adverb"
        ],
        "stage": 30
    },
    {
        "qLa": "magnus, magna, magnum",
        "aLa": [
            "magnus"
        ],
        "qEn": "big, large, great",
        "aEn": [
            "big",
            "large",
            "great"
        ],
        "type": [
            "adjective"
        ],
        "stage": 3
    },
    {
        "qLa": "maior, maius (irregular comparative)",
        "aLa": [
            "maior"
        ],
        "qEn": "bigger, larger, greater",
        "aEn": [
            "bigger",
            "larger",
            "greater"
        ],
        "type": [
            "adjective"
        ],
        "stage": 0
    },
    {
        "qLa": "malus, mala, malum",
        "aLa": [
            "malus"
        ],
        "qEn": "evil, bad",
        "aEn": [
            "evil",
            "bad"
        ],
        "type": [
            "adjective"
        ],
        "stage": 28
    },
    {
        "qLa": "mane\u00c5\u008d, man\u00c4\u201cre, m\u00c4\u0081ns\u00c4\u00ab",
        "aLa": [
            "maneo",
            "manere"
        ],
        "qEn": "remain, stay",
        "aEn": [
            "remain",
            "stay"
        ],
        "type": [
            "verb"
        ],
        "stage": 9
    },
    {
        "qLa": "manus, man\u00c5\u00abs, f.",
        "aLa": [
            "manus"
        ],
        "qEn": "hand, group of people",
        "aEn": [
            "hand",
            "group of people"
        ],
        "type": [
            "noun"
        ],
        "stage": 18
    },
    {
        "qLa": "mare, maris, n.",
        "aLa": [
            "mare"
        ],
        "qEn": "sea",
        "aEn": [
            "sea"
        ],
        "type": [
            "noun"
        ],
        "stage": 15
    },
    {
        "qLa": "mar\u00c4\u00abtus, mar\u00c4\u00abt\u00c4\u00ab, m.",
        "aLa": [
            "maritus"
        ],
        "qEn": "husband",
        "aEn": [
            "husband"
        ],
        "type": [
            "noun"
        ],
        "stage": 14
    },
    {
        "qLa": "m\u00c4\u0081ter, m\u00c4\u0081tris, f.",
        "aLa": [
            "mater"
        ],
        "qEn": "mother",
        "aEn": [
            "mother"
        ],
        "type": [
            "noun"
        ],
        "stage": 1
    },
    {
        "qLa": "maximus, maxima, maximum",
        "aLa": [
            "maximus"
        ],
        "qEn": "the biggest, the greatest, very big, very great",
        "aEn": [
            "the biggest",
            "the greatest",
            "biggest",
            "greatest",
            "very big",
            "very great"
        ],
        "type": [
            "adjective"
        ],
        "stage": 17
    },
    {
        "qLa": "medius, media, medium",
        "aLa": [
            "medius"
        ],
        "qEn": "middle, middle of",
        "aEn": [
            "middle",
            "middle of"
        ],
        "type": [
            "adjective"
        ],
        "stage": 9
    },
    {
        "qLa": "melior, melius (irregular comparative)",
        "aLa": [
            "melior"
        ],
        "qEn": "better",
        "aEn": [
            "better"
        ],
        "type": [
            "adjective"
        ],
        "stage": 16
    },
    {
        "qLa": "meus, mea, meum",
        "aLa": [
            "meus"
        ],
        "qEn": "my",
        "aEn": [
            "my"
        ],
        "type": [
            "adjective"
        ],
        "stage": 5
    },
    {
        "qLa": "m\u00c4\u00ables, m\u00c4\u00ablitis, m.",
        "aLa": [
            "miles"
        ],
        "qEn": "soldier",
        "aEn": [
            "soldier"
        ],
        "type": [
            "noun"
        ],
        "stage": 18
    },
    {
        "qLa": "m\u00c4\u00ablle, pl. m\u00c4\u00ablia",
        "aLa": [
            "mille"
        ],
        "qEn": "thousand",
        "aEn": [
            "thousand"
        ],
        "type": [
            "noun"
        ],
        "stage": 28
    },
    {
        "qLa": "minim\u00c4\u201c (indecl.)",
        "aLa": [
            "minime"
        ],
        "qEn": "very little, least, no",
        "aEn": [
            "very little",
            "least",
            "no"
        ],
        "type": [
            "adverb"
        ],
        "stage": 11
    },
    {
        "qLa": "minimus, minima, minimum",
        "aLa": [
            "minimus"
        ],
        "qEn": "very little, very small",
        "aEn": [
            "very little",
            "very small"
        ],
        "type": [
            "adjective"
        ],
        "stage": 22
    },
    {
        "qLa": "minor, minus (irregular comparative)",
        "aLa": [
            "minor"
        ],
        "qEn": "smaller, less",
        "aEn": [
            "smaller",
            "less"
        ],
        "type": [
            "adjective"
        ],
        "stage": 0
    },
    {
        "qLa": "miser, misera, miserum",
        "aLa": [
            "miser",
            "tristis"
        ],
        "qEn": "miserable, wretched, sad",
        "aEn": [
            "miserable",
            "wretched",
            "sad"
        ],
        "type": [
            "adjective"
        ],
        "stage": 15
    },
    {
        "qLa": "mitt\u00c5\u008d, mittere, m\u00c4\u00abs\u00c4\u00ab, missus",
        "aLa": [
            "mitto",
            "mittere"
        ],
        "qEn": "send",
        "aEn": [
            "send"
        ],
        "type": [
            "verb"
        ],
        "stage": 12
    },
    {
        "qLa": "modus, mod\u00c4\u00ab, m.",
        "aLa": [
            "modus"
        ],
        "qEn": "manner, way, kind",
        "aEn": [
            "manner",
            "way",
            "kind"
        ],
        "type": [
            "noun"
        ],
        "stage": 23
    },
    {
        "qLa": "m\u00c5\u008dns, montis, m.",
        "aLa": [
            "mons"
        ],
        "qEn": "mountain",
        "aEn": [
            "mountain"
        ],
        "type": [
            "noun"
        ],
        "stage": 12
    },
    {
        "qLa": "morior, mor\u00c4\u00ab, mortuus sum",
        "aLa": [
            "morior",
            "mori"
        ],
        "qEn": "die",
        "aEn": [
            "die"
        ],
        "type": [
            "verb"
        ],
        "stage": 34
    },
    {
        "qLa": "mors, mortis, f.",
        "aLa": [
            "mors"
        ],
        "qEn": "death",
        "aEn": [
            "death"
        ],
        "type": [
            "noun"
        ],
        "stage": 20
    },
    {
        "qLa": "mox (indecl.)",
        "aLa": [
            "mox"
        ],
        "qEn": "soon",
        "aEn": [
            "soon"
        ],
        "type": [
            "adverb"
        ],
        "stage": 9
    },
    {
        "qLa": "mult\u00c5\u008d, multum (indecl.)",
        "aLa": [
            "multo",
            "multum",
            "multus"
        ],
        "qEn": "much",
        "aEn": [
            "much"
        ],
        "type": [
            "adverb"
        ],
        "stage": 0
    },
    {
        "qLa": "multus, multa, multum",
        "aLa": [
            "multus"
        ],
        "qEn": "much, many",
        "aEn": [
            "much",
            "many"
        ],
        "type": [
            "adjective"
        ],
        "stage": 5
    },
    {
        "qLa": "m\u00c5\u00abrus, m\u00c5\u00abr\u00c4\u00ab, m.",
        "aLa": [
            "murus"
        ],
        "qEn": "wall",
        "aEn": [
            "wall"
        ],
        "type": [
            "noun"
        ],
        "stage": 11
    },
    {
        "qLa": "nam (indecl.)",
        "aLa": [
            "enim",
            "nam"
        ],
        "qEn": "for",
        "aEn": [
            "for"
        ],
        "type": [
            "misc"
        ],
        "stage": 18
    },
    {
        "qLa": "n\u00c4\u0081rr\u00c5\u008d, n\u00c4\u0081rr\u00c4\u0081re, n\u00c4\u0081rr\u00c4\u0081v\u00c4\u00ab, n\u00c4\u0081rr\u00c4\u0081tus",
        "aLa": [
            "narro",
            "narrare",
            "refero",
            "referre"
        ],
        "qEn": "tell, relate",
        "aEn": [
            "tell",
            "relate"
        ],
        "type": [
            "verb"
        ],
        "stage": 7
    },
    {
        "qLa": "nauta, nautae, m.",
        "aLa": [
            "nauta"
        ],
        "qEn": "sailor",
        "aEn": [
            "sailor"
        ],
        "type": [
            "noun"
        ],
        "stage": 15
    },
    {
        "qLa": "n\u00c4\u0081vig\u00c5\u008d, n\u00c4\u0081vig\u00c4\u0081re, n\u00c4\u0081vig\u00c4\u0081v\u00c4\u00ab",
        "aLa": [
            "navigo",
            "navigare"
        ],
        "qEn": "sail",
        "aEn": [
            "sail"
        ],
        "type": [
            "verb"
        ],
        "stage": 16
    },
    {
        "qLa": "n\u00c4\u0081vis, n\u00c4\u0081vis, f.",
        "aLa": [
            "navis"
        ],
        "qEn": "ship",
        "aEn": [
            "ship"
        ],
        "type": [
            "noun"
        ],
        "stage": 3
    },
    {
        "qLa": "n\u00c4\u201c (indecl.)",
        "aLa": [
            "ne"
        ],
        "qEn": "that ... not, so that ... not",
        "aEn": [
            "that not",
            "so that not"
        ],
        "type": [
            "misc"
        ],
        "stage": 31
    },
    {
        "qLa": "-ne (indecl.)",
        "aLa": [
            "-ne",
            "ne"
        ],
        "qEn": "introduces question",
        "aEn": [
            "introduces question"
        ],
        "type": [
            "misc"
        ],
        "stage": 0
    },
    {
        "qLa": "nec ... nec, neque ... neque (indecl.)",
        "aLa": [
            "nec nec",
            "neque neque"
        ],
        "qEn": "neither ... nor ...",
        "aEn": [
            "neither nor"
        ],
        "type": [
            "misc"
        ],
        "stage": 0
    },
    {
        "qLa": "necesse (indecl.)",
        "aLa": [
            "necesse"
        ],
        "qEn": "necessary",
        "aEn": [
            "necessary"
        ],
        "type": [
            "noun"
        ],
        "stage": 14
    },
    {
        "qLa": "nec\u00c5\u008d, nec\u00c4\u0081re, nec\u00c4\u0081v\u00c4\u00ab, nec\u00c4\u0081tus",
        "aLa": [
            "interficio",
            "interficere",
            "neco",
            "necare",
            "occido",
            "occidere"
        ],
        "qEn": "kill",
        "aEn": [
            "kill"
        ],
        "type": [
            "verb"
        ],
        "stage": 7
    },
    {
        "qLa": "n\u00c4\u201cm\u00c5\u008d, n\u00c4\u201cminis",
        "aLa": [
            "nemo"
        ],
        "qEn": "no one, nobody",
        "aEn": [
            "no one",
            "nobody"
        ],
        "type": [
            "noun"
        ],
        "stage": 18
    },
    {
        "qLa": "nescio, nesc\u00c4\u00abre, nesc\u00c4\u00abv\u00c4\u00ab",
        "aLa": [
            "nescio",
            "nescire"
        ],
        "qEn": "not know",
        "aEn": [
            "not know"
        ],
        "type": [
            "verb"
        ],
        "stage": 25
    },
    {
        "qLa": "nihil (indecl.)",
        "aLa": [
            "nihil"
        ],
        "qEn": "nothing",
        "aEn": [
            "nothing"
        ],
        "type": [
            "noun"
        ],
        "stage": 7
    },
    {
        "qLa": "n\u00c5\u008dl\u00c5\u008d, n\u00c5\u008dlle, n\u00c5\u008dlu\u00c4\u00ab",
        "aLa": [
            "nolo",
            "nolle"
        ],
        "qEn": "not want",
        "aEn": [
            "not want"
        ],
        "type": [
            "verb"
        ],
        "stage": 13
    },
    {
        "qLa": "n\u00c5\u008dmen, n\u00c5\u008dminis, n.",
        "aLa": [
            "nomen"
        ],
        "qEn": "name",
        "aEn": [
            "name"
        ],
        "type": [
            "noun"
        ],
        "stage": 25
    },
    {
        "qLa": "n\u00c5\u008dn (indecl.)",
        "aLa": [
            "non"
        ],
        "qEn": "not",
        "aEn": [
            "not"
        ],
        "type": [
            "adverb"
        ],
        "stage": 3
    },
    {
        "qLa": "n\u00c5\u008dnne? (indecl.)",
        "aLa": [
            "nonne"
        ],
        "qEn": "surely?",
        "aEn": [
            "surely"
        ],
        "type": [
            "adverb"
        ],
        "stage": 16
    },
    {
        "qLa": "n\u00c5\u008ds, nostrum",
        "aLa": [
            "nos"
        ],
        "qEn": "we, us",
        "aEn": [
            "we",
            "us"
        ],
        "type": [
            "pronoun"
        ],
        "stage": 10
    },
    {
        "qLa": "noster, nostra, nostrum",
        "aLa": [
            "noster"
        ],
        "qEn": "our",
        "aEn": [
            "our"
        ],
        "type": [
            "pronoun"
        ],
        "stage": 11
    },
    {
        "qLa": "novem (indecl.)",
        "aLa": [
            "novem"
        ],
        "qEn": "nine",
        "aEn": [
            "nine"
        ],
        "type": [
            "adjective"
        ],
        "stage": 20
    },
    {
        "qLa": "novus, nova, novum",
        "aLa": [
            "novus"
        ],
        "qEn": "new",
        "aEn": [
            "new"
        ],
        "type": [
            "adjective"
        ],
        "stage": 13
    },
    {
        "qLa": "nox, noctis, f.",
        "aLa": [
            "nox"
        ],
        "qEn": "night",
        "aEn": [
            "night"
        ],
        "type": [
            "noun"
        ],
        "stage": 22
    },
    {
        "qLa": "n\u00c5\u00abllus, n\u00c5\u00ablla, n\u00c5\u00abllum",
        "aLa": [
            "nullus"
        ],
        "qEn": "not any, no",
        "aEn": [
            "not any",
            "no"
        ],
        "type": [
            "adjective"
        ],
        "stage": 13
    },
    {
        "qLa": "num (indecl.)",
        "aLa": [
            "num"
        ],
        "qEn": "whether",
        "aEn": [
            "whether"
        ],
        "type": [
            "misc"
        ],
        "stage": 26
    },
    {
        "qLa": "num ... ? (indecl.)",
        "aLa": [
            "num"
        ],
        "qEn": "surely not?",
        "aEn": [
            "surely not"
        ],
        "type": [
            "misc"
        ],
        "stage": 14
    },
    {
        "qLa": "numquam (indecl.)",
        "aLa": [
            "numquam"
        ],
        "qEn": "never",
        "aEn": [
            "never"
        ],
        "type": [
            "adverb"
        ],
        "stage": 17
    },
    {
        "qLa": "nunc (indecl.)",
        "aLa": [
            "iam",
            "nunc"
        ],
        "qEn": "now",
        "aEn": [
            "now"
        ],
        "type": [
            "adverb"
        ],
        "stage": 11
    },
    {
        "qLa": "n\u00c5\u00abnti\u00c5\u008d, n\u00c5\u00abnti\u00c4\u0081re, n\u00c5\u00abnti\u00c4\u0081v\u00c4\u00ab, n\u00c5\u00abnti\u00c4\u0081tus",
        "aLa": [
            "nuntio",
            "nuntiare"
        ],
        "qEn": "announce, report",
        "aEn": [
            "announce",
            "report"
        ],
        "type": [
            "verb"
        ],
        "stage": 10
    },
    {
        "qLa": "n\u00c5\u00abntius, n\u00c5\u00abnti\u00c4\u00ab, m.",
        "aLa": [
            "nuntius"
        ],
        "qEn": "messenger, message, news",
        "aEn": [
            "messenger",
            "message",
            "news"
        ],
        "type": [
            "noun"
        ],
        "stage": 8
    },
    {
        "qLa": "occ\u00c4\u00abd\u00c5\u008d, occ\u00c4\u00abdere, occ\u00c4\u00abd\u00c4\u00ab, occ\u00c4\u00absus",
        "aLa": [
            "interficio",
            "interficere",
            "neco",
            "necare",
            "occido",
            "occidere"
        ],
        "qEn": "kill",
        "aEn": [
            "kill"
        ],
        "type": [
            "verb"
        ],
        "stage": 28
    },
    {
        "qLa": "oct\u00c5\u008d (indecl.)",
        "aLa": [
            "octo"
        ],
        "qEn": "eight",
        "aEn": [
            "eight"
        ],
        "type": [
            "adjective"
        ],
        "stage": 20
    },
    {
        "qLa": "offer\u00c5\u008d, offerre, obtul\u00c4\u00ab, obl\u00c4\u0081tus",
        "aLa": [
            "offero",
            "offerre"
        ],
        "qEn": "offer",
        "aEn": [
            "offer"
        ],
        "type": [
            "verb"
        ],
        "stage": 9
    },
    {
        "qLa": "\u00c5\u008dlim (indecl.)",
        "aLa": [
            "olim"
        ],
        "qEn": "once, some time ago",
        "aEn": [
            "once",
            "some time ago"
        ],
        "type": [
            "adverb"
        ],
        "stage": 6
    },
    {
        "qLa": "omnis, omne",
        "aLa": [
            "omnis"
        ],
        "qEn": "all, every",
        "aEn": [
            "all",
            "every"
        ],
        "type": [
            "adjective"
        ],
        "stage": 7
    },
    {
        "qLa": "oppugn\u00c5\u008d, oppugn\u00c4\u0081re, oppugn\u00c4\u0081v\u00c4\u00ab, oppugn\u00c4\u0081tus",
        "aLa": [
            "oppugno",
            "oppugnare",
            "peto",
            "petere"
        ],
        "qEn": "attack",
        "aEn": [
            "attack"
        ],
        "type": [
            "verb"
        ],
        "stage": 24
    },
    {
        "qLa": "optimus, optima, optimum",
        "aLa": [
            "optimus"
        ],
        "qEn": "the best, very good, excellent",
        "aEn": [
            "the best",
            "best",
            "very good",
            "excellent"
        ],
        "type": [
            "adjective"
        ],
        "stage": 5
    },
    {
        "qLa": "\u00c5\u008dr\u00c5\u008d, \u00c5\u008dr\u00c4\u0081re, \u00c5\u008dr\u00c4\u0081v\u00c4\u00ab, \u00c5\u008dr\u00c4\u0081tus",
        "aLa": [
            "oro",
            "orare"
        ],
        "qEn": "beg, beg for",
        "aEn": [
            "beg",
            "beg for"
        ],
        "type": [
            "verb"
        ],
        "stage": 0
    },
    {
        "qLa": "ostend\u00c5\u008d, ostendere, ostend\u00c4\u00ab, ostentus",
        "aLa": [
            "ostendo",
            "ostendere"
        ],
        "qEn": "show",
        "aEn": [
            "show"
        ],
        "type": [
            "verb"
        ],
        "stage": 9
    },
    {
        "qLa": "paene (indecl.)",
        "aLa": [
            "paene"
        ],
        "qEn": "almost, nearly",
        "aEn": [
            "almost",
            "nearly"
        ],
        "type": [
            "adverb"
        ],
        "stage": 12
    },
    {
        "qLa": "p\u00c4\u0081re\u00c5\u008d, p\u00c4\u0081r\u00c4\u201cre, p\u00c4\u0081ru\u00c4\u00ab + dat",
        "aLa": [
            "pareo",
            "parere"
        ],
        "qEn": "obey",
        "aEn": [
            "obey"
        ],
        "type": [
            "verb"
        ],
        "stage": 23
    },
    {
        "qLa": "par\u00c5\u008d, par\u00c4\u0081re, par\u00c4\u0081v\u00c4\u00ab, par\u00c4\u0081tus",
        "aLa": [
            "paro",
            "parare"
        ],
        "qEn": "prepare",
        "aEn": [
            "prepare"
        ],
        "type": [
            "verb"
        ],
        "stage": 7
    },
    {
        "qLa": "pars, partis, f.",
        "aLa": [
            "pars"
        ],
        "qEn": "part",
        "aEn": [
            "part"
        ],
        "type": [
            "noun"
        ],
        "stage": 18
    },
    {
        "qLa": "parvus, parva, parvum",
        "aLa": [
            "parvus"
        ],
        "qEn": "small",
        "aEn": [
            "small"
        ],
        "type": [
            "adjective"
        ],
        "stage": 6
    },
    {
        "qLa": "pater, patris, m.",
        "aLa": [
            "pater"
        ],
        "qEn": "father",
        "aEn": [
            "father"
        ],
        "type": [
            "noun"
        ],
        "stage": 1
    },
    {
        "qLa": "pauc\u00c4\u00ab, paucae, pauca",
        "aLa": [
            "pauci"
        ],
        "qEn": "few, a few",
        "aEn": [
            "few",
            "a few"
        ],
        "type": [
            "adjective"
        ],
        "stage": 17
    },
    {
        "qLa": "p\u00c4\u0081x, p\u00c4\u0081cis, f.",
        "aLa": [
            "pax"
        ],
        "qEn": "peace",
        "aEn": [
            "peace"
        ],
        "type": [
            "noun"
        ],
        "stage": 10
    },
    {
        "qLa": "pec\u00c5\u00abnia, pec\u00c5\u00abniae, f.",
        "aLa": [
            "pecunia"
        ],
        "qEn": "money",
        "aEn": [
            "money"
        ],
        "type": [
            "noun"
        ],
        "stage": 4
    },
    {
        "qLa": "peior, peius (irregular comparative)",
        "aLa": [
            "peior"
        ],
        "qEn": "worse",
        "aEn": [
            "worse"
        ],
        "type": [
            "adjective"
        ],
        "stage": 0
    },
    {
        "qLa": "per + acc (also used as prefix with verbs)",
        "aLa": [
            "per"
        ],
        "qEn": "through, along",
        "aEn": [
            "through",
            "along"
        ],
        "type": [
            "preposition"
        ],
        "stage": 6
    },
    {
        "qLa": "pere\u00c5\u008d, per\u00c4\u00abre, peri\u00c4\u00ab",
        "aLa": [
            "pereo",
            "perire"
        ],
        "qEn": "die, perish",
        "aEn": [
            "die",
            "perish"
        ],
        "type": [
            "verb"
        ],
        "stage": 16
    },
    {
        "qLa": "per\u00c4\u00abculum, per\u00c4\u00abcul\u00c4\u00ab, n.",
        "aLa": [
            "periculum"
        ],
        "qEn": "danger",
        "aEn": [
            "danger"
        ],
        "type": [
            "noun"
        ],
        "stage": 19
    },
    {
        "qLa": "persu\u00c4\u0081de\u00c5\u008d, persu\u00c4\u0081d\u00c4\u201cre, persu\u00c4\u0081s\u00c4\u00ab + dat",
        "aLa": [
            "persuadeo",
            "persuadere"
        ],
        "qEn": "persuade",
        "aEn": [
            "persuade"
        ],
        "type": [
            "verb"
        ],
        "stage": 20
    },
    {
        "qLa": "perterritus, perterrita, perterritum",
        "aLa": [
            "perterritus"
        ],
        "qEn": "terrified",
        "aEn": [
            "terrified"
        ],
        "type": [
            "adjective"
        ],
        "stage": 4
    },
    {
        "qLa": "p\u00c4\u201cs, pedis, m.",
        "aLa": [
            "pes"
        ],
        "qEn": "foot, paw",
        "aEn": [
            "foot",
            "paw"
        ],
        "type": [
            "noun"
        ],
        "stage": 8
    },
    {
        "qLa": "pessimus, pessima, pessimum",
        "aLa": [
            "pessimus"
        ],
        "qEn": "the worst, very bad",
        "aEn": [
            "the worst",
            "worst",
            "very bad"
        ],
        "type": [
            "adjective"
        ],
        "stage": 20
    },
    {
        "qLa": "pet\u00c5\u008d, petere, pet\u00c4\u00abv\u00c4\u00ab, pet\u00c4\u00abtus",
        "aLa": [
            "peto",
            "petere"
        ],
        "qEn": "make for, attack, seek, beg, ask for",
        "aEn": [
            "make for",
            "attack",
            "seek",
            "beg",
            "ask for"
        ],
        "type": [
            "verb"
        ],
        "stage": 5
    },
    {
        "qLa": "place\u00c5\u008d, plac\u00c4\u201cre, placu\u00c4\u00ab + dat",
        "aLa": [
            "placeo",
            "placere"
        ],
        "qEn": "please",
        "aEn": [
            "please"
        ],
        "type": [
            "verb"
        ],
        "stage": 11
    },
    {
        "qLa": "pl\u00c4\u201cnus, pl\u00c4\u201cna, pl\u00c4\u201cnum",
        "aLa": [
            "plenus"
        ],
        "qEn": "full",
        "aEn": [
            "full"
        ],
        "type": [
            "adjective"
        ],
        "stage": 21
    },
    {
        "qLa": "plus, pluris (irregular comparative)",
        "aLa": [
            "plus"
        ],
        "qEn": "more",
        "aEn": [
            "more"
        ],
        "type": [
            "adjective"
        ],
        "stage": 21
    },
    {
        "qLa": "poena, poenae, f.",
        "aLa": [
            "poena"
        ],
        "qEn": "punishment",
        "aEn": [
            "punishment"
        ],
        "type": [
            "noun"
        ],
        "stage": 25
    },
    {
        "qLa": "poen\u00c4\u0081s d\u00c5\u008d, dare, ded\u00c4\u00ab, datus",
        "aLa": [
            "poenas do",
            "poenas dare"
        ],
        "qEn": "pay the penalty, be punished",
        "aEn": [
            "pay the penalty",
            "be punished"
        ],
        "type": [
            "verb"
        ],
        "stage": 25
    },
    {
        "qLa": "p\u00c5\u008dn\u00c5\u008d, p\u00c5\u008dnere, posu\u00c4\u00ab, positus",
        "aLa": [
            "pono",
            "ponere"
        ],
        "qEn": "put, place, put up",
        "aEn": [
            "put",
            "place",
            "put up"
        ],
        "type": [
            "verb"
        ],
        "stage": 16
    },
    {
        "qLa": "porta, portae, f.",
        "aLa": [
            "porta"
        ],
        "qEn": "gate",
        "aEn": [
            "gate"
        ],
        "type": [
            "noun"
        ],
        "stage": 8
    },
    {
        "qLa": "port\u00c5\u008d, port\u00c4\u0081re, port\u00c4\u0081v\u00c4\u00ab, port\u00c4\u0081tus",
        "aLa": [
            "fero",
            "ferre",
            "porto",
            "portare"
        ],
        "qEn": "carry",
        "aEn": [
            "carry"
        ],
        "type": [
            "verb"
        ],
        "stage": 3
    },
    {
        "qLa": "possum, posse",
        "aLa": [
            "possum",
            "posse"
        ],
        "qEn": "can, be able",
        "aEn": [
            "can",
            "be able"
        ],
        "type": [
            "verb"
        ],
        "stage": 13
    },
    {
        "qLa": "post + acc",
        "aLa": [
            "post"
        ],
        "qEn": "after, behind",
        "aEn": [
            "after",
            "behind"
        ],
        "type": [
            "preposition"
        ],
        "stage": 9
    },
    {
        "qLa": "poste\u00c4\u0081 (indecl.)",
        "aLa": [
            "postea"
        ],
        "qEn": "afterwards",
        "aEn": [
            "afterwards"
        ],
        "type": [
            "adverb"
        ],
        "stage": 18
    },
    {
        "qLa": "postquam (indecl.)",
        "aLa": [
            "postquam"
        ],
        "qEn": "after, when",
        "aEn": [
            "after",
            "when"
        ],
        "type": [
            "misc"
        ],
        "stage": 6
    },
    {
        "qLa": "postr\u00c4\u00abdi\u00c4\u201c (indecl.)",
        "aLa": [
            "postridie"
        ],
        "qEn": "on the next day",
        "aEn": [
            "on the next day"
        ],
        "type": [
            "adverb"
        ],
        "stage": 16
    },
    {
        "qLa": "postul\u00c5\u008d, postul\u00c4\u0081re, postul\u00c4\u0081v\u00c4\u00ab, postul\u00c4\u0081tus",
        "aLa": [
            "postulo",
            "postulare"
        ],
        "qEn": "demand",
        "aEn": [
            "demand"
        ],
        "type": [
            "verb"
        ],
        "stage": 8
    },
    {
        "qLa": "praebe\u00c5\u008d, praeb\u00c4\u201cre, praebu\u00c4\u00ab, praebitus",
        "aLa": [
            "praebeo",
            "praebere"
        ],
        "qEn": "provide",
        "aEn": [
            "provide"
        ],
        "type": [
            "verb"
        ],
        "stage": 26
    },
    {
        "qLa": "praemium, praemi\u00c4\u00ab, n.",
        "aLa": [
            "praemium"
        ],
        "qEn": "prize, reward, profit",
        "aEn": [
            "prize",
            "reward",
            "profit"
        ],
        "type": [
            "noun"
        ],
        "stage": 27
    },
    {
        "qLa": "pr\u00c4\u00abmus, pr\u00c4\u00abma, pr\u00c4\u00abmum",
        "aLa": [
            "primus"
        ],
        "qEn": "first",
        "aEn": [
            "first"
        ],
        "type": [
            "adjective"
        ],
        "stage": 11
    },
    {
        "qLa": "pr\u00c4\u00abnceps, pr\u00c4\u00abncipis, m.",
        "aLa": [
            "princeps"
        ],
        "qEn": "chief, chieftain, emperor",
        "aEn": [
            "chief",
            "chieftain",
            "emperor"
        ],
        "type": [
            "noun"
        ],
        "stage": 15
    },
    {
        "qLa": "pr\u00c5\u008d + abl (also used as prefix with verbs)",
        "aLa": [
            "pro"
        ],
        "qEn": "in front of, for, in return for (as prefix = forwards)",
        "aEn": [
            "in front of",
            "for",
            "in return for"
        ],
        "type": [
            "preposition"
        ],
        "stage": 18
    },
    {
        "qLa": "pr\u00c5\u008dc\u00c4\u201cd\u00c5\u008d, pr\u00c5\u008dc\u00c4\u201cdere, pr\u00c5\u008dcess\u00c4\u00ab",
        "aLa": [
            "procedo",
            "procedere"
        ],
        "qEn": "advance, proceed",
        "aEn": [
            "advance",
            "proceed"
        ],
        "type": [
            "verb"
        ],
        "stage": 9
    },
    {
        "qLa": "pr\u00c5\u008dgredior, pr\u00c5\u008dgred\u00c4\u00ab, pr\u00c5\u008dgressus sum",
        "aLa": [
            "progredior",
            "progredi"
        ],
        "qEn": "advance",
        "aEn": [
            "advance"
        ],
        "type": [
            "verb"
        ],
        "stage": 34
    },
    {
        "qLa": "pr\u00c5\u008dmitt\u00c5\u008d, pr\u00c5\u008dmittere, pr\u00c5\u008dm\u00c4\u00abs\u00c4\u00ab, pr\u00c5\u008dmissus",
        "aLa": [
            "promitto",
            "promittere"
        ],
        "qEn": "promise",
        "aEn": [
            "promise"
        ],
        "type": [
            "verb"
        ],
        "stage": 11
    },
    {
        "qLa": "prope + acc",
        "aLa": [
            "prope"
        ],
        "qEn": "near",
        "aEn": [
            "near"
        ],
        "type": [
            "preposition"
        ],
        "stage": 7
    },
    {
        "qLa": "propter + acc",
        "aLa": [
            "propter"
        ],
        "qEn": "because of",
        "aEn": [
            "because of"
        ],
        "type": [
            "preposition"
        ],
        "stage": 0
    },
    {
        "qLa": "proximus, proxima, proximum",
        "aLa": [
            "proximus"
        ],
        "qEn": "nearest, next to",
        "aEn": [
            "nearest",
            "next to"
        ],
        "type": [
            "adjective"
        ],
        "stage": 27
    },
    {
        "qLa": "puella, puellae, f.",
        "aLa": [
            "puella"
        ],
        "qEn": "girl",
        "aEn": [
            "girl"
        ],
        "type": [
            "noun"
        ],
        "stage": 5
    },
    {
        "qLa": "puer, puer\u00c4\u00ab, m.",
        "aLa": [
            "puer"
        ],
        "qEn": "boy",
        "aEn": [
            "boy"
        ],
        "type": [
            "noun"
        ],
        "stage": 8
    },
    {
        "qLa": "pugn\u00c5\u008d, pugn\u00c4\u0081re, pugn\u00c4\u0081v\u00c4\u00ab",
        "aLa": [
            "pugno",
            "pugnare"
        ],
        "qEn": "fight",
        "aEn": [
            "fight"
        ],
        "type": [
            "verb"
        ],
        "stage": 8
    },
    {
        "qLa": "pulcher, pulchra, pulchrum",
        "aLa": [
            "pulcher"
        ],
        "qEn": "beautiful, handsome",
        "aEn": [
            "beautiful",
            "handsome"
        ],
        "type": [
            "adjective"
        ],
        "stage": 9
    },
    {
        "qLa": "puto, put\u00c4\u0081re, put\u00c4\u0081v\u00c4\u00ab, put\u00c4\u0081tus",
        "aLa": [
            "cogito",
            "cogitare",
            "puto",
            "putare"
        ],
        "qEn": "think",
        "aEn": [
            "think"
        ],
        "type": [
            "verb"
        ],
        "stage": 0
    },
    {
        "qLa": "quaer\u00c5\u008d, quaerere, quaes\u00c4\u00abv\u00c4\u00ab, quaes\u00c4\u00abtus",
        "aLa": [
            "quaero",
            "quaerere"
        ],
        "qEn": "search for, look for, ask",
        "aEn": [
            "search for",
            "look for",
            "ask"
        ],
        "type": [
            "verb"
        ],
        "stage": 4
    },
    {
        "qLa": "qu\u00c4\u0081lis, qu\u00c4\u0081le?",
        "aLa": [
            "qualis"
        ],
        "qEn": "what sort of?",
        "aEn": [
            "what sort of"
        ],
        "type": [
            "adjective"
        ],
        "stage": 27
    },
    {
        "qLa": "quam (indecl.)",
        "aLa": [
            "quam"
        ],
        "qEn": "than, how ... ? how ... !",
        "aEn": [
            "than",
            "how"
        ],
        "type": [
            "adverb"
        ],
        "stage": 10
    },
    {
        "qLa": "quamquam (indecl.)",
        "aLa": [
            "quamquam"
        ],
        "qEn": "although",
        "aEn": [
            "although"
        ],
        "type": [
            "misc"
        ],
        "stage": 14
    },
    {
        "qLa": "quantus, quanta, quantum?",
        "aLa": [
            "quantus"
        ],
        "qEn": "how big? how much?",
        "aEn": [
            "how big",
            "how much"
        ],
        "type": [
            "adjective"
        ],
        "stage": 22
    },
    {
        "qLa": "quattuor (indecl.)",
        "aLa": [
            "quattuor"
        ],
        "qEn": "four",
        "aEn": [
            "four"
        ],
        "type": [
            "adjective"
        ],
        "stage": 20
    },
    {
        "qLa": "-que (indecl.) (added to end of a word)",
        "aLa": [
            "ac",
            "atque",
            "et",
            "-que",
            "que"
        ],
        "qEn": "and",
        "aEn": [
            "and"
        ],
        "type": [
            "misc"
        ],
        "stage": 14
    },
    {
        "qLa": "qu\u00c4\u00ab, quae, quod",
        "aLa": [
            "qui"
        ],
        "qEn": "who, which",
        "aEn": [
            "who",
            "which"
        ],
        "type": [
            "pronoun"
        ],
        "stage": 15
    },
    {
        "qLa": "qu\u00c4\u00abnque (indecl.)",
        "aLa": [
            "quinque"
        ],
        "qEn": "five",
        "aEn": [
            "five"
        ],
        "type": [
            "adjective"
        ],
        "stage": 20
    },
    {
        "qLa": "quis, quid?",
        "aLa": [
            "quis"
        ],
        "qEn": "who? what?",
        "aEn": [
            "who",
            "what"
        ],
        "type": [
            "pronoun"
        ],
        "stage": 4
    },
    {
        "qLa": "qu\u00c5\u008d? (indecl.)",
        "aLa": [
            "quo"
        ],
        "qEn": "where to?",
        "aEn": [
            "where to"
        ],
        "type": [
            "adverb"
        ],
        "stage": 18
    },
    {
        "qLa": "quod (indecl.)",
        "aLa": [
            "quod"
        ],
        "qEn": "because",
        "aEn": [
            "because"
        ],
        "type": [
            "misc"
        ],
        "stage": 6
    },
    {
        "qLa": "qu\u00c5\u008d mod\u00c5\u008d? (indecl.)",
        "aLa": [
            "quo modo"
        ],
        "qEn": "how? in what way?",
        "aEn": [
            "how",
            "in what way"
        ],
        "type": [
            "adverb"
        ],
        "stage": 22
    },
    {
        "qLa": "quoque (indecl.)",
        "aLa": [
            "etiam",
            "quoque"
        ],
        "qEn": "also, too",
        "aEn": [
            "also",
            "too"
        ],
        "type": [
            "misc"
        ],
        "stage": 2
    },
    {
        "qLa": "quot? (indecl.)",
        "aLa": [
            "quot"
        ],
        "qEn": "how many?",
        "aEn": [
            "how many"
        ],
        "type": [
            "adjective"
        ],
        "stage": 26
    },
    {
        "qLa": "rapi\u00c5\u008d, rapere, rapu\u00c4\u00ab, raptus",
        "aLa": [
            "rapio",
            "rapere"
        ],
        "qEn": "seize, grab",
        "aEn": [
            "seize",
            "grab"
        ],
        "type": [
            "verb"
        ],
        "stage": 0
    },
    {
        "qLa": "re- (prefix used with verbs)",
        "aLa": [
            "re",
            "re-"
        ],
        "qEn": "back",
        "aEn": [
            "back"
        ],
        "type": [
            "misc"
        ],
        "stage": 0
    },
    {
        "qLa": "redd\u00c5\u008d, reddere, reddid\u00c4\u00ab, redditus",
        "aLa": [
            "reddo",
            "reddere"
        ],
        "qEn": "give back, restore",
        "aEn": [
            "give back",
            "restore"
        ],
        "type": [
            "verb"
        ],
        "stage": 4
    },
    {
        "qLa": "rede\u00c5\u008d, red\u00c4\u00abre, redi\u00c4\u00ab",
        "aLa": [
            "redeo",
            "redire"
        ],
        "qEn": "go back, come back, return",
        "aEn": [
            "go back",
            "come back",
            "return"
        ],
        "type": [
            "verb"
        ],
        "stage": 15
    },
    {
        "qLa": "refer\u00c5\u008d, referre, rettul\u00c4\u00ab, rel\u00c4\u0081tus",
        "aLa": [
            "refero",
            "referre"
        ],
        "qEn": "bring/carry back; report, tell",
        "aEn": [
            "bring back",
            "carry back",
            "report",
            "tell"
        ],
        "type": [
            "verb"
        ],
        "stage": 26
    },
    {
        "qLa": "r\u00c4\u201cg\u00c4\u00abna, r\u00c4\u201cg\u00c4\u00abnae, f.",
        "aLa": [
            "regina"
        ],
        "qEn": "queen",
        "aEn": [
            "queen"
        ],
        "type": [
            "noun"
        ],
        "stage": 33
    },
    {
        "qLa": "regredior, regred\u00c4\u00ab, regressus sum",
        "aLa": [
            "regredior",
            "regredi"
        ],
        "qEn": "go back, return",
        "aEn": [
            "go back",
            "return"
        ],
        "type": [
            "verb"
        ],
        "stage": 34
    },
    {
        "qLa": "relinqu\u00c5\u008d, relinquere, rel\u00c4\u00abqu\u00c4\u00ab, relictus",
        "aLa": [
            "discedo",
            "discedere",
            "relinquo",
            "relinquere"
        ],
        "qEn": "leave, leave behind",
        "aEn": [
            "leave",
            "leave behind"
        ],
        "type": [
            "verb"
        ],
        "stage": 20
    },
    {
        "qLa": "r\u00c4\u201cs, re\u00c4\u00ab, f.",
        "aLa": [
            "res"
        ],
        "qEn": "thing, business, matter",
        "aEn": [
            "thing",
            "business",
            "matter"
        ],
        "type": [
            "noun"
        ],
        "stage": 6
    },
    {
        "qLa": "resist\u00c5\u008d, resistere, restit\u00c4\u00ab + dat",
        "aLa": [
            "resisto",
            "resistere"
        ],
        "qEn": "resist",
        "aEn": [
            "resist"
        ],
        "type": [
            "verb"
        ],
        "stage": 17
    },
    {
        "qLa": "responde\u00c5\u008d, respond\u00c4\u201cre, respond\u00c4\u00ab, resp\u00c5\u008dnsus",
        "aLa": [
            "respondeo",
            "respondere"
        ],
        "qEn": "reply",
        "aEn": [
            "reply"
        ],
        "type": [
            "verb"
        ],
        "stage": 3
    },
    {
        "qLa": "r\u00c4\u201cx, r\u00c4\u201cgis, m.",
        "aLa": [
            "rex"
        ],
        "qEn": "king",
        "aEn": [
            "king"
        ],
        "type": [
            "noun"
        ],
        "stage": 14
    },
    {
        "qLa": "r\u00c4\u00abde\u00c5\u008d, r\u00c4\u00abd\u00c4\u201cre, r\u00c4\u00abs\u00c4\u00ab",
        "aLa": [
            "rideo",
            "ridere"
        ],
        "qEn": "laugh, smile",
        "aEn": [
            "laugh",
            "smile"
        ],
        "type": [
            "verb"
        ],
        "stage": 3
    },
    {
        "qLa": "rog\u00c5\u008d, rog\u00c4\u0081re, rog\u00c4\u0081v\u00c4\u00ab, rog\u00c4\u0081tus",
        "aLa": [
            "rogo",
            "rogare"
        ],
        "qEn": "ask, ask for",
        "aEn": [
            "ask",
            "ask for"
        ],
        "type": [
            "verb"
        ],
        "stage": 7
    },
    {
        "qLa": "R\u00c5\u008dma, R\u00c5\u008dmae, f.",
        "aLa": [
            "Roma"
        ],
        "qEn": "Rome",
        "aEn": [
            "Rome"
        ],
        "type": [
            "noun"
        ],
        "stage": 0
    },
    {
        "qLa": "R\u00c5\u008dmae",
        "aLa": [
            "Romae"
        ],
        "qEn": "at/in Rome",
        "aEn": [
            "at Rome",
            "in Rome"
        ],
        "type": [
            "adverb"
        ],
        "stage": 0
    },
    {
        "qLa": "R\u00c5\u008dm\u00c4\u0081nus, R\u00c5\u008dm\u00c4\u0081na, Romanum",
        "aLa": [
            "Romanus"
        ],
        "qEn": "Roman",
        "aEn": [
            "Roman"
        ],
        "type": [
            "adjective"
        ],
        "stage": 0
    },
    {
        "qLa": "sacer, sacra, sacrum",
        "aLa": [
            "sacer"
        ],
        "qEn": "sacred",
        "aEn": [
            "sacred"
        ],
        "type": [
            "adjective"
        ],
        "stage": 21
    },
    {
        "qLa": "saepe (indecl.)",
        "aLa": [
            "saepe"
        ],
        "qEn": "often",
        "aEn": [
            "often"
        ],
        "type": [
            "adverb"
        ],
        "stage": 8
    },
    {
        "qLa": "saevus, saeva, saevum",
        "aLa": [
            "crudelis",
            "saevus"
        ],
        "qEn": "savage, cruel",
        "aEn": [
            "savage",
            "cruel"
        ],
        "type": [
            "adjective"
        ],
        "stage": 26
    },
    {
        "qLa": "sal\u00c5\u00abt\u00c5\u008d, sal\u00c5\u00abt\u00c4\u0081re, sal\u00c5\u00abt\u00c4\u0081v\u00c4\u00ab, sal\u00c5\u00abt\u00c4\u0081tus",
        "aLa": [
            "saluto",
            "salutare"
        ],
        "qEn": "greet",
        "aEn": [
            "greet"
        ],
        "type": [
            "verb"
        ],
        "stage": 2
    },
    {
        "qLa": "sanguis, sanguinis, m.",
        "aLa": [
            "sanguis"
        ],
        "qEn": "blood",
        "aEn": [
            "blood"
        ],
        "type": [
            "noun"
        ],
        "stage": 8
    },
    {
        "qLa": "scio, sc\u00c4\u00abre, sc\u00c4\u00abv\u00c4\u00ab, sc\u00c4\u00abtus",
        "aLa": [
            "scio",
            "scire"
        ],
        "qEn": "know",
        "aEn": [
            "know"
        ],
        "type": [
            "verb"
        ],
        "stage": 23
    },
    {
        "qLa": "scr\u00c4\u00abb\u00c5\u008d, scr\u00c4\u00abbere, scr\u00c4\u00abps\u00c4\u00ab, scr\u00c4\u00abptus",
        "aLa": [
            "scribo",
            "scribere"
        ],
        "qEn": "write",
        "aEn": [
            "write"
        ],
        "type": [
            "verb"
        ],
        "stage": 6
    },
    {
        "qLa": "s\u00c4\u201c, su\u00c4\u00ab",
        "aLa": [
            "ipse",
            "se"
        ],
        "qEn": "himself, herself, itself, themselves",
        "aEn": [
            "himself",
            "herself",
            "itself",
            "themselves"
        ],
        "type": [
            "pronoun"
        ],
        "stage": 13
    },
    {
        "qLa": "sed (indecl.)",
        "aLa": [
            "sed"
        ],
        "qEn": "but",
        "aEn": [
            "but"
        ],
        "type": [
            "misc"
        ],
        "stage": 4
    },
    {
        "qLa": "sede\u00c5\u008d, sed\u00c4\u201cre, s\u00c4\u201cd\u00c4\u00ab",
        "aLa": [
            "sedeo",
            "sedere"
        ],
        "qEn": "sit",
        "aEn": [
            "sit"
        ],
        "type": [
            "verb"
        ],
        "stage": 1
    },
    {
        "qLa": "semper (indecl.)",
        "aLa": [
            "semper"
        ],
        "qEn": "always",
        "aEn": [
            "always"
        ],
        "type": [
            "adverb"
        ],
        "stage": 10
    },
    {
        "qLa": "sen\u00c4\u0081tor, sen\u00c4\u0081t\u00c5\u008dris, m.",
        "aLa": [
            "senator"
        ],
        "qEn": "senator",
        "aEn": [
            "senator"
        ],
        "type": [
            "noun"
        ],
        "stage": 11
    },
    {
        "qLa": "senex, senis (m.)",
        "aLa": [
            "senex"
        ],
        "qEn": "old; old man",
        "aEn": [
            "old",
            "old man"
        ],
        "type": [
            "adjective",
            "noun"
        ],
        "stage": 5
    },
    {
        "qLa": "senti\u00c5\u008d, sent\u00c4\u00abre, s\u00c4\u201cns\u00c4\u00ab, s\u00c4\u201cnsus",
        "aLa": [
            "sentio",
            "sentire"
        ],
        "qEn": "feel, notice",
        "aEn": [
            "feel",
            "notice"
        ],
        "type": [
            "verb"
        ],
        "stage": 12
    },
    {
        "qLa": "septem (indecl.)",
        "aLa": [
            "septem"
        ],
        "qEn": "seven",
        "aEn": [
            "seven"
        ],
        "type": [
            "adjective"
        ],
        "stage": 20
    },
    {
        "qLa": "sequor, sequ\u00c4\u00ab, sec\u00c5\u00abtus sum",
        "aLa": [
            "sequor",
            "sequi"
        ],
        "qEn": "follow",
        "aEn": [
            "follow"
        ],
        "type": [
            "verb"
        ],
        "stage": 34
    },
    {
        "qLa": "serv\u00c5\u008d, serv\u00c4\u0081re, serv\u00c4\u0081v\u00c4\u00ab, serv\u00c4\u0081tus",
        "aLa": [
            "servo",
            "servare"
        ],
        "qEn": "save, look after",
        "aEn": [
            "save",
            "look after"
        ],
        "type": [
            "verb"
        ],
        "stage": 10
    },
    {
        "qLa": "servus, serv\u00c4\u00ab, m.",
        "aLa": [
            "servus"
        ],
        "qEn": "slave",
        "aEn": [
            "slave"
        ],
        "type": [
            "noun"
        ],
        "stage": 1
    },
    {
        "qLa": "sex (indecl.)",
        "aLa": [
            "sex"
        ],
        "qEn": "six",
        "aEn": [
            "six"
        ],
        "type": [
            "adjective"
        ],
        "stage": 20
    },
    {
        "qLa": "s\u00c4\u00ab (indecl.)",
        "aLa": [
            "si"
        ],
        "qEn": "if",
        "aEn": [
            "if"
        ],
        "type": [
            "misc"
        ],
        "stage": 26
    },
    {
        "qLa": "s\u00c4\u00abc (indecl.)",
        "aLa": [
            "ita",
            "sic"
        ],
        "qEn": "thus, in this way",
        "aEn": [
            "thus",
            "in this way"
        ],
        "type": [
            "adverb"
        ],
        "stage": 28
    },
    {
        "qLa": "s\u00c4\u00abcut (indecl.)",
        "aLa": [
            "sicut"
        ],
        "qEn": "just as, like",
        "aEn": [
            "just as",
            "like"
        ],
        "type": [
            "adverb"
        ],
        "stage": 20
    },
    {
        "qLa": "signum, sign\u00c4\u00ab, n.",
        "aLa": [
            "signum"
        ],
        "qEn": "sign, signal, seal",
        "aEn": [
            "sign",
            "signal",
            "seal"
        ],
        "type": [
            "noun"
        ],
        "stage": 4
    },
    {
        "qLa": "silva, silvae, f.",
        "aLa": [
            "silva"
        ],
        "qEn": "wood",
        "aEn": [
            "wood"
        ],
        "type": [
            "noun"
        ],
        "stage": 8
    },
    {
        "qLa": "simulac, simulatque",
        "aLa": [
            "simulac",
            "simulatque"
        ],
        "qEn": "as soon as",
        "aEn": [
            "as soon as"
        ],
        "type": [
            "misc"
        ],
        "stage": 16
    },
    {
        "qLa": "sine + abl",
        "aLa": [
            "sine"
        ],
        "qEn": "without",
        "aEn": [
            "without"
        ],
        "type": [
            "preposition"
        ],
        "stage": 0
    },
    {
        "qLa": "s\u00c5\u008dlus, s\u00c5\u008dla, s\u00c5\u008dlum",
        "aLa": [
            "solus"
        ],
        "qEn": "alone, lonely, only, on one\u00e2\u20ac\u2122s own",
        "aEn": [
            "alone",
            "lonely",
            "only",
            "on one's own",
            "on ones own"
        ],
        "type": [
            "adjective"
        ],
        "stage": 10
    },
    {
        "qLa": "soror, sor\u00c5\u008dris, f.",
        "aLa": [
            "soror"
        ],
        "qEn": "sister",
        "aEn": [
            "sister"
        ],
        "type": [
            "noun"
        ],
        "stage": 30
    },
    {
        "qLa": "spect\u00c5\u008d, spect\u00c4\u0081re, spect\u00c4\u0081v\u00c4\u00ab, spect\u00c4\u0081tus",
        "aLa": [
            "specto",
            "spectare"
        ],
        "qEn": "look at, watch",
        "aEn": [
            "look at",
            "watch"
        ],
        "type": [
            "verb"
        ],
        "stage": 5
    },
    {
        "qLa": "sp\u00c4\u201cs, spe\u00c4\u00ab, f.",
        "aLa": [
            "spes"
        ],
        "qEn": "hope",
        "aEn": [
            "hope"
        ],
        "type": [
            "noun"
        ],
        "stage": 28
    },
    {
        "qLa": "statim (indecl.)",
        "aLa": [
            "statim"
        ],
        "qEn": "at once, immediately",
        "aEn": [
            "at once",
            "immediately"
        ],
        "type": [
            "adverb"
        ],
        "stage": 8
    },
    {
        "qLa": "st\u00c5\u008d, st\u00c4\u0081re, stet\u00c4\u00ab",
        "aLa": [
            "sto",
            "stare"
        ],
        "qEn": "stand",
        "aEn": [
            "stand"
        ],
        "type": [
            "verb"
        ],
        "stage": 5
    },
    {
        "qLa": "stultus, stulta, stultum",
        "aLa": [
            "stultus"
        ],
        "qEn": "stupid, foolish",
        "aEn": [
            "stupid",
            "foolish"
        ],
        "type": [
            "adjective"
        ],
        "stage": 11
    },
    {
        "qLa": "sub + acc/abl (also used as prefix with verbs)",
        "aLa": [
            "sub"
        ],
        "qEn": "under, beneath (as prefix = under, up to)",
        "aEn": [
            "under",
            "beneath"
        ],
        "type": [
            "preposition"
        ],
        "stage": 27
    },
    {
        "qLa": "subit\u00c5\u008d (indecl.)",
        "aLa": [
            "subito"
        ],
        "qEn": "suddenly",
        "aEn": [
            "suddenly"
        ],
        "type": [
            "adverb"
        ],
        "stage": 6
    },
    {
        "qLa": "sum, esse, fu\u00c4\u00ab",
        "aLa": [
            "sum",
            "esse"
        ],
        "qEn": "be",
        "aEn": [
            "be"
        ],
        "type": [
            "verb"
        ],
        "stage": 1
    },
    {
        "qLa": "summus, summa, summum",
        "aLa": [
            "summus"
        ],
        "qEn": "highest, greatest, top (of)",
        "aEn": [
            "highest",
            "greatest",
            "top"
        ],
        "type": [
            "adjective"
        ],
        "stage": 16
    },
    {
        "qLa": "super\u00c5\u008d, super\u00c4\u0081re, super\u00c4\u0081v\u00c4\u00ab, super\u00c4\u0081tus",
        "aLa": [
            "supero",
            "superare"
        ],
        "qEn": "overcome, overpower",
        "aEn": [
            "overcome",
            "overpower"
        ],
        "type": [
            "verb"
        ],
        "stage": 6
    },
    {
        "qLa": "surg\u00c5\u008d, surgere, surr\u00c4\u201cx\u00c4\u00ab",
        "aLa": [
            "surgo",
            "surgere"
        ],
        "qEn": "get up, stand up, rise",
        "aEn": [
            "get up",
            "stand up",
            "rise"
        ],
        "type": [
            "verb"
        ],
        "stage": 3
    },
    {
        "qLa": "suus, sua, suum",
        "aLa": [
            "suus"
        ],
        "qEn": "his, her, its, their (own)",
        "aEn": [
            "his",
            "her",
            "its",
            "their"
        ],
        "type": [
            "pronoun"
        ],
        "stage": 10
    },
    {
        "qLa": "taberna, tabernae, f.",
        "aLa": [
            "taberna"
        ],
        "qEn": "shop, inn",
        "aEn": [
            "shop",
            "inn"
        ],
        "type": [
            "noun"
        ],
        "stage": 3
    },
    {
        "qLa": "tace\u00c5\u008d, tac\u00c4\u201cre, tacu\u00c4\u00ab, tacitus",
        "aLa": [
            "taceo",
            "tacere"
        ],
        "qEn": "be silent, be quiet",
        "aEn": [
            "be silent",
            "be quiet"
        ],
        "type": [
            "verb"
        ],
        "stage": 10
    },
    {
        "qLa": "t\u00c4\u0081lis, t\u00c4\u0081le",
        "aLa": [
            "talis"
        ],
        "qEn": "such",
        "aEn": [
            "such"
        ],
        "type": [
            "adjective"
        ],
        "stage": 23
    },
    {
        "qLa": "tam (indecl.)",
        "aLa": [
            "ita",
            "tam"
        ],
        "qEn": "so",
        "aEn": [
            "so"
        ],
        "type": [
            "adverb"
        ],
        "stage": 20
    },
    {
        "qLa": "tamen (indecl.)",
        "aLa": [
            "tamen"
        ],
        "qEn": "however",
        "aEn": [
            "however"
        ],
        "type": [
            "misc"
        ],
        "stage": 7
    },
    {
        "qLa": "tandem (indecl.)",
        "aLa": [
            "tandem"
        ],
        "qEn": "at last, finally",
        "aEn": [
            "at last",
            "finally"
        ],
        "type": [
            "adverb"
        ],
        "stage": 12
    },
    {
        "qLa": "tantus, tanta, tantum",
        "aLa": [
            "tantus"
        ],
        "qEn": "so great, such a great, so much",
        "aEn": [
            "so great",
            "such a great",
            "so much"
        ],
        "type": [
            "adjective"
        ],
        "stage": 27
    },
    {
        "qLa": "templum, templ\u00c4\u00ab, n.",
        "aLa": [
            "templum"
        ],
        "qEn": "temple",
        "aEn": [
            "temple"
        ],
        "type": [
            "noun"
        ],
        "stage": 12
    },
    {
        "qLa": "tempus, temporis, n.",
        "aLa": [
            "tempus"
        ],
        "qEn": "time",
        "aEn": [
            "time"
        ],
        "type": [
            "noun"
        ],
        "stage": 0
    },
    {
        "qLa": "tene\u00c5\u008d, ten\u00c4\u201cre, tenu\u00c4\u00ab, tentus",
        "aLa": [
            "teneo",
            "tenere"
        ],
        "qEn": "hold, keep, possess",
        "aEn": [
            "hold",
            "keep",
            "possess"
        ],
        "type": [
            "verb"
        ],
        "stage": 15
    },
    {
        "qLa": "terra, terrae, f.",
        "aLa": [
            "terra"
        ],
        "qEn": "ground, land",
        "aEn": [
            "ground",
            "land"
        ],
        "type": [
            "noun"
        ],
        "stage": 12
    },
    {
        "qLa": "terre\u00c5\u008d, terr\u00c4\u201cre, terru\u00c4\u00ab, territus",
        "aLa": [
            "terreo",
            "terrere"
        ],
        "qEn": "frighten",
        "aEn": [
            "frighten"
        ],
        "type": [
            "verb"
        ],
        "stage": 7
    },
    {
        "qLa": "time\u00c5\u008d, tim\u00c4\u201cre, timu\u00c4\u00ab",
        "aLa": [
            "timeo",
            "timere"
        ],
        "qEn": "fear, be afraid",
        "aEn": [
            "fear",
            "be afraid"
        ],
        "type": [
            "verb"
        ],
        "stage": 12
    },
    {
        "qLa": "toll\u00c5\u008d, tollere, sustul\u00c4\u00ab, subl\u00c4\u0081tus",
        "aLa": [
            "tollo",
            "tollere"
        ],
        "qEn": "raise, lift up",
        "aEn": [
            "raise",
            "lift up"
        ],
        "type": [
            "verb"
        ],
        "stage": 16
    },
    {
        "qLa": "tot (indecl.)",
        "aLa": [
            "tot"
        ],
        "qEn": "so many",
        "aEn": [
            "so many"
        ],
        "type": [
            "adjective"
        ],
        "stage": 19
    },
    {
        "qLa": "t\u00c5\u008dtus, t\u00c5\u008dta, t\u00c5\u008dtum",
        "aLa": [
            "totus"
        ],
        "qEn": "whole",
        "aEn": [
            "whole"
        ],
        "type": [
            "adjective"
        ],
        "stage": 8
    },
    {
        "qLa": "tr\u00c4\u0081d\u00c5\u008d, tr\u00c4\u0081dere, tr\u00c4\u0081did\u00c4\u00ab, tr\u00c4\u0081ditus",
        "aLa": [
            "trado",
            "tradere"
        ],
        "qEn": "hand over",
        "aEn": [
            "hand over"
        ],
        "type": [
            "verb"
        ],
        "stage": 9
    },
    {
        "qLa": "trah\u00c5\u008d, trahere, tr\u00c4\u0081x\u00c4\u00ab, tractus",
        "aLa": [
            "traho",
            "trahere"
        ],
        "qEn": "drag, draw, pull",
        "aEn": [
            "drag",
            "draw",
            "pull"
        ],
        "type": [
            "verb"
        ],
        "stage": 13
    },
    {
        "qLa": "tr\u00c4\u0081ns + acc (also used as prefix with verbs)",
        "aLa": [
            "trans"
        ],
        "qEn": "across",
        "aEn": [
            "across"
        ],
        "type": [
            "preposition"
        ],
        "stage": 0
    },
    {
        "qLa": "tr\u00c4\u201cs, tria",
        "aLa": [
            "tres"
        ],
        "qEn": "three",
        "aEn": [
            "three"
        ],
        "type": [
            "adjective"
        ],
        "stage": 12
    },
    {
        "qLa": "tr\u00c4\u00abstis, tr\u00c4\u00abste",
        "aLa": [
            "miser",
            "tristis"
        ],
        "qEn": "sad",
        "aEn": [
            "sad"
        ],
        "type": [
            "adjective"
        ],
        "stage": 24
    },
    {
        "qLa": "t\u00c5\u00ab, tu\u00c4\u00ab",
        "aLa": [
            "tu"
        ],
        "qEn": "you (singular)",
        "aEn": [
            "you"
        ],
        "type": [
            "pronoun"
        ],
        "stage": 4
    },
    {
        "qLa": "tum (indecl.)",
        "aLa": [
            "deinde",
            "tum"
        ],
        "qEn": "then",
        "aEn": [
            "then"
        ],
        "type": [
            "adverb"
        ],
        "stage": 6
    },
    {
        "qLa": "turba, turbae, f.",
        "aLa": [
            "turba"
        ],
        "qEn": "crowd",
        "aEn": [
            "crowd"
        ],
        "type": [
            "noun"
        ],
        "stage": 5
    },
    {
        "qLa": "t\u00c5\u00abtus, t\u00c5\u00abta, t\u00c5\u00abtum",
        "aLa": [
            "tutus"
        ],
        "qEn": "safe",
        "aEn": [
            "safe"
        ],
        "type": [
            "adjective"
        ],
        "stage": 22
    },
    {
        "qLa": "tuus, tua, tuum",
        "aLa": [
            "tuus"
        ],
        "qEn": "your (singular), yours",
        "aEn": [
            "your",
            "yours"
        ],
        "type": [
            "pronoun"
        ],
        "stage": 6
    },
    {
        "qLa": "ubi (indecl.)",
        "aLa": [
            "ubi"
        ],
        "qEn": "where, when, where?",
        "aEn": [
            "where",
            "when",
            "where"
        ],
        "type": [
            "adverb"
        ],
        "stage": 5
    },
    {
        "qLa": "umquam (indecl.)",
        "aLa": [
            "umquam"
        ],
        "qEn": "ever",
        "aEn": [
            "ever"
        ],
        "type": [
            "adverb"
        ],
        "stage": 23
    },
    {
        "qLa": "unde (indecl.)",
        "aLa": [
            "unde"
        ],
        "qEn": "from where",
        "aEn": [
            "from where"
        ],
        "type": [
            "adverb"
        ],
        "stage": 21
    },
    {
        "qLa": "\u00c5\u00abnus, \u00c5\u00abna, \u00c5\u00abnum",
        "aLa": [
            "unus"
        ],
        "qEn": "one",
        "aEn": [
            "one"
        ],
        "type": [
            "adjective"
        ],
        "stage": 12
    },
    {
        "qLa": "urbs, urbis, f.",
        "aLa": [
            "urbs"
        ],
        "qEn": "city",
        "aEn": [
            "city"
        ],
        "type": [
            "noun"
        ],
        "stage": 5
    },
    {
        "qLa": "ut (indecl.) + subjunc.",
        "aLa": [
            "ut"
        ],
        "qEn": "that, so that, in order that",
        "aEn": [
            "that",
            "so that",
            "in order that"
        ],
        "type": [
            "misc"
        ],
        "stage": 26
    },
    {
        "qLa": "ut (indecl.) + indic.",
        "aLa": [
            "ut"
        ],
        "qEn": "as",
        "aEn": [
            "as"
        ],
        "type": [
            "misc"
        ],
        "stage": 28
    },
    {
        "qLa": "uxor, ux\u00c5\u008dris, f.",
        "aLa": [
            "uxor"
        ],
        "qEn": "wife",
        "aEn": [
            "wife"
        ],
        "type": [
            "noun"
        ],
        "stage": 10
    },
    {
        "qLa": "vehementer (indecl.)",
        "aLa": [
            "vehementer"
        ],
        "qEn": "violently, loudly, strongly",
        "aEn": [
            "violently",
            "loudly",
            "strongly"
        ],
        "type": [
            "adverb"
        ],
        "stage": 10
    },
    {
        "qLa": "v\u00c4\u201cnd\u00c5\u008d, v\u00c4\u201cndere, v\u00c4\u201cndid\u00c4\u00ab, v\u00c4\u201cnditus",
        "aLa": [
            "vendo",
            "vendere"
        ],
        "qEn": "sell",
        "aEn": [
            "sell"
        ],
        "type": [
            "verb"
        ],
        "stage": 6
    },
    {
        "qLa": "veni\u00c5\u008d, ven\u00c4\u00abre, v\u00c4\u201cn\u00c4\u00ab",
        "aLa": [
            "venio",
            "venire"
        ],
        "qEn": "come",
        "aEn": [
            "come"
        ],
        "type": [
            "verb"
        ],
        "stage": 5
    },
    {
        "qLa": "verbum, verb\u00c4\u00ab, n.",
        "aLa": [
            "verbum"
        ],
        "qEn": "word",
        "aEn": [
            "word"
        ],
        "type": [
            "noun"
        ],
        "stage": 22
    },
    {
        "qLa": "v\u00c4\u201crus, v\u00c4\u201cra, v\u00c4\u201crum",
        "aLa": [
            "verus"
        ],
        "qEn": "true, real",
        "aEn": [
            "true",
            "real"
        ],
        "type": [
            "adjective"
        ],
        "stage": 33
    },
    {
        "qLa": "vester, vestra, vestrum",
        "aLa": [
            "vester"
        ],
        "qEn": "your (plural), yours",
        "aEn": [
            "your",
            "yours"
        ],
        "type": [
            "pronoun"
        ],
        "stage": 29
    },
    {
        "qLa": "vest\u00c4\u00abmenta, vest\u00c4\u00abment\u00c5\u008drum, n.pl.",
        "aLa": [
            "vestimenta"
        ],
        "qEn": "clothes",
        "aEn": [
            "clothes"
        ],
        "type": [
            "noun"
        ],
        "stage": 34
    },
    {
        "qLa": "via, viae, f.",
        "aLa": [
            "via"
        ],
        "qEn": "street, road, way",
        "aEn": [
            "street",
            "road",
            "way"
        ],
        "type": [
            "noun"
        ],
        "stage": 1
    },
    {
        "qLa": "vide\u00c5\u008d, vid\u00c4\u201cre, v\u00c4\u00abd\u00c4\u00ab, v\u00c4\u00absus",
        "aLa": [
            "video",
            "videre"
        ],
        "qEn": "see",
        "aEn": [
            "see"
        ],
        "type": [
            "verb"
        ],
        "stage": 3
    },
    {
        "qLa": "v\u00c4\u00ablla, v\u00c4\u00abllae, f.",
        "aLa": [
            "villa"
        ],
        "qEn": "house, country house",
        "aEn": [
            "house",
            "country house"
        ],
        "type": [
            "noun"
        ],
        "stage": 0
    },
    {
        "qLa": "vinc\u00c5\u008d, vincere, v\u00c4\u00abc\u00c4\u00ab, victus",
        "aLa": [
            "vinco",
            "vincere"
        ],
        "qEn": "conquer, win, be victorious",
        "aEn": [
            "conquer",
            "win",
            "be victorious"
        ],
        "type": [
            "verb"
        ],
        "stage": 15
    },
    {
        "qLa": "v\u00c4\u00abnum, v\u00c4\u00abn\u00c4\u00ab, n.",
        "aLa": [
            "vinum"
        ],
        "qEn": "wine",
        "aEn": [
            "wine"
        ],
        "type": [
            "noun"
        ],
        "stage": 3
    },
    {
        "qLa": "vir, vir\u00c4\u00ab, m.",
        "aLa": [
            "homo",
            "vir"
        ],
        "qEn": "man",
        "aEn": [
            "man"
        ],
        "type": [
            "noun"
        ],
        "stage": 11
    },
    {
        "qLa": "v\u00c4\u00abta, v\u00c4\u00abtae, f.",
        "aLa": [
            "vita"
        ],
        "qEn": "life",
        "aEn": [
            "life"
        ],
        "type": [
            "noun"
        ],
        "stage": 13
    },
    {
        "qLa": "v\u00c4\u00abv\u00c5\u008d, v\u00c4\u00abvere, v\u00c4\u00abx\u00c4\u00ab",
        "aLa": [
            "habito",
            "habitare",
            "vivo",
            "vivere"
        ],
        "qEn": "live, be alive",
        "aEn": [
            "live",
            "be alive"
        ],
        "type": [
            "verb"
        ],
        "stage": 19
    },
    {
        "qLa": "v\u00c4\u00abvus, v\u00c4\u00abva, v\u00c4\u00abvum",
        "aLa": [
            "vivus"
        ],
        "qEn": "alive, living",
        "aEn": [
            "alive",
            "living"
        ],
        "type": [
            "adjective"
        ],
        "stage": 29
    },
    {
        "qLa": "vix (indecl.)",
        "aLa": [
            "vix"
        ],
        "qEn": "scarcely, hardly, with difficulty",
        "aEn": [
            "scarcely",
            "hardly",
            "with difficulty"
        ],
        "type": [
            "adverb"
        ],
        "stage": 19
    },
    {
        "qLa": "voc\u00c5\u008d, voc\u00c4\u0081re, voc\u00c4\u0081v\u00c4\u00ab, voc\u00c4\u0081tus",
        "aLa": [
            "voco",
            "vocare"
        ],
        "qEn": "call",
        "aEn": [
            "call"
        ],
        "type": [
            "verb"
        ],
        "stage": 4
    },
    {
        "qLa": "vol\u00c5\u008d, velle, volu\u00c4\u00ab",
        "aLa": [
            "cupio",
            "cupere",
            "volo",
            "velle"
        ],
        "qEn": "want",
        "aEn": [
            "want"
        ],
        "type": [
            "verb"
        ],
        "stage": 13
    },
    {
        "qLa": "v\u00c5\u008ds, vestrum",
        "aLa": [
            "vos"
        ],
        "qEn": "you (plural)",
        "aEn": [
            "you"
        ],
        "type": [
            "pronoun"
        ],
        "stage": 10
    },
    {
        "qLa": "v\u00c5\u008dx, v\u00c5\u008dcis, f.",
        "aLa": [
            "clamo",
            "clamor",
            "vox"
        ],
        "qEn": "voice, shout",
        "aEn": [
            "voice",
            "shout"
        ],
        "type": [
            "noun"
        ],
        "stage": 19
    },
    {
        "qLa": "vulnus, vulneris, n.",
        "aLa": [
            "vulnus"
        ],
        "qEn": "wound",
        "aEn": [
            "wound"
        ],
        "type": [
            "noun"
        ],
        "stage": 20
    },
    {
        "qLa": "vultus, vult\u00c5\u00abs, m.",
        "aLa": [
            "vultus"
        ],
        "qEn": "expression, face",
        "aEn": [
            "expression",
            "face"
        ],
        "type": [
            "noun"
        ],
        "stage": 0
    }
]

words = parse_raw(raw)
