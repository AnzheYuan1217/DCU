def string_dict(lis):
    dict1 = {}
    for i in lis:
        a = i.split('=')
        dict1[a[0]] = a[1]
    return dict1


print(string_dict(['1=one', '2=two', '3=three', '4=four']))
