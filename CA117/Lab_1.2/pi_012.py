#!/usr/bin/env python3

import sys

def task(pi, n):
    print(f'{pi:.{n}f}')
    return

def main():
    from math import pi
    for line in sys.stdin:
        task(pi, line.strip())

if __name__ == '__main__':
    main()
