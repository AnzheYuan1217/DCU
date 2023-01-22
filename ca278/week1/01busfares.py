#!/usr/bin/env python3

age = int(input("Please enter your age:"))

if age >= 5 and age <= 16:
    s = "Your fare is: 0.75 euro."
elif age >= 17 and age <= 20:
    s = "Your fare is: 1.25 euro."
elif age >= 21 and age <= 64:
    s = "Your fare is: 1.5 euro."
else:
    s = "You go free!"

print(s)
