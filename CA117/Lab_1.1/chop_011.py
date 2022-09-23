#!/usr/bin/env python3

import sys
"""
a = sys.stdin.readlines()
i = 0
while i < len(a):
    b = a[i].rstrip()
    if len(b) > 2:
        print(b[1:-1])
    i += 1
"""

def chop(s):
    return s[1:-1]

def main():
    for line in sys.stdin:
        chopped = chop(line.strip())
        if chopped:  # The empty string '' is interpreted as False
            print(chopped)

if __name__ == '__main__':
    main()
