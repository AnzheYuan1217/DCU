#!/usr/bin/env python3

print("Please enter a list of values:")
a = []
s = input()
if s != "":
    a = s.split(" ")

print("Please enter a second list of values:")
b = []
s = input()
if s != "":
    b = s.split(" ")

print(f"Removing elements of {b} from {a}")
c = []
for i in a:
    if i not in b:
        c.append(i)

print(c)
