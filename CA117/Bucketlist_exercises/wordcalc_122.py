#!/usr/bin/env python3

import sys

def w_calc(s, var, r_var):
    num = int(var[s[0]])
    for i in range(len(s)):
        if s[i] == '+': 
            num = num + int(var[s[i + 1]])
        elif s[i] == '-':
            num = num - int(var[s[i + 1]])

    if str(num) in var.values():
        return r_var[str(num)]
    else:
        return 'unknown'

def main():
    dir = {}
    r_dir = {}
    for i in sys.stdin:
        try:
            i = i.strip().split(" ")
            if i[0] == "def":
                dir[i[1]] = i[2]
                r_dir[i[2]] = i[1]
            elif i[0] == "calc":
                print(f'{" ".join(i[1:])} {w_calc(i[1:], dir, r_dir)}')
            else:
                dir.clear()
                r_dir.clear()

        except KeyError:  # 优雅
            print(" ".join(i[1:]), "unknown")

if __name__ == '__main__':
    main()
