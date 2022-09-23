#!/usr/bin/env python3

n = int(input())
i = 0
x = 0

while i < n:
    print(-x)
    x = (x + 1) % 3
    i += 1
