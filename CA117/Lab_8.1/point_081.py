#!/usr/bin/env python3

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def midpoint(self, other):
        new = Point()
        new.x = (self.x + other.x) / 2
        new.y = (self.y + other.y) / 2
        return new

    def __str__(self):
        return '({:.1f}, {:.1f})'.format(self.x, self.y)
