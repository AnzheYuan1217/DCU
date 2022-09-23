#!/usr/bin/env python3

a = []
n = input()
while n != "end":
    a.append(int(n))
    n = input()
m = int(input())

i = m
position = i
while i < len(a):
    if a[position] > a[i]:
        position = i
    i += 1

print(position)
