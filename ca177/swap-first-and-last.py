#!/usr/bin/env python3

s = input()

a = s[(len(s) - 1):]     # last
b = s[1: (len(s) - 1)]   # middle
c = s[:1]                # first

print(a + b + c)
