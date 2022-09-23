#!/usr/bin/env python3

import sys

def main():
    dir = {
         "0": "zero",
         "1": "one",
         "2": "two",
         "3": "three",
         "4": "four",
         "5": "five",
         "6": "six",
         "7": "seven",
         "8": "eight",
         "9": "nine",
         "10": "ten", }
    for lines in sys.stdin:
        line = lines.strip().split()
        a = [dir[n] if n in dir else "unknown" for n in line]
        print(" ".join(a))

if __name__ == '__main__':
    main()
