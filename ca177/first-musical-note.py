#!/usr/bin/env python3

s = input()
i = 0
while i < len(s) and not ("a" <= s[i] and s[i] <= "g"):
    i = i + 1
print(s[i])
