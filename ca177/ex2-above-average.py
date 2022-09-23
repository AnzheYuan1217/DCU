#!/usr/bin/env python3

a = []
n = int(input())
total = 0
i = 0
while n != 0:
  a.append(n)
  total += n
  i += 1
  n = int(input())

average = total // i

j = 0
while j < len(a):
  if a[j] > average:
    print(a[j])
  j += 1
