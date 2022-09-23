#!/usr/bin/env python3

import sys

def task(s):
    i = 0
    while i < len(s):
        if s[i].startswith('m'):
            s[i] = s[i].capitalize()
            break
        i += 1
    return ' '.join(s)


def main():
    for line in sys.stdin:
        a = line.strip().split() 
        print(task(a))


if __name__ == '__main__':
    main()
