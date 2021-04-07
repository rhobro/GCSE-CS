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
    while True:
        cprint("""
        p - proceed to checkout
        c - clear basket
        """)
        name = input("Enter product name: ")
        if name == "p":
            break
        if name == "c":
            basket = []
            continue
        # get product details
        price = float(input("Enter price: "))
        discount = float(input("Enter discount %: "))

        basket.append((name, price, discount))

    return basket


def receipt(basket):
    """
    Formatted printing of receipt with columns and rows
    :param basket:
    :return:
    """

    cprint("""\n\n         Item            Price     Discount    Final Price
------------------------------------------------------------------""")
    sigma_all = sum([e[1] for e in basket])
    sigma_discount = 0
    for name, price, discount in basket:
        discounted_price = (100 - discount) / 100 * price
        cprint("|   %16s | £%10.2f |  %3d" % (name, price, discount) + "%" + f"   |    £%10.2f    |" % discounted_price)
        sigma_discount += discounted_price
    cprint("|________________________________________________________________|")

    cprint("\n\nTotal Price: £%.2f" % sigma_all)
    cprint("Total Discount: £%.2f" % (sigma_all - sigma_discount))
    cprint("Final Price: £%.2f" % sigma_discount)

    cprint("\nThank you for shopping at " + SHOP_NAME)


last = 0
gap = 0.5


def cprint(msg):
    """
    Custom print function to print one line at a time, to simulate a receipt printing machine
    :param msg:
    :return:
    """

    global last

    for s in msg.split("\n"):
        now = t.time()
        if now - last < gap:
            extra = gap - (now - last)
            t.sleep(extra)
        last = t.time()

        print(s)


def main():
    cprint(SHOP_NAME)
    cprint(dt.today().date().strftime("%d-%m-%Y"))

    # initial basket values
    basket = [
        ("Baked Beans", 0.89, 50),
        ("Loaf of bread", 0.99, 0),
        ("6 x Cans of cola", 2.99, 0),
        ("Pasta", 0.75, 10),
        ("Rice", 1.98, 50),
        ("Flour", 0.94, 0),
        ("Breakfast cereal", 1.49, 0)
    ]
    # use menu to allow user to add / remove from basket
    basket = menu(basket)
    # print receipt at the end of the transaction
    receipt(basket)


if __name__ == "__main__":
    main()
