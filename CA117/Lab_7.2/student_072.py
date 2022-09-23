#!/usr/bin/env python3

class Student(object):
    def __init__(self, sid, name, modlist=False):
        self.sid = sid
        self.name = name
        if not modlist:
            self.modlist = []
        else:
            self.modlist = modlist
        return

    def add_module(self, mod):
        if mod not in self.modlist:
            self.modlist.append(mod)
        return

    def del_module(self, mod):
        if mod in self.modlist:
            self.modlist.remove(mod)
        return

    def __str__(self):

        return 'ID: {}\nName: {}\nModules: {}'.format(
            self.sid, self.name, ", ".join(self.modlist))
