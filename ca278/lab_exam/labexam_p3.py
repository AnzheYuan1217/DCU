#!/usr/bin/env python3

import sys

file_id = sys.argv[1]
file_year = sys.argv[2]

with open(file_year) as f:
    target_year = f.readline().strip()  # use strip to remove the /n at the end

patients = []
with open(file_id) as f:
    for ids in f.readlines():
        if ids[5:9] == target_year:
            patients.append(ids.strip())  # use strip to remove the /n at the end

if patients:  # False when this lis is empty.
    print(patients)
else:
    print('There are no patients born that year.')
