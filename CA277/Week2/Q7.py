dict_graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'D': ['G', 'H'],
    'G': ['I', 'J'],
    'H': ['K']
}


def func_dict_graph(dic, a, b):
    if dic.get(b) is None:
        return False
    return a in dic.get(b)


print(func_dict_graph(dict_graph, 'B', 'A'))
print(func_dict_graph(dict_graph, 'B', 'D'))
print(func_dict_graph(dict_graph, 'K', 'A'))

