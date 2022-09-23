#!/usr/bin/env python3

import sys

def prime(s):
    for i in range(2, s):
        if s % i == 0:
            return False
    return True

def main():
    for line in sys.stdin:
        i = int(line)
        a = [n for n in range(2, i) if prime(n)]
        print("Primes:", a)

if __name__ == '__main__':
    main()
