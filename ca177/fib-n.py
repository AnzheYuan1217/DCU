#!/usr/bin/env python3

n = int(input())

i = 0
a = 0
b = 1
print(a)
print(b)
while i < n - 2:
  j = a + b
  print(j)
  a = b
  b = j
  i = i + 1
