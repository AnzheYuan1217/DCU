def q1_sum(a):
    s = 0
    for i in a:
        for j in i:
            if j % 2 == 0:
                s += j
    return s


num = (q1_sum([
    [1, 0, 2],
    [5, 5, 7],
    [9, 4, 3]
]))

print(num)
