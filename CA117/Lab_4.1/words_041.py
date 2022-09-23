#!/usr/bin/env python3

import sys, string

def main():
    dir = {}
    for i in sys.stdin:
        for word in i.lower().strip().split(" "):
            word = word.strip(string.punctuation)

            if word in dir:
                dir[word] += 1
            else:
                dir[word] = 1

    
    for k, v in sorted(dir.items()):
        print(f'{k} : {v}')

if __name__ == '__main__':
    main()
