import json
from vocab import *

DEBUG = True

MENU = """
 __________________
||||||||||||||||||||
|| S - start quiz ||
|| Q - quit       ||
||||||||||||||||||||
"""


def main():
    while True:
        print(MENU)
        choice = input("Choose: ").upper()

        if choice == "S":
            latin = input("Test from latin to english? (T/f)").strip().lower() == "t"
            n_qs = int(input("Number of questions: "))
            stages = [int(s) for s in input("Comma separated list of stages to test on: ").split(",")]

            test(latin, n_qs, stages)

        if choice == "T":
            print(json.dumps(vocab, indent="    "))

        elif choice == "Q":
            break


def test(ln, n_qs, stages):
    filtrate = [w for w in vocab if w["stage"] in stages]
    n_qs = n_qs if 0 < n_qs <= len(filtrate) else len(filtrate)
    filtrate = filtrate[:n_qs]

    for w in filtrate:
        clear()

        q = w["qLa"] if ln else w["qEn"]
        a = w["aEn"] if ln else w["aLa"]

        inp = input(f"What's {q}? : ")
        if inp in a:
            input("Well done")
        else:
            input("Nope")
        clear()


def clear():
    print("".join(["\n" for _ in range(1000)]))


if __name__ == "__main__":
    main()
