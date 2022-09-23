#!/usr/bin/env python3

"""
Add es if the noun ends in ch, sh, x, s or z.
If a noun ends in a consonant + y drop the y and add ies.
If a noun ends in f (or fe) drop the f (or fe) and add ves.
If a noun ends in o add es.
Otherwise add s.
"""
import sys

def task(s):
    a = s[-2:]
    b = s[-1]
    c = s[-2]
    es = {
        "ch": True,
        "sh": True,
        "x": True,
        "s": True,
        "z": True,
        "o": True
    }
    vowel = {
        "a": True,
        "e": True,
        "i": True,
        "o": True,
        "u": True
    }

    if b in es or a in es:
        print(s + "es")
    elif b == "y" and c not in vowel:
        print(s[:-1] + "ies")
    elif a == "fe":
        print(s[:-2] + "ves")
    elif b == "f":
        print(s[:-1] + "ves")
    else:
        print(s + "s")
    return

def main():
    for line in sys.stdin:
        task(line.strip())



if __name__ == '__main__':
    main()
