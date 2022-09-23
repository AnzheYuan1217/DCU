#!/usr/bin/env python3

s = input()
i = 0
while i < len(s) and s[i] != " ":
    i = i + 1
a = i
Day = s[:i]
i = i + 1

while i < len(s) and s[i] != " ":
    i = i + 1
b = i
Date = s[a + 1:i]
i = i + 1


while i < len(s) and s[i] != " ":
    i += 1
c = i
Month = s[b + 1:i - 1]
i = i + 1

while i < len(s) and s[i] != " ":
    i += 1
d = i
Year = s[c + 1:i]

print(Month, Date + ",", Year, "(" + Day + ")")
