#!/usr/bin/env python3

weight = float(input("Please enter your weight in lbs:"))

# 1 st = 14 lbs
if weight <= 0:
    print("Invalid input. Your weight must be positive.")
else:

    a = int(weight // 14)  # stone
    a = "" if a == 0 else str(a) + "st"

    b = weight % 14  # pound
    b = "" if int(b) == 0 else str(b) + "lbs"

    print(f"Your weight in stones and lbs is {a}{b}.")