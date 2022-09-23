#!/usr/bin/env python3

count = 0

s = input()
while s != "end":
   i = 0
   while i < len(s):

      while i < len(s) and s[i] == " ":
         i = i + 1
      j = i

      while j < len(s) and s[j] != " ":
         j = j + 1

      if i <= len(s):
         count = count + 1
         print(s[i:j])
         i = j

   s = input()

print(count)
