#!/usr/bin/env python3

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        return

    def distance(self, p2):
        x1 = self.x
        y1 = self.y
        x2 = p2.x
        y2 = p2.y
        d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        return d

    def __str__(self):
        return '({:.1f}, {:.1f})'.format(self.x, self.y)
