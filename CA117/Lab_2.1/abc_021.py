#!/usr/bin/env python3

import sys

def main():
    line = sys.stdin.readlines()
    i = line[0].strip().split()
    for n in i:
        i[i.index(n)] = int(n)

    k = []
    i.sort()
    a, b, c = i[0], i[1], i[2]
    for i in line[1].strip():
        if i == "A":
            k.append(str(a))
        elif i == "B":
            k.append(str(b))
        else:
            k.append(str(c))

    print(" ".join(k))

if __name__ == '__main__':
    main()
