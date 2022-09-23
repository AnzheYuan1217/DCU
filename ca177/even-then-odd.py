#!/usr/bin/env python3

odd = []
n = input()
while n != "end":
    if int(n) % 2 == 0:
        print(n)
    else:
        odd.append(n)
    n = input()

i = 0
while i < len(odd):
    print(odd[i])
    i += 1
