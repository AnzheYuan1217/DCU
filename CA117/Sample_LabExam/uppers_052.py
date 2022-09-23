#!/usr/bin/env python3

import sys

def main():
    for line in sys.stdin:
        a = []
        for i in line.strip():
            if i.islower():
                i = i.replace(i, " ")
            a.append(i)

        a = "".join(a).split(" ")
        print(max(a))

if __name__ == '__main__':
    main()
