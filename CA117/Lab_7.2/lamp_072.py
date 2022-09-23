#!/usr/bin/env python3

class Lamp(object):
    def __init__(self, on=False):
        self.on = on
        return

    def turn_on(self):
        self.on = True
        return

    def turn_off(self):
        self.on = False
        return

    def toggle(self):
        if self.on:
            self.on = False
        else:
            self.on = True
        return
