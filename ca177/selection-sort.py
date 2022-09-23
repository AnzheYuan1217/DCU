#!/usr/bin/env python3

a = []
n = input()
while n != "end":
    a.append(int(n))
    n = input()

i = 0

while i < len(a):
    p = i
    j = i + 1
    while j < len(a):

        if a[p] > a[j]:
            p = j
        j += 1
    t = a[i]
    a[i] = a[p]
    a[p] = t
    i += 1

i = 0
while i < len(a):
    print(a[i])
    i += 1
