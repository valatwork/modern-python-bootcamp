age = 21
# 2-8 2 USD ticket
# 65 5 USD ticket
# 10 USD everyone else

if not ((age >= 2 and age <= 8) or age >= 65):
    print("YOU PAY 10 USD and are not a child or senior")
else:
    print("YOU ARE A CHILD OR SENIOR!")