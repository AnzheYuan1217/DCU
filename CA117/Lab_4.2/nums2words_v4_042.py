#!/usr/bin/env python3

import sys

def main():
    dir = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "10": "ten",
        "11": "eleven",
        "12": "twelve",
        "13": "thirteen",
        "14": "fourteen",
        "15": "fifteen",
        "16": "sixteen",
        "17": "seventeen",
        "18": "eighteen",
        "19": "nineteen",
        "20": "twenty",
        "30": "thirty",
        "40": "forty",
        "50": "fifty",
        "60": "sixty",
        "70": "seventy",
        "80": "eighty",
        "90": "ninety",
        "100": "one hundred"}
    
    for lines in sys.stdin:
        a = []
        line = lines.strip().split()

        for i in line:
            n = int(i)
            if n < 20 or n % 10 == 0:
                a.append(dir[i])
            else:
                a.append(dir[str(n // 10 * 10)] + "-" + dir[str(n % 10)])

        print(" ".join(a))
        # b = [dir[i] if (int(i) < 20 or int(i) % 10 == 0) else (dir[str(int(i) // 10 * 10)] + "-" + dir[str(int(i) % 10)]) for i in line]
        # print(" ".join(b))

if __name__ == '__main__':
    main()
