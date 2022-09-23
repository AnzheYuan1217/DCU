#!/usr/bin/env python3

s = int(input())
while s % 3 != 0 or s % 5 != 0:
    s = int(input())
print(s)
