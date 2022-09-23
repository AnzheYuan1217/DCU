#!/usr/bin/env python3

text_a = input()
text_b = input()
text_c = input()
a = len(text_a)
b = len(text_b)
c = len(text_c)
if a > b and a > c:
  print(text_a)
elif b > a and b > c:
  print(text_b)
else:
  print(text_c)
