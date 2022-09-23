#!/usr/bin/env python3

class Point():
    def set_attributes(self, x, y):
        self.x = x
        self.y = y

        return


    def print_attributes(self):
        print('x: {:.2f}'.format(self.x))
        print('y: {:.2f}'.format(self.y))
        return

    def reflect(self):
        self.x = - self.x
        self.y = - self.y
        return
