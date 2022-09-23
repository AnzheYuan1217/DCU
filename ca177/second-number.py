#!/usr/bin/env python3

s = input()

i = 0

while i < len(s) and (s[i] < "0" or "9" < s[i]):
    i += 1

j = i
while j < len(s) and ("0" <= s[j] and s[j] <= "9"):
    j += 1

k = j
while k < len(s) and (s[k] < "0" or "9" < s[k]):
    k += 1

m = k
while m < len(s) and ("0" <= s[m] and s[m] <= "9"):
    m += 1

if i < len(s):
    print(s[k:m], k)
