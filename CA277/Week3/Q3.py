guests = {
    'Randy': 'Germany',
    'Karla': 'France',
    'Wendy': 'Japan',
    'Norman': 'England',
    'Sam': 'Argentina'
}


# Using f string
def greetings(name):
    if name in guests.keys():
        return f'Hi, I\'m {name} and I\'m from {guests[name]}'
    else:
        return f'Hi, I\'m {name}'

# Not using f string
def greetings_2(name):
    a = 'Hi, I\'m ' + name
    b = ' and I\'m from ' + guests[name]
    if name in guests:
        a += b
    return a


print(greetings('Sam'))
print(greetings_2('Sam'))
