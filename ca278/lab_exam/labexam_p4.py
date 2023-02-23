#!/usr/bin/env python3

import sys


def get_year(id):
    return id[5:9]


file_id = sys.argv[1]
file_year = sys.argv[2]

with open(file_year) as f:
    target_year = f.readline().strip()  # use strip to remove the /n at the end

patients = []
with open(file_id) as f:
    for ids in f.readlines():
        if get_year(ids) == target_year:
            patients.append(ids.strip())  # use strip to remove the /n at the end

if patients:  # False when this lis is empty.
    print(patients)
else:
    print('There are no patients born that year.')
