#!/usr/bin/env python3

text = []
n = 0
s = input()

while s != "end":
    text.append(s)
    n += 1
    s = input()

i = 0
while i < n:
    print(i, n, text[i])
    i += 1
