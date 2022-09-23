#!/usr/bin/env python3

a = input()
b = input()
i = 0
j = 0
if len(a) == len(b):
  while i < len(a):
    if a[i] == b[i] or a[i] == "-":
      j += 1
    i += 1

if j == len(a):
  print("yes")
else:
  print("no")
