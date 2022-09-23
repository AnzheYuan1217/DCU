#!/usr/bin/env python3

s = input()
line = len(s)
while s != "end":
    if line > len(s):
        line = len(s)
    s = input()
print(line)
