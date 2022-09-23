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

    def is_empty(self):
        return len(self.l) == 0

    def __len__(self):
        return len(self.l)

def matcher(s):
    a = Stack()
    d = {"(" : ")", "[" : "]", "{" : "}"}

    for i in s:
        if i in d.keys():
            a.push(i)

        elif not a.is_empty():
            if d[a.top()] == i:
                a.pop()

        else:
            return False

    return a.is_empty()
