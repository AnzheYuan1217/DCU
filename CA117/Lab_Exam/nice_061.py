#!/usr/bin/env python3

import sys

def task(s):
    dir = {}
    for n in s:
        if n in list("nice"):
            if n not in dir:
                dir[n] = 1
            else:
                return False
    return True

def main():
    for i in sys.stdin:
        i = i.strip()
        if task(i):
            print(i)

if __name__ == '__main__':
    main()
