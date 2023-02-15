#!/usr/bin/env python3

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.radius ** 2 * math.pi

    def get_circumference(self):
        return self.radius * 2 * math.pi
