#!/usr/bin/env python3

class Element(object):

    def set_attributes(self, number, name, symbol, bp):
        self.number = number
        self.name = name
        self.symbol = symbol
        self.bp = bp

        return

    def print_attributes(self):
        # print('Number: {}\nName: {}\nSymbol: {}\nBoiling point: {} K'.format(self.number, self.name, self.symbol, self.bp))
        print('Number: {}'.format(self.number))
        print('Name: {}'.format(self.name))
        print('Symbol: {}'.format(self.symbol))
        print('Boiling point: {} K'.format(self.bp))

        return
