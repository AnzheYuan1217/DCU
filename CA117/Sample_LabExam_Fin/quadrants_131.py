#!/usr/bin/env python3

import sys

def main():
    for i in sys.stdin:
        i = i.strip().split()
        x = int(i[0])
        y = int(i[1])
        if x > 0:
            if y > 0:
                print(1)
            else:
                print(2)
        elif x < 0:
            if y > 0:
                print(4)
            else:
                print(3)

if __name__ == '__main__':
    main()
