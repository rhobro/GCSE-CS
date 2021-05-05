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
        choice = input("Choose: ").lower()

        if choice == "S":
            pass

        if choice == "T":
            for i in vocab:


        elif choice == "Q":
            break


if __name__ == "__main__":
    main()
