#!/usr/bin/env python3

a = int(input("Please enter a number (-1 to stop):"))
b = []

while a != -1:
    if a not in b:
        b.append(a)
    a = int(input("Please enter a number (-1 to stop):"))

print(b)
