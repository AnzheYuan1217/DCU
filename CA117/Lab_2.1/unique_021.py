#!/usr/bin/env python3

import sys, string

def main():
    a = []
    for line in sys.stdin:
        for i in line.lower().strip().split():

            i = i.strip(string.punctuation)  # strip these characters means "--" will be an empty string
            if i and i not in a:             # False when i is empty
                a.append(i)

    print(len(a))

if __name__ == '__main__':
    main()
