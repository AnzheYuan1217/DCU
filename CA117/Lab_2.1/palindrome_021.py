#!/usr/bin/env python3

import sys

def main():
    for i in sys.stdin:
        a = []
        for j in i.strip().lower():
            if j.isalnum():
                a.append(j)

        print(a == a[::-1])

if __name__ == '__main__':
    main()
