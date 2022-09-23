#!/usr/bin/env python3

n = int(input())
i = 1
x = 0
if n == 0:
    a = ""
else:
    a = str(x)

while i < n:
    x = ((x + 1) % 3)
    a = a + " " + str(-x)
    i += 1

print(a)
