#!/usr/bin/env python3

s = input()
while s != "end":
  code = s.split()
  if code[0] == "3":
    print(" ".join(code))
  s = input()
