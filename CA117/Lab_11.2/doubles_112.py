#!/usr/bin/usr python3

import sys
v = ['a', 'e', 'i', 'o', 'u']

def task(s):
    count = 0
    for i in range(len(s) - 1):
        if s[i] in v and s[i - 1] == s[i] and s[i] != s[i + 1]:
            count += 1
    return count

def main():
    count = 0
    for i in sys.stdin:
        i = i.strip()
        n = task(i)
        if n > count:
            winner = i
            count = n

    print(winner)

if __name__ == '__main__':
    main()
