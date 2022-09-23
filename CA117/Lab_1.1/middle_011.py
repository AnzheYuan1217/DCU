#!/usr/bin/env python3

import sys

def task(s):
    if len(s) % 2 == 0 and len(s) != 1:
        print("No middle character!")
    else:
        print(s[len(s) // 2])
    return

def main():
    for line in sys.stdin:
        task(line.strip())

if __name__ == '__main__':
    main()
