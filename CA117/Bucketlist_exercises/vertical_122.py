#!/usr/bin/env python3

import sys

def lower_case(s):
    return s.lower()

def switch(line):
        a = len(line[0])
        lines = [[] for i in range(a)]

        for i in line:
            for j in range(a):
                lines[j].append(i[j])

        lines = ["".join(lines[i]) for i in range(a)]
        return lines

def main():
        lines = [i.strip() for i in sys.stdin]

        virtical = switch(lines)

        final = sorted(virtical, key=lower_case)

        for i in switch(final):
            print(i)

if __name__ == '__main__':
    main()
