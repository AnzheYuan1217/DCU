#!/usr/bin/env python3

import sys

def main():
    for i in sys.stdin:
        i = i.strip().split()
        a = [n for n in i if i.count(n) == 1]
        if a == []:
            print("none")
        else:
            print(max(a))

if __name__ == '__main__':
    main()
