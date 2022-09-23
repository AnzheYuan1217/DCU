#!/usr/bin/env python3

if __name__ == "__main__":
    a = ["ab", "abc", "abcd", "abcde", "abcdef", "abcdefg"]
    s = "abc"

i = 0
b = []
while i < len(a):
    word = a[i]
    if word[:len(s)] == s:
        b.append(word)
    i += 1
if len(a) > 0:
    print(b[0])
