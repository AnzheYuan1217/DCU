#!/usr/bin/env python3

class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def __lt__(self, other):
        return (self.goals, self.points) < (other.goals, other.points)

    def __le__(self, other):
        return (self.goals, self.points) <= (other.goals, other.points)

    def __ne__ (self, other):
        return (self.goals, self.points) != (other.goals, other.points)

    def __eq__(self, other):
        return (self.goals, self.points) == (other.goals, other.points)  # ???

    def __str__(self):
        return '{} goal(s) and {} point(s)'.format(self.goals, self.points)
    
    def __add__(self, other):
        new = Score()
        new.goals = (self.goals + other.goals)
        new.points = (self.points + other.points)
        return new
    
    def __iadd__(self, other):
        self.goals = self.goals + other.goals
        self.points = self.points + other.points
        return self
