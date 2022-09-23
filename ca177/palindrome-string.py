#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and (s[i] == s[-i - 1]):
    i += 1

if i == len(s):
    print("palindrome")
