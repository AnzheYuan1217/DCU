#!/usr/bin/env python3

number = 711

sum_all = 0
for i in str(number):
    sum_all += int(i)

print(number % sum_all == 0)
