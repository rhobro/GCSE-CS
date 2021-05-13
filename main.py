import random as rand

from vocab import words

# displayed menu
# test option is invisible as an easter egg for developers
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
            # start

            # input params
            latin = input("Test from latin to english? (T/f) : ").strip().lower() == "t"
            n_qs = int(input("Number of questions: "))
            stages = [int(s)
                      for s in input("Comma separated list of stages to test on: ").replace(" ", "").split(",")
                      if s.isdigit()]

            # test
            test(latin, n_qs, stages)

        if choice == "T":
            # test vocab list

            for w in words:
                print(f"""
Latin   : {w.get_a_latin()}
English : {w.get_a_english()}
Type    : {w.get_types()}
Stage   : {w.stage}""")

        elif choice == "Q":
            # quit
            break


def test(ln, n_qs, stages):
    filtrate = [w for w in words if w.stage in stages]
    rand.shuffle(filtrate)
    n_qs = n_qs if 0 < n_qs <= len(filtrate) else len(filtrate)  # logic to choose number of questions
    filtrate = filtrate[:n_qs]  # choose number of questions being tested on

    correct_count = 0

    for i, w in enumerate(filtrate):
        clear()

        q = w.q_la if ln else w.q_en  # choose correct question value
        a = w.a_en if ln else w.a_la  # choose correct answer value

        # ask for guess
        print(f"""
Question {i + 1} / {len(filtrate)}
Score    {correct_count} / {i}
""")
        inp = input(f"What's '{q}'? : ")
        if inp in a:
            input("Well done")
            correct_count += 1

        else:
            input(f"Nope, it's '{w.get_a_english() if ln else w.get_a_latin()}'")

        clear()


def clear():
    print("".join(["\n" for _ in range(1000)]))


if __name__ == "__main__":
    main()
