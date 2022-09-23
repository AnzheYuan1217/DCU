#!/usr/bin/env python3

import sys

def Capital(s):
    a = s[0].upper() + s[1:-1] + s[-1].upper()
    return a

def main():
    for line in sys.stdin:
        b = line.strip()
        if len(b) > 1:
            print(Capital(b))

if __name__ == '__main__':
    main()
