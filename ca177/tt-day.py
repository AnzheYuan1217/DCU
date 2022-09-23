#!/usr/bin/env python3

a = []
s = input()
while s != "end":
  a.append(s)
  s = input()
b = input()

i = 0
while i < len(a):
  code = a[i].split()
  if code[0] == b:
    print(" ".join(code))
  i += 1
