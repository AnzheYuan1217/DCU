#!/usr/bin/env python3

print("Enter a number:")

a = int(input())

sum = 0
for i in range(a+1):
    b = a - i
    print(b)
    sum += b

print("")
print(sum)
