#!/usr/bin/usr python3

import sys

def main():
    for i in sys.stdin:
        i = i.strip().split()
        sum = 0
        discount = 0
        for j in i:
            sum += int(j)
        if len(i) >= 3:
            frees = len(i) // 3
            for n in range(frees):
                discount += int(min(i))
                i.remove(min(i))
            sum-= discount
        print(sum)

if __name__ == '__main__':
    main()
