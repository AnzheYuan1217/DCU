#!/usr/bin/env python3

class Contact(object):
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def __str__(self):
        return '{} {} {}'.format(self.name, self.phone, self.email)

class ContactList(object):
    
    def __init__(self, d={}):
        self.d = d

    def add(self, item):
        self.d[item.name] = item
        return

    def get(self, item):
        if item in self.d:
            return self.d[item]
        else:
            return

    def remove(self, item):
        if item in self.d:
            self.d.pop(item)

    def __str__(self):
        a = []
        print("Contact list")
        print("------------")
        for v in (self.d).values():
            a.append((f'{v}'))
        a.sort()
        return ("\n".join(a))
