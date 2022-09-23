#!/usr/bin/env python3

import sys

def main():
    cups = ["","",""]
    line = sys.stdin.readlines()
    cups[int(line[0].strip()) - 1] = "price"

    for i in "".join(line[1:]).strip():
        if i == "A":
            cups[0], cups[1] = cups[1], cups[0]
        elif i == "B":
            cups[1], cups[2] = cups[2], cups[1]
        else:
            cups[0], cups[2] = cups[2], cups[0]

    print(cups.index("price") + 1)

if __name__ == '__main__':
    main()
