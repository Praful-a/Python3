# Program to demonstrate dictionary

# Dict = {1: "Geeks", 2: "For", 3: "Geeks"}
# print("Dictionary")
# print(Dict)
# print(Dict[1])

# defaultdict
from collections import defaultdict

# def def_value():
# 	return "Not Present"

# # Defining the dict
# d = defaultdict(def_value)
# d["a"] = 1
# d['b'] = 2

# print(d['a'])
# print(d['b'])
# print(d['c'])

# d = defaultdict(lambda: "Not Present")
# d['a'] = 1
# d['b'] = 2

# # Provides the default value for the key
# print(d.__missing__('a'))
# print(d.__missing__('d'))

# d = defaultdict(list)

# for i in range(5):
# 	d[i].append(i)

# print("Dictionary with values as list: ")
# print(d)


d = defaultdict(int)

L = [1, 2, 3, 4, 2, 4, 1, 2]

for i in L:
	d[i] += 1

print(d)