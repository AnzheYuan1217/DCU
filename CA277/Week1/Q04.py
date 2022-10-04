#!/usr/bin/env python3

number = -9256345678
count = 0

number = abs(number)
if number == 0:		# if the input is 0
    print(1)
else:
    while number != 0:
        number = number // 10
        count += 1
    print(count)


