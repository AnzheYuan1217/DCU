#!/usr/bin/env python3

import sys
def vowels(s):
    return "a" in s and "e" in s and "i" in s and "o" in s and "u" in s

def most_e(s):
    a = 0
    for i in s:
        if a < i.count("e"):
            a = i.count("e")
    return a
def main():
    i = [n.strip() for n in sys.stdin]

    a = [n for n in i if vowels(n.lower())]
    a.sort(key = len)
    print("Shortest word containing all vowels:", a[0])

    b = [n for n in i if n[-4:] == "iary"]
    print("Words ending in iary:", len(b))

    num = most_e(i)
    c = [n for n in i if n.count("e") == num]
    print("Words with most e's:", c)

if __name__ == '__main__':
    main()
