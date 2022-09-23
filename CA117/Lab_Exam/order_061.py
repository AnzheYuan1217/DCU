#!/usr/bin/env python3

import sys

def task(s):
    a = []
    for n in s:
        if n in list("nice"):
            if n not in a:
                a.append(n)
            else:
                return False

    if "".join(a) == "nice":
        return True
    else:
        return False

def main():
    for i in sys.stdin:
        i = i.strip()
        if task(i):
            print(i)

if __name__ == '__main__':
    main()
