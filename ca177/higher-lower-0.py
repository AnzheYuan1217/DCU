#!/usr/bin/env python3

a = int(input())
if a != 0:
    b = int(input())
    while b != 0:
        if a > b:
            print("lower")
        elif a < b:
            print("higher")
        else:
            print("equal")
        a = b
        b = int(input())
