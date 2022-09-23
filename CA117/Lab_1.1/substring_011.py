#!/usr/bin/env python3

import sys

def task(s):
    a = s.lower().split()
    return a[0] in a[1]

def main():
    for line in sys.stdin:
        b = line.strip()
        print(task(b))


if __name__ == '__main__':
    main()
