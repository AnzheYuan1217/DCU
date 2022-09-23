#!/usr/bin/env python3

def swap_unique_keys_values(d):
    dir = {}
    not_unique = {}
    seen = {}

    for v in d.values():
        if v in seen:
            not_unique[v] = True
        seen[v] = True

    for k, v in d.items():
        if v not in not_unique:
            dir[v] = k
    return dir
