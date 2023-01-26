#!/usr/bin/env python3

"""
def check_comma(s):
    i = 1
    while i < len(s):
        if s[i] != ",":
            return False
        i += 2
    return True
"""

a = input("Please enter a comma-separated list of scores:")
b = a.split(",")
c = {"Draws": 0, "Losses": 0, "Wins": 0}
valid = False
if a[1] == ',':  # or check_comma(a)
    valid = True
    for i in b:
        if int(i) == 3:
            c["Wins"] += 1
        elif int(i) == 1:
            c["Draws"] += 1
        elif int(i) == 0:
            c["Losses"] += 1
        else:
            valid = False
            break

if valid:
    for k, v in c.items():
        print(f"{k}: {v}")
else:
    print("The list of scores is not valid.")
