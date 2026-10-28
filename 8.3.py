password = input("Enter a password").strip()
if len(password) < 8:
    print("WEAK")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif not ch.isspace():
            has_special = True
    kinds = sum([has_upper, has_lower, has_digit, has_special])
    if kinds == 4:
        print("STRONG")
    elif kinds >= 2:
        print("MODERATE")
    else:
        print("WEAK")

