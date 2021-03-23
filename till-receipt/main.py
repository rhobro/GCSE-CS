import time as t
from datetime import datetime as dt

SHOP_NAME = "BigMart"


def receipt(basket):
    print(SHOP_NAME)
    cprint(dt.today().date().strftime("%d-%m-%Y"))

    cprint("""\n\n        Item           Price   Discount   Final Price
  ---------------------------------------------------------""")
    sigma_all = sum([e[1] for e in basket])
    sigma_discount = 0
    for name, price, discount in basket:
        discounted_price = (100 - discount) / 100 * price
        cprint("%20s | £%.2f |  %3d" % (name, price, discount) + "%" + f"   |     £%.2f" % discounted_price)
        sigma_discount += discounted_price

    cprint("\n\nTotal Price: £%.2f" % sigma_all)
    cprint("Total Discount: £%.2f" % (sigma_all - sigma_discount))
    cprint("Final Price: £%.2f" % sigma_discount)

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


if __name__ == "__main__":
    receipt([
        ("Baked Beans", 0.89, 50),
        ("Loaf of bread", 0.99, 0),
        ("6 x Cans of cola", 2.99, 0),
        ("Pasta", 0.75, 10),
        ("Rice", 1.98, 50),
        ("Flour", 0.94, 0),
        ("Breakfast cereal", 1.49, 0)
    ])
