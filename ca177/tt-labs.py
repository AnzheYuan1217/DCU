#!/usr/bin/env python3

s = input()

while s != "end":
  code = s.split()
  if int(code[2]) > 1:
    print(s)
  s = input()
