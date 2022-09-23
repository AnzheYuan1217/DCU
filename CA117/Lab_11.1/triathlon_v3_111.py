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


class Triathlon(object):
    def __init__(self):
        self.lists = {}
        self.set = {}
        self.names = {}

    def add(self, key):
        self.set[key.name] = key.time
        self.lists[key.name] = key.tid
        self.names[key.tid] = key.name
        return

    def best(self):
        time = min(self.set.values())
        for i in self.set:
            if self.set[i] == time:
                id = self.lists[i]
                name = i

        return 'Name: {}\nID: {}\nRace time: {}'.format(name, id, time)

    def worst(self):
        time = max(self.set.values())
        for i in self.set:
            if self.set[i] == time:
                id = self.lists[i]
                name = i

        return 'Name: {}\nID: {}\nRace time: {}'.format(name, id, time)

    def __str__(self):
        a = sorted(self.lists.items())
        b = []
        # c = [(f'Name: {i[0]}\nID: {i[1]}') for i in a]

        for i in a:
            b.append(f'Name: {i[0]}\nID: {i[1]}')
        result = "\n".join(b)
        # result = "\n".join(c)
        return result
