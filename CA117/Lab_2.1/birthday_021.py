#!/usr/bin/env python3

import sys, calendar

poem = ["Monday's child is fair of face.", "Tuesday's child is full of grace.", "Wednesday's child is full of woe.", "Thursday's child has far to go.", "Friday's child is loving and giving.", "Saturday's child works hard for a living.", "Sunday's child is fair and wise and good in every way."]

weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",]

def task(year, month, date):
    a = calendar.weekday(year, month, date)

    return "You were born on a " + weekday[a] + " and " + poem[a]
def main():
    for line in sys.stdin:
        i = line.strip().split()
        year = int(i[2])
        month = int(i[1])
        date = int(i[0])
        print(task(year, month, date))

if __name__ == '__main__':
    main()
