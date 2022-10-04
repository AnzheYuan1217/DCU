#!/usr/bin/env python3

input_a = [1, 2, 2, 2, 3, 4, 5]		# input1
input_b = [1, 2, 4, 5]		# input2

lis = []
for i in input_a:
    if i in input_b and i not in lis:

        lis.append(i)

print(lis)
