#!/usr/bin/env python3

import sys

def task(a, b):
    for c in a:
        if c in b:
            b.remove(c)
        else:
            return False
    return True

def main():
    for i in sys.stdin:
        a = (i.split())[0]
        b = ((i.split())[1])
        if len(a) == len(b):
            print(task(a, list(b)))
        else:
            print(False)

if __name__ == '__main__':
    main()
