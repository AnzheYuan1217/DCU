#!/usr/bin/env python3

import sys

def task(s):
    dir = {}
    a = list("abcdefghijklmnopqrstuvwxyz")

    for i in s:
        if i.isalpha():
            dir[i] = True

    if len(dir) == 26:
        return "pangram"
    else:
        for i in s:
            if i in dir:
                a.remove(i)
        return "missing " + "".join(a)

def main():
    for line in sys.stdin:
        print(task(line.strip().lower()))

if __name__ == '__main__':
    main()
