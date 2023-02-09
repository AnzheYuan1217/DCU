#!/usr/bin/env python3

import sys

file_one = sys.argv[1]
file_two = sys.argv[2]

with open(file_two) as f:
    name = f.readline().strip().lower()

names = []
with open(file_one) as f:
    for i in f.readlines():
        temp = i.split()
        if temp[1].lower() == name:
            names.append(temp[0])

if not names:
    print("No-one has that surname")
else:
    print(names)
