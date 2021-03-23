from datetime import datetime as dt

SHOP_NAME = "BigMart"


def receipt(basket):
    print(SHOP_NAME)
    print(dt.today().date().strftime("%d-%m-%Y"))

    print("""\n\n        Item           Price   Discount   Final Price
  ---------------------------------------------------------""")
    sigma_all = sum([e[1] for e in basket])
    sigma_discount = 0
    for name, price, discount in basket:
        discounted_price = (100 - discount) / 100 * price
        print("%20s | £%.2f |  %3d" % (name, price, discount) + "%" + f"   |     £%.2f" % discounted_price)
        sigma_discount += discounted_price

    print("\n\nTotal Price: £%.2f" % sigma_all)
    print("Total Discount: £%.2f" % (sigma_all - sigma_discount))
    print("Final Price: £%.2f" % sigma_discount)

    print("\nThank you for shopping at " + SHOP_NAME)


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
