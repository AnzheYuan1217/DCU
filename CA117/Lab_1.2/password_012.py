#!/usr/bin/env python3

import sys

def task(s):
    digit, lower, upper, other = 0, 0, 0, 0
    for i in s:
        if i.isdigit():
            digit = 1

        elif i.islower():
            lower = 1

        elif i.isupper():
            upper = 1

        else:
            other = 1

    return digit + lower + upper + other

def main():
    for line in sys.stdin:
        print(task(line.strip()))

if __name__ == '__main__':
    main()
