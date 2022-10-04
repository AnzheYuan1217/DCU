#!/usr/bin/env python3

lst = ["&&", "&", "&&&", "&&&&"]

item = lst[0]
result = True
for i in lst:
    if i != item:
        result = False
print(result)
