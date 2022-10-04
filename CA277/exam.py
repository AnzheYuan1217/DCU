# Q01
# (a):
# !usr/bin/env python3
mlt_dict = {
   "1111": ["John John", 45000],
   "1112": ["Rose Rose", 50000],
   "1113": ["Peter Peter", 55000]
}
idx = 1111  # idx should be int(input()), assuming it's 1111 here
for k, v in mlt_dict.items():
    if int(k) == idx:
        print(v[0])

# (b):
# !usr/bin/env python3

mlt_dict = {
   "1111": ["John John", 45000],
   "1112": ["Rose Rose", 50000],
   "1113": ["Peter Peter", 55000]
}

sum_all = 0
highest_salary = 0
name = ''

for k, v in mlt_dict.items():
    sum_all += v[1]
    if v[1] > highest_salary:
        highest_salary = v[1]
        name = v[0]

print(name)  # Print the name of the employee has the highest salary.
print(sum_all)  # Print the sum of all salaries.

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Q02
# (a)
sampleDict = {
    "a": "don't remember",
    "b": "don't remember",
    "c": "don't remember",
    "d": "don't remember",
    "location": "Dublin"}

sampleDict['city'] = sampleDict.pop('location')

# (b)
# Time complexity: O(1)

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Q03
# !usr/bin/env python3

list_m = (['1', '*', '9', 'm'])
output_list = []

for i in list_m:
    nested_list = []
    for j in range(len(list_m)):
        nested_list.append(i)
    output_list.append(nested_list)

print(output_list)

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Q04
# Timsort O(nlog(n))

# Heap’s algorithm O(n!)

# Binary trees O(log(n))

# Hash table O(1)

# Linear search O(n)
# Q05
# in

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Q06
# Tuples are immutable.

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Q07
# !usr/bin/env python3

dict1 = {'name': 'John', 'university': 'DCU', 'phone': None}
# 1. Drop the empty items
dict3 = {}
for k, v in dict1.items():
    if v:       # False if v == None
        dict3[k] = v

# 2. Concatenate the output
dict2 = {'birth': '1990', 'city': 'Dublin'}
dict3.update(dict2)

# 3. Calculate John's age!
age = 2022 - int(dict3.get('birth'))

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# Q08
# !usr/bin/env python3

s = "Hello!!!, Welcome to, ---Dublin City University---, Ireland."
a = ''

for i in s:
    if i.isalnum() or i.isspace():
        a += i
print(a)
