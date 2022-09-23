#!/usr/bin/env python3

import sys

def main():
    for lines in sys.stdin:
        n = int(lines.strip())
        num = n // 400
        if n % 400 != 0:
            num += 1
        print(num)

if __name__ == '__main__':
    main()
