# Python code to demonstrate working of enumerate()

# for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']):
# 	print(key, value)

# Python code to demonstrate working of zip()

# initializing list
# questions = ['name', 'colour', 'shape']
# answers = ['apple', 'red', 'a circle']

# # using zip() to combine two containers
# # and print values
# for question, answer in zip(questions, answers):
# 	print('What is your {0}? I am {1}.'.format(question, answer))

# Python code to demonstrate working of iteritems(), items

# d = {"geeks": "for", "only": "geeks"}

# # using iteritems to print the dictionary key-value pair
# print("The key value pair using iteritems is : ")
# for i,j in d.items():
# 	print(i, j)


# Use of sorted() function

# lis = [1, 3, 5, 6, 2, 1, 3]

# print("The list is sorted order is : ")
# for i in sorted(lis):
# 	print(i, end=" ")
# print('\r')

# using sorted() and set() to print the list in sorted order
# use of set() removes duplicates.
# print("The list in sorted order (without duplicates) is : ")
# for i in sorted(set(lis)):
# 	print(i, end=" ")

# Initialzing list
# basket = ['guava', 'orange', 'apple', 'pear', 'guava'
# 			'banan', 'grape']

# # using sorted() and set() to print the list in sorted order
# for fruit in sorted(set(basket)):
# 	print(fruit)

# Initializing list
# lis = [1, 3, 5, 6, 2, 1, 3]

# using reversed() to print the list in reversed order
# print("The list in reversed order is : ")
# for i in reversed(lis):
# 	print(i, end=" ")

# Program to demonstrate working of reversed()

# using reversed() to print in reverse order
for i in reversed(range(1, 10, 3)):
	print(i)