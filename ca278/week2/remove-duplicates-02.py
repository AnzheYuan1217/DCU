#!/usr/bin/env python3

print("Please enter a list of values:")
s = input()
a = s.split(" ") if s != "" else []

print("Please enter a second list of values:")
s = input()
b = s.split(" ") if s != "" else []

print(f"Removing elements of {b} from {a}")

""" Method 1: using a new list
c = []
for i in a:
    if i not in b:
        c.append(i)
        
print(c)
"""

""" Method 2 - edit given list
for i in b:
    if i in a:
        a.remove(i)
print(a)"""


# Method 3: Same as Method 1 but in one line.
print([i for i in a if i not in b])
