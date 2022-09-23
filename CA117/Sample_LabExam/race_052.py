#!/usr/bin/env python3

import sys

def best(s):
    times = []
    for i in s:
        i = i.split(":")
        if i[0].isdigit() and i[1].isdigit():
            i = float(".".join(i))
            times.append(i)
        else:
            return
    return min(times)

def main():
    race = {}
    for line in sys.stdin:
        line = line.strip().split()
        name = line[0]
        time = line[1:]
        if best(time):
            race[name] = best(time)

    a = min(race.values())
    for k in race.keys():
        if race[k] == a:
            print(f'{k} : {str(a).replace(".", ":")}')

if __name__ == '__main__':
    main()
