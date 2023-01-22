#!/usr/bin/env pytho3

year = int(input("Please enter the year:"))

if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    answer = "is not"

else:
    answer = "is"

# answer = "is not" if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0) else "is"


print(f"{year} {answer} a leap year.")
