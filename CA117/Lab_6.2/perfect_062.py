#!/usr/bin/env python3

import sys

def sum_factors(s):
    sum = 0
    for i in range(1, s - 1):
        if s % i == 0:
            sum += i
    return sum

def main():
    for i in sys.stdin:
        i = int(i.strip())
        print(sum_factors(i) == i)

if __name__ == '__main__':
    main()
