#!/usr/bin/env python3

s = input()

while s != "end":
    a = ""
    i = 0
    while i < len(s):
        if (s[i] <= "z" and s[i] >= "a") or (s[i] <= "Z" and s[i] >= "A"):
            a += s[i]
        i += 1
    print(a)
    s = input()
