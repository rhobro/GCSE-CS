def validate(t: str, s: str) -> bool:
    # false if length is not same
    if len(s) != len(t):
        return False

    # above check ensures zip() is valid
    for t_c, s_c in zip(t, s):
        if t_c == "L":
            # letter
            if not s_c.isalpha():
                return False

        elif t_c == "N":
            # number
            if not s_c.isdigit():
                return False

        else:
            # chars in between e.g. spaces
            if t_c != s_c:
                return False

    # all checks passed to reach end of func
    return True


template = ""

while True:
    new_template = input("Template: ").upper()
    if new_template != "":
        template = new_template

    test = input("Test string: ")
    print(f"Valid = {validate(template, test)}")
