#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        i = range(1, int(line) + 1)
        a = [n for n in i if n % 3 == 0]
        b = [n ** 2 for n in i if n % 3 == 0]
        c = [n * 2 for n in i if n % 4 == 0]
        d = [n for n in i if n % 3 == 0 or n % 4 == 0]
        e = [n for n in i if n % 3 == 0 and n % 4 == 0]

        print("Multiples of 3:", a)
        print("Multiples of 3 squared:", b)
        print("Multiples of 4 doubled:", c)
        print("Multiples of 3 or 4:", d)
        print("Multiples of 3 and 4:", e)

if __name__ == '__main__':
    main()
