#!/usr/bin/env python3

if __name__ == "__main__":
  a = [49, 32, 39, 13, 30, 12, 14, 19, 31, 31]

minimum = a[0]
position = 0
i = 0
while i < len(a):
  if minimum > a[i]:
    minimum = a[i]
    position = i
  i = i + 1

print(position)
