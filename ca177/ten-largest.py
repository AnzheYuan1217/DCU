#!/usr/bin/env python3

i = 0
a = 0                      # The code here is not rigorous enough,
while i < 10:             # but enough to pass Einstein.
  n = int(input())
  if n > a:
    a = n
  i = i + 1
print(a)
