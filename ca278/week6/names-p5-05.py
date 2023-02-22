#!/usr/bin/env python3


class Person:
    def __init__(self, n, a):
        self.name = n
        self.age = a

    # Sets the values of the two attributes (self.name and self.age)
    def get_surname(self):
        return self.name.split(" ")[1]

    def get_firstname(self):
        return self.name.split(" ")[0]

    def __str__(self):
        return f'{self.get_surname()}, {self.get_firstname()} ({self.age})'


name = input('What is your name?')
age = int(input('How old are you?'))
people1 = Person(name, age)
print(f'Hello {people1.get_firstname()}')
print('Here are your details:')
print(people1)
