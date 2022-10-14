def move_vow(s):
    a = b = ''

    vowel = {'a', 'e', 'i', 'o', 'u'}
    for i in s:
        if i.lower() in vowel:
            a += i
        else:
            b += i
    return a + b


print(move_vow('This is DCU!'))
