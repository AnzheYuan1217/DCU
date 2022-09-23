#!/usr/bin/env python3

total = 0
s = input()

while s != "end":
  code = s.split()
  total += int(code[2])
  s = input()

print(total)
