#!/usr/bin/env python3

import sys

def main():

    i = [n.strip() for n in sys.stdin]
    a = [n for n in i if len(n) == 17]
    b = [n for n in i if len(n) >= 18]
    c = [n for n in i if n.lower().count('a') == 4]
    d = [n for n in i if n.lower().count('q') >= 2]
    e = [n for n in i if "cie" in n.lower()]
    f = [n for n in i if sorted(n.lower()) == sorted("angle") and n.lower() != "angle"]

    print("Words containing 17 letters:", a)
    print("Words containing 18+ letters:", b)
    print("Words with 4 a's:", c)
    print("Words with 2+ q's:", d)
    print("Words containing cie:", e)
    print("Anagrams of angle:", f)

if __name__ == '__main__':
    main()
