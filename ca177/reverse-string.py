#!/usr/bin/env python3

s = input()
i = 0
n = ""
while i < len(s):
  n = n + s[len(s) - i - 1]
  i = i + 1
print(n)
