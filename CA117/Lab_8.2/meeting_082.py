#!/usr/bin/env python3

class Meeting(object):
    def __init__(self, hour, minute, duration):
        self.hour = hour
        self.minute = minute
        self.duration = duration
        return

    def __str__(self):
        return '{:02}:{:02} ({} minutes)'.format(self.hour, self.minute, self.duration)
