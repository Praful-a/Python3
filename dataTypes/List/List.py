# Program to demonstrate creation of list
# Creation of list

# Creating a list
# lst = []
# print("Blank list: ")
# print(lst)

# Creating number of list
# lst = [10, 2, 3]
# print("\nList of numbers: ")
# print(lst)

# Creating a List of strings and accessing using index
# lst = ["Geeks", "For", "Geeks"]
# print(lst[0])
# print(lst[1])

# Creating a Multi-Dimensional list 
# lst = [['Geeks', 'For'], ['Geeks']]
# print("\nMulti-Dimensional List: ")
# print(lst)

# Creating a list with the use of Numbers 
# (Having duplicate values)
# lst = [1, 2, 4, 4, 3, 3, 3, 6, 5]
# print("\nList with the use of Numbers: ")
# print(lst)

# # Creating a list with mixed type of values 
# # (Having numbers and strings)
# lst = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
# print('\nList with the use of Mixed Values: ')
# print(lst)

# lst = []
# print(len(lst))

# # Creating a list of numbers
# lst2 = [3, 10, 20]
# print(len(lst2))

# Program to demonstrate addition of elements in a list
# lst = []
# print("Initial blank list: ")
# print(lst)

# lst.append(1)
# lst.append(2)
# lst.append(4)
# print("\nList after Addition of Three elements: ")
# print(lst)

# # Adding elements to the lst
# # using iterator
# for i in range(4):
# 	lst.append(i)
# print("\nList after Addition of elements from 1-3")
# print(lst)

# # Adding Tuples to the list
# lst.append((5, 6))
# print('\nList after Addition of a Tuple:')
# print(lst)

# # Addition of list to a list
# lst2 = ['For', 'Geeks']
# lst.append(lst2)
# print("\nList after Addition of a List: ")
# print(lst)

# Addition of elements in a list at position

# lst = [1, 2, 3, 4]
# print("Initial List: ")
# print(lst)

# lst.insert(3, 12)
# lst.insert(0, 'Geeks')
# print('\nList after performing Insert Operation: ')
# print(lst)

# Addition of elements in a list using extend

# lst = [1, 2, 3, 4]
# print(lst)

# lst.extend([8, 'Geeks', 'Always'])
# print(lst)

# Accessing of element from list
# lst = ['Geeks', 'For', 'Geeks']

# print("Accessing a element from the list")
# print(lst[0])
# print(lst[2])

# lst = [[1, 2], ['Hello']]

# print("Accessing a element from a Multi-Dimensional list")
# print(lst[0][1])
# print(lst[1][0])

# lst = [1, 2, 'Python', 4, 'java', 6, 'London']

# print(lst[-1])
# print(lst[-3])

# Removal of elements in a list

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
# 		11, 12, 13]
# print("Intial List: ")
# print(lst)

# # Removing elements from list
# lst.remove(5)
# lst.remove(6)
# print(lst)

# for i in range(1, 5):
# 	lst.remove(i)
# print(lst)

# lst = [1, 2, 3, 4, 5]

# lst.pop()
# print('\nList after popping an element: ')
# print(lst)

# lst.pop(2)
# print("\nList after popping a specific location: ")
# print(lst)

# Creating a list
# lst = ['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G',
# 		'E', 'E', 'K', 'S']
# print("Intial List: ")
# print(lst)

# Sliced_list = lst[3:8]
# print(Sliced_list)

# Sliced_list = lst[5:]
# print(Sliced_list)

# Sliced_list = lst[:]
# print("\nPrinting all elements using slice operation: ")
# print(Sliced_list)

# Creating a list
# lst = ['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G',
		# 'E', 'E', 'K', 'S']

# Sliced_list = lst[:-6]
# print("\nElements sliced till 6th element from last: ")
# print(Sliced_list)

# Sliced_list = lst[-6:-1]
# print("\nElements sliced from index -6 to -1")
# print(Sliced_list)

# Sliced_list = lst[::-1]
# print("\nPrinting list in reverse: ")
# print(Sliced_list)

# List Comprehension
# odd_square = [x ** 2 for x in range(1, 11) if x % 2 != 0]
# print(odd_square)

# For understanding, above generation is same as,
odd_square = []

for x in range(1, 11):
	if x % 2 == 1:
		odd_square.append(x ** 2)
print(odd_square)