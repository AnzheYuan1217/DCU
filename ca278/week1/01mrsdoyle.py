#!/usr/bin/env python3

b = "Will you have a cup of tea, Father?"
a = input().upper()
while a != "YES":
    b += "Ah go on?"
    a = input().upper()
b += "Here you are."

print(b)
