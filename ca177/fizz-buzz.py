#!/usr/bin/env python3

n = int(input())

i = 0

while i < n:
  a = i + 1
  if (a % 3) == 0 and (a % 5) == 0:
    print("fizz-buzz")
  elif (a % 3) == 0:
    print("fizz")
  elif (a % 5) == 0:
    print("buzz")
  else:
    print(a)
  i = i + 1
