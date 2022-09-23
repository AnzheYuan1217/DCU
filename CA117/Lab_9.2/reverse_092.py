def reverse_list(s, i=1):
    if i == len(s) + 1:
        return s
    else:
        a = s[-i]
        s.pop(-i)
        s.append(a)

    return reverse_list(s, i + 1)
