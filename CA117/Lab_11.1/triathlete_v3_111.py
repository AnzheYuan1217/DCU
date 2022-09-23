#!/usr/bin/env python3

class Triathlete(object):
    def __init__(self, name, tid, time=0, races={}):
        self.name = name
        self.tid = tid
        self.time = time
        self.races = races

    def add_time(self, race_name, race_time):
        self.races[race_name] = race_time
        self.time += race_time
        return
        
    def get_time(self, name):
        return self.races[name]

    def __eq__(self, other):
        return self.time == other

    def __lt__(self, other):
        return self.time < other

    def __gt__(self, other):
        return self.time > other

    def __str__(self):
        return 'Name: {}\nID: {}\nRace time: {}'.format(
            self.name, self.tid, self.time)
