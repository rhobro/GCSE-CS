import time as t
from datetime import datetime as dt

SHOP_NAME = r"""
__________.__          _____                 __   
\______   \__| ____   /     \ _____ ________/  |_ 
 |    |  _/  |/ ___\ /  \ /  \\__  \\_  __ \   __\
 |    |   \  / /_/  >    Y    \/ __ \|  | \/|  |  
 |______  /__\___  /\____|__  (____  /__|   |__|  
        \/  /_____/         \/     \/"""


def menu(basket):
    inp = ""

    while True:
        print("c - continue")
        name = input("Enter product name: ")
        if name == "c":
            break
        price = float(input("Enter price: "))
        dcount = float(input("Enter discount %: "))

        basket.append((name, price, dcount))


def receipt(basket):
    cprint("""\n\n         Item          Price   Discount  Final Price
------------------------------------------------------""")
    sigma_all = sum([e[1] for e in basket])
    sigma_discount = 0
    for name, price, discount in basket:
        discounted_price = (100 - discount) / 100 * price
        cprint("|   %16s | Â£%.2f |  %3d" % (name, price, discount) + "%" + f"   |    Â£%.2f    |" % discounted_price)
        sigma_discount += discounted_price
    cprint("|____________________________________________________|")

    cprint("\n\nTotal Price: Â£%.2f" % sigma_all)
    cprint("Total Discount: Â£%.2f" % (sigma_all - sigma_discount))
    cprint("Final Price: Â£%.2f" % sigma_discount)

    cprint("\nThank you for shopping at " + SHOP_NAME)


last = 0
gap = 0.5


def cprint(string):
    global last

    now = t.time()
    if now - last < gap:
        extra = gap - (now - last)
        t.sleep(extra)
    print(string)

    last = t.time()


def main():
    print(SHOP_NAME)
    cprint(dt.today().date().strftime("%d-%m-%Y"))

    basket = [
        ("Baked Beans", 0.89, 50),
        ("Loaf of bread", 0.99, 0),
        ("6 x Cans of cola", 2.99, 0),
        ("Pasta", 0.75, 10),
        ("Rice", 1.98, 50),
        ("Flour", 0.94, 0),
        ("Breakfast cereal", 1.49, 0)
    ]
    menu(basket)
    receipt(basket)


if __name__ == "__main__":
    main()
