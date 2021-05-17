# Creating a Dictionary with Integer Keys
# Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# print("\nDictionary with the use of Integer Keys: ")
# print(Dict)

# # Creating a Dictionary with Mixed Keys
# Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
# print("\nDictionary with the use of Mixed Keys: ")
# print(Dict)

# Creating an empty Dictionary
# Dict = {}
# print("Empty Dictionary: ")
# print(Dict)

# # Creating a Dictionary with dict() method
# Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
# print("\nDictionary with the use of dict(): ")
# print(Dict)

# # Creating a Dictionary with each item as a Pair
# # with each item as a Pair
# Dict = dict([(1, 'Geeks'), (2, 'For')])
# print("\nDictionary with each item as a pair: ")
# print(Dict)

# Creating a Nested Dictionary as shown in the below 
# image
# Dict = {1: 'Geeks', 2: 'For', 
# 		3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
# print(Dict)
# print(Dict[3]['A']) # Accessing A 


# Creating an empty Dictionary
# Dict = {}
# print("Empty Dictionary")
# print(Dict)

# # Adding elements one at a time
# Dict[0] = 'Geeks'
# Dict[2] = 'For'
# Dict[3] = 1
# print("\nDictionary after adding 3 elements: ")
# print(Dict)

# # Adding set a values to a single key
# Dict['Value_set'] = 2, 3, 4
# print("\nDictionary after adding 3 elements: ")
# print(Dict)

# # Updating existing key's value
# Dict[2] = 'Welcome'
# print("\nUpdated key value: ")
# print(Dict)

# # Adding Nested key value to Dictionary
# Dict[5] = {"Nested": {'1': 'Life', '2': 'Geeks'}}
# print("\nAdding a Nested Key: ")
# print(Dict)

# Dict[3] = 2+1
# print(Dict)

# Program to demonstrate accessing a element from a Dictionary

# Creating a Dictionary
# Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# # accessing a element using key
# print("Accessing a element using key: ")
# print(Dict['name'])

# # accessing a element using key
# print("Accessing a element using key: ")
# print(Dict[1])


# Creating a Dictionary
# Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# # accessing a element using get() method
# print("Accessing a element using get: ")
# print(Dict.get(3))

# Creating a Dictionary
# Dict = {'Dict1': {1: 'Geeks'},
# 		'Dict2': {"Name": 'For'}}

# # Accessing element using key
# print(Dict['Dict1'])
# print(Dict['Dict1'][1])
# print(Dict['Dict2'])
# print(Dict['Dict2']['Name'])

# Initial Dictionary
# Dict = {5: 'Welcome', 6: 'To', 7: 'Geeks'
# 		,'A': {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'},
# 		'B' : {1: 'Geeks', 2: 'Life'}}

# print("Initial Dictionary: ")
# print(Dict)

# # Deleting a key value
# del Dict[6]
# print("\nDeleting a specific key: ")
# print(Dict)

# # Deleting a key from Nested Dictionary
# del Dict['A'][2]
# print("\nDeleting a key from Nested Dictionary: ")
# print(Dict)

# Creating a Dictionary
# Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# # Deleting a key using pop() method
# pop_ele = Dict.pop(1)
# print("\nDictionary after deletion: " + str(Dict))
# print("Value associated to popped key is: " + str(pop_ele))

# Creating Dictionary
# Dict = {1: 'Geeks', 'name': 'for', 3: 'Geeks'}

# # Deleting an arbitary key using popitem() function
# pop_ele = Dict.popitem()
# print("\nDictionary after deletion: " + str(Dict))
# print("The arbitary pair returned is: " + str(pop_ele))


# Crating a Dictionary
Dict = {1: "Hello", 2: 'World'}

# Deleting entire Dictionary
Dict.clear()
print("\nDeleting Entire Dictionary: ")
print(Dict)