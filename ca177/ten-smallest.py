#!/usr/bin/env python3

i = 0
n = 0
n = int(input())
while i < 9:
  a = int(input())
  if a < n:
    n = a
  i = i + 1
print(n)
