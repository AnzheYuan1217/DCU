#!/usr/bin/env python3

print("Please enter the temperatures in Celsius (comma-separated):")
lis = {}
celsius = input().split(",")
for i in celsius:
    lis[float(i)] = (float(i) * 1.8 + 32)
print("Celsius Fahrenheit")
for k, v in lis.items():
    print(k, v)
