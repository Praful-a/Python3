# Program to illustrate while loop
# count = 0
# while(count < 3):
# 	count = count + 1
# 	print("Hello Geek")

# Program to illustrate combining else with while
# count = 0
# while (count < 3):
# 	count = count + 1
# 	print("Hello Geek")
# else:
# 	print("In Else Block")

# Program to illustrate Single statement while block
# count = 0
# while(count == 0): print("hello Geek")

# Python program to illustrate Iterating over range
# 0 10 n-1

# n = 4
# for i in range(0, n):
# 	print(i)

# Program to illustrate Iterating over a list
# print("List Iteration")
# l = ["geeks", 'for', 'geeks']
# for i in l:
# 	print(i)

# Iterating over a tuple (immutable)
# print("\nTuple Iteration")
# t = ("geeks", "for", "geeks")
# for i in t:
# 	print(i)

# Iterating over String
# print("String Iterations")
# s = "I Love Python"
# for i in s:
# 	print(i)

# Iterating over dictionary
# print("Dictionary Iteration")
# d = dict()
# d['xyz'] = 123
# d['abc'] = 345
# for i in d:
# 	print("%s %d" %(i, d[i]))

# Iterating by index
# l = [1, 2, 3, 4, 5]
# for i in range(len(l)):
# 	print(l[i])

# Combining else with for

# lst = ["I", "Love", "Python"]
# for index in range(len(lst)):
# 	print(lst[index])
# else:
# 	print("Inside Else Block")

# Nested Loop
# for i in range(1, 5):
# 	for j in range(i):
# 		print(i, end=" ")
# 	print()

# Prints all letters excpet 'e' and 's'
# for letter in 'geeksforgeeks':
# 	if letter == 'e' or letter == 's':
# 		continue
# 	print("Current Letter : ", letter)
	# var = 10

# for letter in 'geeksforgeeks':

# 	# break the loop as soon it sees 'e' 
# 	# of 's'
# 	if letter == 'e' or letter == 's':
# 		break
# print('Current Letter :', letter)

# Create an empty loop by using pass
# for letter in 'geeksforgeeks':
# 	pass
# print("Last letter: ", letter)

# fruits = ["apple", "orange", "kiwi"]

# # Creating an iterator object
# # from that iterable i.e fruits
# iter_obj = iter(fruits)

# # Infinite while loop
# while True:
# 	try:
# 		# getting the next item
# 		fruit = next(iter_obj)
# 		print(fruit)
# 	except StopIteration:

# 		# If StopIteration is raised,
# 		# break from loop
# 		break

# Print a list in reverse order

l = [1, 2, 3, 4, 5]
for i in range(len(l), 0, -1):
	print(i)

# l = [1, 2, 3, 4, 5]
# n = len(l)-1
# while(n >= 0):
# 	print(l[n])
# 	n -= 1