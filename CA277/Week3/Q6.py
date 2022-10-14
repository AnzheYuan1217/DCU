def filter_star(a, b):
    for i, j in a.items():
        if len(j) == b:
            return {i: j}
    return 'No result found!'


c = filter_star({
  'Luxury Chocolates': '*   ****',
  'Tasty Chocolates': '****',
  'Big Chocolates': '*****',
  'Generic Chocolates': '***'
}, 4)  # {'Tasty Chocolates': '****'}
print(c)

d = filter_star({
  'Luxury Chocolates': '*****',
  'Tasty Chocolates': '****',
  'Big Chocolates': '*****',
  'Generic Chocolates': '***'
}, 2)  # No result found!
print(d)
