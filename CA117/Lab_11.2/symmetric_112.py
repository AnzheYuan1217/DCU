#!/usr/bin/usr python3

import sys

def main():

    line = [lines.strip() for lines in sys.stdin]

    a = line[::2]
    b = line[1::2]

    print('\n'.join(a + b[::-1]))

if __name__ == '__main__':
    main()
