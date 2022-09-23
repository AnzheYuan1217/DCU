#!/usr/bin/env python3

import sys

def main():
    dir = {}
    with open(sys.argv[1]) as f:
        for lines in f:
            (name, number, email) = lines.strip().split()
            dir[name] = number, email

    for i in sys.stdin:
        i = i.strip()
        print(f'Name: {i:s}')
        if i in dir:
            print(f'Phone: {dir[i][0]:s}')
            print(f'Email: {dir[i][1]:s}')
        else:
            print("No such contact")

if __name__ == '__main__':
    main()
