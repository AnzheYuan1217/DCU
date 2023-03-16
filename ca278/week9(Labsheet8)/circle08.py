#!/usr/bin/env python3

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.radius ** 2 * math.pi

    def get_circumference(self):
        return self.radius * 2 * math.pi

    def __str__(self):
        return f'circle with radius {self.radius}'

    def __eq__(self, other):
        return 'yes' if self.radius == other.radius else 'no'


print('Enter the radius of the first circle:')
r = float(input())
a = Circle(r)
print('Enter the radius of the second circle:')
r = float(input())
b = Circle(r)

print(a)
print(b)
print('Are they equal?')
print(a == b)
