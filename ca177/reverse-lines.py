#!/usr/bin/env python3

a = []
n = input()
while n != "end":
    a.append(n)
    n = input()

i = 0
while i < len(a):
    print(a[(len(a) - i - 1)])
    i += 1
