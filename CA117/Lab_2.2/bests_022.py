#!/usr/bin/env python3

import sys

def main():
    mark = 0
    names = []

    with open(sys.argv[1]) as f:
        contents = f.readlines()
    for line in contents:
        i = line.strip().split(" ")
        a = int(i[0])
        
        if mark < a:
            mark = a

    for line in contents:
        i = line.strip().split(" ", 1)
        if int(i[0]) == mark:
            names.append(i[1])
    
    name = ", " .join(names)
    print(f'Best student(s): {name}\nBest mark: {mark}')

if __name__ == '__main__':
    main()
