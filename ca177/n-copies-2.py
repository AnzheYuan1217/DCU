#!/usr/bin/env python3

s = input()
n = int(input())

a = (s + "-") * n
a = a[:len(a) - 1]

print(a)
