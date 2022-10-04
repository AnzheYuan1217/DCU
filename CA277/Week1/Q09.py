#!/usr/bin/env python3

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

s = "welcome"
result = ""

for i in range(len(s)):
    result += alphabets[alphabets.index(s[i]) + 1]

print(result)
