#!/usr/bin/env python3

import sys

def main():
    with open(sys.argv[1]) as f:
        j = [n.strip() for n in f.readlines()]

    for a in sys.stdin:
        a = a.strip()
        for b in j:
            if b in a:
                a = a.replace(b, "@" * len(b))
        print(a)

if __name__ == '__main__':
    main()
