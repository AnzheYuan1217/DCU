#!/usr/bin/env python3

import sys

def main():
    dir = {}
    with open(sys.argv[1]) as f:
        for lines in f:
            (name, number) = lines.strip().split()
            dir[name] = number

    for i in sys.stdin:
        i = i.strip()
        print(f'Name: {i}')
        if i in dir:
            print(f'Phone: {dir[i]}')
        else:
            print("No such contact")

if __name__ == '__main__':
    main()
