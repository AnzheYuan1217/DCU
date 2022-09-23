#!/usr/bin/env python3

import sys

def vowels(s):
    return "a" in s or "e" in s or "i" in s or "o" in s or "u" in s

def tagger(item):
   return item[1]

def main():
    dir = {}
    for i in sys.stdin.read().strip().lower():

        if vowels(i):
            if i in dir:
                dir[i] += 1
            else:
                dir[i] = 1

    for k, v in sorted(dir.items(), key = tagger, reverse=True):
        print(f'{k} : {v:>{len(str(max(dir.values())))}}')

if __name__ == '__main__':
    main()
