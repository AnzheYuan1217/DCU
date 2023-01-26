#!/usr/bin/env python3

a = input("Please enter a comma-separated list of scores:")
b = a.split(",")
c = {"Draws": 0, "Losses": 0, "Wins": 0}

if len(set(a[::2])) != 1 and a[1] == ',':  # or just a[1] == ','
    for i in b:
        if int(i) == 3:
            c["Wins"] += 1
        elif int(i) == 1:
            c["Draws"] += 1
        elif int(i) == 0:
            c["Losses"] += 1

for k, v in c.items():
    print(f"{k}: {v}")

