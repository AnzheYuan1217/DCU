def minimum(s):

    if len(s) == 1:
        return s[0]
    elif s[0] > s[1]:
        s.pop(0)
    else:
        s.pop(1)

    return minimum(s)
