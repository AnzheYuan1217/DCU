#!/usr/bin/env python3

class Stack(object):
    def __init__(self):
        self.l = []

    def push(self, e):
        self.l.append(e)

    def pop(self):
        return self.l.pop()

    def top(self):
        return self.l[-1]
    
    def next_top(self):
        return self.l[-2]

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)
    

def calculator(line):
    a = Stack()
    from math import sqrt
    binops = {'+': int.__add__,
            '-': int.__sub__,
            '*': float.__mul__,
            '/': float.__truediv__}
    uniops = {'n': float.__neg__,
            'r': sqrt}

    for i in line.split(" "):
        if i in binops:
            num = binops[i](float(a.next_top()), float(a.top()))
            a.pop()
            a.pop()
            a.push(num)
        elif i in uniops:
            num = uniops[i](a.top())
            a.pop()
            a.push(num)
        else:
            a.push(float(i))

    return a.top()

