#!/usr/bin/env python3

import sys

def task(s, n):
    return (f'{s:^{n}s}')

def main():
    text = sys.stdin.read().strip().split("\n")

    a = 0
    for b in text:
        if len(b) > a:
            a = len(b)

    for i in text:
        print(task(i, a))

if __name__ == '__main__':
    main()
