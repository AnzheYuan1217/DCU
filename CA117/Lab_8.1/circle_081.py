#!/usr/bin/env python3

from tkinter import CENTER


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

class Circle(object):

    def __init__(self, centre=False, radius=1):
        self.radius = radius
        if centre:
            self.centre = centre
        else:
            self.centre = Point(0, 0)


    def __str__(self):
        return 'Centre: {}\nRadius: {}'.format(self.centre, self.radius)
