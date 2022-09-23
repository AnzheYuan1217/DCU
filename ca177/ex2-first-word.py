#!/usr/bin/env python3

s = input()

i = 0
while i < len(s) and s[i] == " ":
  i += 1

start = i

i += 1
while i < len(s) and s[i] != " ":
  i += 1
end = i

if i < len(s):
  print(s[start:end])
