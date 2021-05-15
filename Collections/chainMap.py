from collections import ChainMap

# d1 = {'a': 1, 'b': 2}
# d2 = {'c': 3, 'd': 4}
# d3 = {'e': 5, 'f': 6}

# c = ChainMap(d1, d2, d3)
# print(c)

# Python code to demonstrate ChainMap and keys(), 
# values() and maps

# dic1 = {'a': 1, 'b': 2}
# dic2 = {'b': 3, 'c': 4}

# chain = ChainMap(dic1, dic2)

# # printing chainMap using maps
# print("All the ChainMap contents are :")
# print(chain.maps)

# # Printing keys using keys()
# print("All keys of ChainMap are :")
# print(list(chain.keys()))

# # Printing keys using keys()
# print("All values of ChainMap are :")
# print(list(chain.values()))


dic1 = {'a' : 1, 'b' : 2}
dic2 = {'b' : 3, 'c' : 4}
dic3 = {'f' : 5}

chain = ChainMap(dic1, dic2)

print("All the ChainMap contents are: ")
print(chain.maps)

# using new_child() to add new dictionary
chain1 = chain.new_child(dic3)

print('Displaying new ChainMap : ')
print(chain1.maps)

print("Value associated with b before reversing is : ", end="")
print(chain1['b'])

# reversing the ChainMap
chain1.maps = reversed(chain1.maps)

# displaying value associated with b after reversing
print("Value associated with b after reversing is : ", end="")
print(chain1['b'])