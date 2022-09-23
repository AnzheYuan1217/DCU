#!/usr/bin/env python3

class Triathlete(object):
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        return 'Name: {}\nID: {}'.format(self.name, self.tid)

class Triathlon(object):
    def __init__(self):
        self.lists = {}

    def add(self, key):
        self.lists[key.name] = key.tid
        return

    def __str__(self):
        a = sorted(self.lists.items())
        b = []
        # c = [(f'Name: {i[0]}\nID: {i[1]}') for i in a]

        for i in a:
            b.append(f'Name: {i[0]}\nID: {i[1]}')
        result = "\n".join(b)
        # result = "\n".join(c)
        return result
