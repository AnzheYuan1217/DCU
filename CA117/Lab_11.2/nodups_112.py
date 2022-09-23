#!/usr/bin/usr python3

import sys, string

def main():
    seen = {}
    for i in sys.stdin:
        i = i.strip().split()
        for j in range(len(i)):
            word = i[j].lower().strip(string.punctuation)
            if word in seen:
                i[j] = "."
            else:
                seen[word] = True
        print(" ".join(i))

if __name__ == '__main__':
    main()
