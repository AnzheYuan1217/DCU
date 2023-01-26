#!/usr/bin/env python3

a = int(input("Please enter a number (-1 to stop):"))
b = []
c = {}
while a != -1:
    if a not in c:
        c[a] = 1
    else:
        c[a] += 1
    if a not in b:
        b.append(a)

    a = int(input("Please enter a number (-1 to stop):"))

print(b)
for k, v in c.items():
    print(f"{k} occurred {v} times")
