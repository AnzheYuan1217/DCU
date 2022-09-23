#!/usr/bin/env python3

x = int(input())
y = int(input())
r = int(input())

a = int(input())
b = int(input())
c = int(input())

if ((x - a) ** 2) + ((y - b) ** 2) < ((r + c) ** 2):
  print("yes")
else:
  print("no")
