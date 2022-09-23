#!/usr/bin/env python3

import sys

def binsearch(s, sorted_list):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] < s:
            low = mid + 1  # Search RHS
        elif sorted_list[mid] > s:
            high = mid - 1  # Search LHS
        else:
            return True  # Found it
    return False  # Not found

def main():
    i = [n.strip() for n in sys.stdin]
    j = [n.lower() for n in i]
    a = [n for n in i if len(n) >= 5 and binsearch((n.lower())[::-1], j)]

    print(a)
if __name__ == '__main__':
    main()
 