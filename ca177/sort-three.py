#!/usr/bin/env python3

a = []
i = 0
while i < 3:
    a.append(int(input()))
    i += 1

if a[0] > a[1]:
    m = a[0]
    n = a[1]
    a[1] = m
    a[0] = n

if a[1] > a[2]:
    m = a[1]
    n = a[2]
    a[2] = m
    a[1] = n

if a[0] > a[1]:
    m = a[0]
    n = a[1]
    a[1] = m
    a[0] = n

i = 0
while i < 3:
    print(a[i])
    i += 1
