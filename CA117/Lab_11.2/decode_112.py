#!/usr/bin/usr python3

import sys

def main():
    v = ['a', 'e', 'i', 'o', 'u']
    for line in sys.stdin:
        line = line.strip()
        i = 0
        s = []
        while i < len(line):
            a = line[i]
            if a in v:
                s.append(a)
                i += 2
            else:
                s.append(a)
            i += 1
            
        print("".join(s))

if __name__ == '__main__':
    main()
