import re

def validate_credit_cards(credit_cards):
    valid_structure = r"[456]\d{3}(-?\d{4}){3}$"
    no_four_repeats = r"((\d)-?(?!(-?\2){3})){16}"
    filters = valid_structure, no_four_repeats

    for cc in credit_cards:
        if all(re.match(f, cc) for f in filters):
            print("Valid")
        else:
            print("Invalid")

TESTER = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")
for _ in range(int(input().strip())):
    #print("Valid" if TESTER.search(input().strip()) else "Invalid")
    print("--------")
    validate_credit_cards(input())

