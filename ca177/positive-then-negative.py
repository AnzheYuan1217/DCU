#!/usr/bin/env python3

n = int(input())
a = []
while n != 0:
    if n > 0:
        print(n)
    else:
        a.append(n)
    n = int(input())
i = 0
while i < len(a):
    print(a[i])
    i += 1
