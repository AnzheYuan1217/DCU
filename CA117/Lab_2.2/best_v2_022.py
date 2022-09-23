#!/usr/bin/env python3

import sys

def main():
    mark = 0
    with open(sys.argv[1]) as f:
        for line in f.readlines():
            i = line.split()
            if not i[0].isdigit():
                print(f'Invalid mark {i[0]} encountered. Exiting.')
                return
            if int(mark) < int(i[0]):
                mark, name = i[0], " ".join(i[1:])
    print(f'Best student: {name}\nBest mark: {mark}')

if __name__ == '__main__':
    main()
