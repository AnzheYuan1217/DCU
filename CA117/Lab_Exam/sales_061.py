#!/usr/bin/env python3

import sys

def tagger(item):
    return float(item[-1])

def main():
    dir = {}
    for i in sys.stdin:
        i = i.strip().split(":")
        name = i[0]
        sales = i[1].strip().split(",")

        sum = 0
        for n in sales:
            sum = sum + int(n)
        average = sum / len(sales)
        dir[name] = (f'{average:.2f}')
    
    for k, v in sorted(dir.items(), key=tagger, reverse=True):
        print(f'{k}: {v}')

if __name__ == '__main__':
    main()
