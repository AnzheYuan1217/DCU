#!/usr/bin/env python3

import sys

def task(left, right):

    for s in left:
        if s in right:
            right = right.replace(s, "")
        else:
            return False
    return True

def main():
    for line in sys.stdin:
        [left, right] = line.strip().lower().split()

        print(task(left, right))

if __name__ == '__main__':
    main()
