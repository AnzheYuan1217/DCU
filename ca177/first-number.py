#!/usr/bin/env python3

s = input()

i = 0

while i < len(s) and (s[i] < "0" or "9" < s[i]):
    i += 1

j = i
while j < len(s) and ("0" <= s[j] and s[j] <= "9"):
    j += 1

if i < len(s):
    print(s[i:j], i)
