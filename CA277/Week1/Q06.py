#!/usr/bin/env python3

s = "The cow jumped over the moon."		# input1
input_list = ["cow", "over"]			# input2

for i in input_list:
    if i in s:
        s = s.replace(i, '*'*len(i))
print(s)
