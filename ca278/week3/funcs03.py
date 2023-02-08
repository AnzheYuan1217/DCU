#!/usr/bin/env/ python3

import time


def get_price(age):
    if age <= 16:
        return 5
    elif age > 60:
        return 7
    else:
        return 10


def weird_case(some_str):
    '''    up = True
    weird_str = ""
    for i in some_str:
        if i.isalpha() and up:
            weird_str += i.upper()
            up = False
        elif i.isalpha():
            weird_str += i.lower()
            up = True
        else:
            weird_str += i
    '''

    j = 0
    aa = ""
    for i in some_str:
        if i.isalpha():
            if j % 2 == 0:
                aa += i.upper()
            else:
                aa += i.lower()
            j += 1
        else:
            aa += i

    return aa


def every_second(l1, l2):
    l3 = []
    for i in range(1, len(l1), 2):
        l3.append(l1[i])
    for i in range(1, len(l2), 2):
        l3.append(l2[i])
    return l3


def is_neg(num):
    return num < 0


def remove_neg(lst):
    i = 0
    while i < len(lst):
        if is_neg(lst[i]):
            lst.pop(i)
            i -= 1
        i += 1
    return


def countdown(num):
    for i in range(num, 0, -1):
        print(i)
        time.sleep(0.1)
    print("LIFT OFF!")
    return


def search(st, letter):
    for i in st:
        if letter == i:
            return True
    return False


def index(s, letter):
    return s.index(letter) if letter in s else -1


def previous_two(n):
    now = 1
    pre = 0
    seq = 0
    for i in range(n):
        seq = now + pre
        now = pre
        pre = seq
    return seq


"""
def previous_two(n):
    back_1 = n - 1
    back_2 = n - 2
    if n == 0 or n == 1:
        return n
    return previous_two(back_1) + previous_two(back_2)
"""
