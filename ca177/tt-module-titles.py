#!/usr/bin/env python3


s = input()
while s != "end":
  code = s.split()
  print(" ".join(code[5:]))
  s = input()
