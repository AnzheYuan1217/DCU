#!/usr/bin/env python3

count = 0

s = input()
while s != "end":
   i = 0
   while i < len(s):
      # Find the next non-space character; this will be the start
      # of the next word.  Linear search.
      #
      while i < len(s) and s[i] == " ":
         i = i + 1

      # Find the next space character; this will be the end
      # of the next word.  Linear search.
      #
      j = i
      while j < len(s) and s[j] != " ":
         j = j + 1

      # Did we find a word?
      #
      if i <= len(s):
         count = count + 1
         # Advance i so that on the next iteration we will be
         # searching for the NEXT word.  (If we didn't find a word,
         # then j and i will both have already fallen off of the
         # end of s, so we don't need to do anything for that case.)
         #
         i = j

   # We're done with that line; move on to the next line.
   #
   s = input()

print(count)
