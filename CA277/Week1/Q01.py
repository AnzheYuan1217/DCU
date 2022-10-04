#!/usr/bin/env python3

lis = [-1, 3, 5, 6, 99, 12, 2]		# input

a = lis[0]
for i in lis:
    if i > a:
        a = i
print(a)    # or just: print(max(lis))
