#!/usr/bin/env python3

class BankAccount(object):
    def __init__(self, balance=0):
        self.balance = balance
        return

    def deposit(self, add):
        self.balance = self.balance + add
        return

    def withdraw(self, subtracts):
        if self.balance >= subtracts:
            self.balance = self.balance - subtracts
        return

    def __str__(self):
        return 'Your current balance is {:.2f} euro'.format(self.balance)
