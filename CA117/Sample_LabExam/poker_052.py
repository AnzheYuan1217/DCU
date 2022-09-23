#!/usr/bin/env python3

import sys

def strength(s):
    rank = list("A23456789TJQK")
    pos = 0
    for i in s:
        a = rank.index(i[0])
        if a > pos:
            pos = a
    return rank[pos]

def main():
    for lines in sys.stdin:
        line = lines.strip().split()
        count = 0
        for i in line:
            if i[0] == strength(line):
                count += 1
        print(count)
"""
def main():
    ranks = 'A23456789TJQK'
    hands = sys.stdin.readline().strip().split()
    d_ranks = {r: 0 for r in ranks}
    for h in hands:
        d_ranks[h[0]] += 1
    print(max(d_ranks.values()))
"""
if __name__ == '__main__':
    main()
