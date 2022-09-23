#!/usr/bin/env python3

i = 0
total = 0
while i < 10:
  n = int(input())
  total = total + int((n ** 2) ** 0.5)
  i = i + 1
print(total)
