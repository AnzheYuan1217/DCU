#!/usr/bin/env python3

class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def __lt__(self, other):
        return (self.goals, self.points) < (other.goals, other.points)

    def __le__(self, other):
        return (self.goals, self.points) <= (other.goals, other.points)
    """
    def __gt__(self, other):
        return (self.goals, self.points) > (other.goals, other.points)

    def __ge__(self, other):
        return (self.goals, self.points) >= (other.goals, other.points)
    """
    def __ne__(self, other):
        return (self.goals, self.points) != (other.goals, other.points)

    def __eq__(self, other):
        a = self.goals * 3 + self.points
        b = other.goals * 3 + other.points
        return a == b

    def __str__(self):
        return '{} goal(s) and {} point(s)'.format(
            self.goals, self.points)

