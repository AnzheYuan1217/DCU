#!/usr/bin/env python3

input_string = "PredictionE"
vowel = ["a", "e", "i", "o", "u"]
n = 0
for i in input_string:
    if i.lower() in vowel:
        n += 1
print(n)
