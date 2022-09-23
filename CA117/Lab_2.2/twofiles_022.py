#!/usr/bin/env python3

import sys

def main():
    with open(sys.argv[1]) as f:
        one = f.readlines()

    with open(sys.argv[2]) as f:
        two = f.readlines()

    for i in range(len(one)):
        print((one[i])[:-1])
        print((two[i])[:-1])


if __name__ == '__main__':
    main()
