#!/usr/bin/env python3

import time


def countdown(num):
    if num > 0:
        print(num)
        time.sleep(0.1)
    else:
        print('LIFT OFF!')
        return
    countdown(num - 1)


def search(the_str, letter):
    return letter in the_str


def previous_two(n):
    back_1 = n - 1
    back_2 = n - 2
    if n == 0 or n == 1:
        return n
    return previous_two(back_1) + previous_two(back_2)
