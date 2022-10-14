#!/usr/bin/env python3

dict1 = {1: 2,
         3: 4,
         4: 3,
         2: 1,
         0: 0
         }

# ascending
dict_a = {}
for i in sorted(dict1, key=dict1.get):
    dict_a[i] = dict1.get(i)
print(dict_a)

# descending
dict_b = {}
for i in sorted(dict1, key=dict1.get, reverse=True):
    dict_b[i] = dict1.get(i)
print(dict_b)
