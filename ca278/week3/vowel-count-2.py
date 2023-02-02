#!/usr/bin/env python3

print("Please enter a word:")
out = ""
vowels = {'a', 'e', 'i', 'o', 'u'}

for i in input():
    if i.lower() not in vowels:
        out += i

print(out)
