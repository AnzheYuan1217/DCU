#!/usr/bin/env python3

import sys

def roots(n):
    n = n.strip().split()
    a = int(n[0])
    b = int(n[1])
    c = int(n[2])
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        return
    x1 = (- b + delta ** 0.5) / (2 * a)
    x2 = (- b - delta ** 0.5) / (2 * a)

    return f'r1 = {x1}, r2 = {x2}'

def main():
    for i in sys.stdin:
        print(roots(i))

if __name__ == '__main__':
    main()
