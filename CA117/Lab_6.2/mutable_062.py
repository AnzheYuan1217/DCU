#!/usr/bin/env python3

def append2list(l1, l2=[]):
    list = []
    for i in l2:
        list.append(i)
    for i in l1:
        list.append(i)
    return list
