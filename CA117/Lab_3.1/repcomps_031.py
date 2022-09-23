#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        i = range(1, int(line) + 1)
        a = [n if n % 3 != 0 else  "X" for n in i ]
        print("Multiples of 3 replaced:", a)

if __name__ == '__main__':
    main()
