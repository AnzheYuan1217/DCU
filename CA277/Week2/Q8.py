def task(a):
    b = {'name': a['name'], 'max_scores': max(a.get('scores'))}
    return b


print(task({'name': 'John', 'scores': [55, 60, 40]}))
