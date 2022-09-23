#!/usr/bin/env python3

import sys

def sum(s):
    sum = 0
    for j in s:
        sum += int(j)
    return sum

def tagger(item):
   return item[1]

def val(s):
    for i in s:
        if not i.isdigit():
            return False
    return True

def main():
    valid = {}
    not_valid = []
    for i in sys.stdin:
        i = i.split()
        name = " ".join(i[:-3])
        scores = i[-3:]

        if val(scores):
            valid[name] = sum(scores)
        else :
            not_valid.append(name)

    for k, v in sorted(valid.items(), key = tagger):
        print(f'{k}: {v}')

    if not_valid != []:
        print(f'Disqualified: {", ".join(not_valid)}')

if __name__ == '__main__':
    main()

