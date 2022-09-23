#!/usr/bin/env python3

class Meeting(object):
    def __init__(self, hour, minute, duration):
        self.hour = hour
        self.minute = minute
        self.duration = duration
        return

    def __str__(self):
        return '{:02}:{:02} ({} minutes)'.format(self.hour, self.minute, self.duration)

class Schedule(object):
    def __init__(self, schedule={}):
        self.schedule = schedule
        return

    def add(self, item):
        self.schedule[item] = True
        return

    def __str__(self):
        a = []
        print("Schedule")
        print("--------")
        for v in (self.schedule).keys():
            a.append((f'{v}'))
        a.sort()
        return '{}\nMeetings today: {}'.format(("\n".join(a)), len(a))
