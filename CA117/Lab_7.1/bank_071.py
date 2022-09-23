#!/usr/bin/env python3

class BankAccount():
    def set_attributes(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance
        return

    def print_attributes(self):
        print('Name: {}'.format(self.name))
        print('Account number: {}'.format(self.number))
        print('Balance: {:.2f}'.format(self.balance))
        return

    def deposit(self, add):
        self.balance += add
        return
