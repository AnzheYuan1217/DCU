def swap_dict(n, s, t):
    dict1 = {}
    for i in range(len(n)):
        if t:
            dict1[s[i]] = n[i]
        else:
            dict1[n[i]] = s[i]

    return dict1


print(swap_dict([1, 2, 3], ['one', 'two', 'three'], False))
print(swap_dict([1, 2, 3], ['one', 'two', 'three'], True))
