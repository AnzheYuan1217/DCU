#!/usr/bin/env python3

a = []
n = input()
while n != "end":
    a.append(int(n))
    n = input()

i = 0
position = 0
while i < len(a):
    if a[position] > a[i]:
        position = i
    i += 1

print(position)
