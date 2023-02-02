#!/usr/bin/env python3

print("Please enter a word:")
count = 0
vowels = {'a', 'e', 'i', 'o', 'u'}
s = input()
for i in s:
    if i.lower() in vowels:
        count += 1
print(f'There are {count} vowels in {s}')
