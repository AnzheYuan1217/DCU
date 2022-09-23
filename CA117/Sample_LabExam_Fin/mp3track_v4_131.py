#!/usr/bin/env python3

class MP3Track(object):
    def __init__(self, title, duration, artists=[]):
        self.title = title
        self.duration = duration
        self.artists = artists

    def add_artist(self, name):
        self.artists.append(name)

    def __str__(self):
        minutes = self.duration // 60
        seconds = self.duration % 60

        return 'Title: {}\nBy: {}\nDuration: {}:{:02d}'.format(
            self.title, ", ".join(self.artists), minutes, seconds)
