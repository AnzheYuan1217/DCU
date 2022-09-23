#!/usr/bin/env python3

i = 0
n = 200
while i < 10:
  a = int(input())
  if a > 0 and a < n:
    n = a
  i = i + 1
print(n)
