#!/usr/bin/env python3

import sys

def task(s):
    a = s[0].split(".")
    b = a[1].capitalize()
    left = a[0].capitalize()
    right = ""
    for i in b:
        if not i.isnumeric():
            right += i
        else:
            return " ".join([left, right])


def main():
    for line in sys.stdin:
        n = line.strip().split("@")
        print(task(n))

if __name__ == '__main__':
    main()
