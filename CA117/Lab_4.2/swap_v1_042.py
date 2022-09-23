#!/usr/bin/env python3

def swap_keys_values(d):
    dir = {}
    for k, v in d.items():
        dir[v] = k
    return dir
