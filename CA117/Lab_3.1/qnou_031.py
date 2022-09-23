#!/usr/bin/env python3

import sys

def qnou(s):
   s = s.replace("qu", "")
   return "q" in s

def main():
    i = [n.strip() for n in sys.stdin if qnou(n.lower())]

    print("Words with q but no u:", i)

if __name__ == '__main__':
    main()
