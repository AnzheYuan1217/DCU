#!/usr/bin/env python3

s = "Look before you leap."
result = True

for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        result = False
        break

print(result)
