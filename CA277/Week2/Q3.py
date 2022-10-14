countries = {'Algeria': 37100000,
             'Canada': 34945200,
             'Uganda': 32939800,
             'Morocco': 32696600,
             'Sudan': 30894000,
             }

# Write a code to find which country has the largest population.
largest_population = max(countries.values())
for k, v in countries.items():
    if v == largest_population:
        print(k, 'has the largest population')

# Write a code to remove the country with the lowest population.
dict3 = {}
lowest_population = min(countries.values())
for k, v in countries.items():
    if v != lowest_population:
        dict3[k] = v
print(dict3)

# Write a code to sort the remaining countries based on their population.
dict4 = {}
for i in sorted(dict3, key=dict3.get):
    dict4[i] = dict3[i]
print(dict4)
