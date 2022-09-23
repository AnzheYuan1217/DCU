#!/usr/bin/env python3

length = int(input())
radius = int(input())

area_s = length ** 2
area_c = 3.14 * (radius ** 2)

if area_s == area_c:
  print("same")
elif area_s < area_c:
  print("circle")
else:
  print("square")
