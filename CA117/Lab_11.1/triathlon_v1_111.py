#!/usr/bin/env python3

class Triathlete(object):
    def __init__(self, name, tid):
        self.name = name
        self.tid = tid

    def __str__(self):
        return 'Name: {}\nID: {}'.format(self.name, self.tid)

class Triathlon(object):
    def __init__(self):
        self.lists = []

    def add(self, key):
        self.lists.append(key)
        return

    def remove(self, obj):
        for i in self.lists:
            if obj == i.tid:
                self.lists.remove(i)
        return

    def lookup(self, obj):
        for i in self.lists:
            if obj == i.tid:
                return i

    def __str__(self):
        return '{}'.format(self.lists)
