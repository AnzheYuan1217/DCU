#!/usr/bin/env python3

print("Please enter a list of numbers:")
lis = input().split(" ")
s = int(lis[0])

t = True
for i in lis[1:]:
    if int(i) <= s:
        t = False
        break
    s += int(i)

print(t)
