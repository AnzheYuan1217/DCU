#!/usr/bin/env python3

import sys

def task(s):
    i = 1
    if len(s) < int(s[-1]):
        for j in s:
            if str(i) in j:
                i += 1
            else:
                return i
    else:
        return "no room"

def main():
    for i in sys.stdin:
        i = i.strip().split()
        i.sort()
    print(task(i))

if __name__ == '__main__':
    main()
