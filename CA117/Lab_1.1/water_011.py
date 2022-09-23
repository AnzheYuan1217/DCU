#!/usr/bin/env python3

import sys

def task(water, bucket):
    total = 0

    for i in bucket:
        b = int(i)
        water -= b
        if water >= 0:
            total += 1

    return total

def main():
    line = sys.stdin.readlines()

    a = int(line[0].strip())
    b = line[1].strip().split()

    print(task(a, b))

if __name__ == '__main__':
    main()
