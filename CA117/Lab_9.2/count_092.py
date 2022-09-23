def count_letters(s):
    s = list(s)
    if s == []:
        return 0
    elif s[0] == '':
        return 1
    else:
        sum = 1
        s.pop()

    return sum + count_letters("".join(s))
