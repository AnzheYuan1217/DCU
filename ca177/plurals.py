#!/usr/bin/env python3

s = input()
line = len(s)
while s != "end":
    if s[-1] == "s":
        print(s)
    s = input()
