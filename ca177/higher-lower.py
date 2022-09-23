#!/usr/bin/env python3

a = int(input())
i = 0
while i < 5:
    b = int(input())
    if a > b:
        print("lower")
    elif a < b:
        print("higher")
    else:
        print("equal")
    a = b
    i = i + 1
