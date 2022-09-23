#!/usr/bin/env python3

s = input()
k = ""
i = 0
while i < len(s):
  if i % 2 == 0:
    k = k + s[(i)]
  i = i + 1
print(k)
