#!/usr/bin/env python3

class BankAccount:
    id_counter = 1
    def __init__(self, balance):
        self.balance = balance
        self.id = BankAccount.id_counter
        BankAccount.id_counter += 1

    def __str__(self):
        return f'Account number: {self.id}\nBalance: {self.balance}'


    def lodge(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


account1 = BankAccount(1000)
account2 = BankAccount(1500)
print(account1)
print(account2)

account2.withdraw(500)
account1.lodge(500)
print(account1)
print(account2)