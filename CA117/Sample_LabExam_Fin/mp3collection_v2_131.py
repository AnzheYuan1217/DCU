#!/usr/bin/env python3

class MP3Track(object):
    def __init__(self, title, duration, artists=[]):
        self.title = title
        self.duration = duration
        self.artists = artists

    def __str__(self):
        return 'Title: {}\nBy: {}\nDuration: {}'.format(
            self.title, ", ".join(self.artists), self.duration)


class MP3Collection(object):
    def __init__(self, collection=[]):
        self.collection = collection

    def add(self, s):
        self.collection.append(s)
        return

    def lookup(self, s):
        for i in self.collection:
            if s == i.title:
                return i
        return None

    def get_mp3s_by_artist(self, s):
        a = []
        for i in self.collection:
            if s in i.artists:
                a.append(i)
        return a

    def remove(self, s):
        for i in self.collection:
            if s == i.title:
                self.collection.remove(i)
                return

    def __str__(self):
        return 'Title: {}\nDuration: {}'.format(self.title, self.duration)
