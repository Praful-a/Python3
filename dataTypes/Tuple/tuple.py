# Creating an empty Tuple
# tuple1 = ()
# print("Initial empty Tuple: ")
# print(tuple1)

# # Creating a Tuple with the use of string
# tuple1 = ('Geeks', 'Learning Platform')
# print("\nTuple with the use of String: ")
# print(tuple1)

# # Creating a Tuple with the use of list
# lst = [1, 2, 4, 5, 6]
# print("\nTuple using List: ")
# print(tuple(lst))


# # Creating a Tuple with the use of built-in functions
# Tuple1 = tuple('Geeks')
# print("\nTuple with the use of function: ")
# print(Tuple1)

# Creating a Tuple with Mixed Datatype
# Tuple1 = (5, 'Welcome', 7, 'Geeks')
# print("\nTuple with Mixed Datatypes: ")
# print(Tuple1)

# # Creating a Tuple with nested tuples
# Tuple1 = (0, 1, 2, 3)
# Tuple2 = ('python', 'geek')
# Tuple3 = (Tuple1, Tuple2)
# print("\nTupele with nested tuples: ")
# print(Tuple3)

# # Creating a Tuple with repetition
# Tuple1 = ('Geeks', ) * 3
# print("\nTuple with repetition: ")
# print(Tuple1)

# # Creating a Tuple with the use of loop
# Tuple1 = ('Geeks')
# n = 5
# print("\nTuple with a loop")
# for i in range(int(n)):
# 	Tuple1 = (Tuple1, )
# 	print(Tuple1)

# Accessing Tuple with Indexing
# Tuple1 = tuple('Geeks')
# print("\nFirst element of Tuple: ")
# print(Tuple1[1])

# # Tuple unpacking
# Tuple1 = ('Geeks', 'For', 'Geeks')

# # This line unpack values of Tuple1
# a, b, c = Tuple1
# print("\nValues after unpacking: ")
# print(a)
# print(b)
# print(c)


# Concatenation of tuples
# Tuple1 = (0, 1, 2, 3)
# Tuple2 = ('Geeks', 'For', 'Geeks')

# Tuple3 = Tuple1 + Tuple2

# # Printing first Tuple
# print("Tuple 1: ")
# print(Tuple1)

# # Printing Second Tuple
# print("\nTuple2: ")
# print(Tuple2)

# # Printing Final Tuple
# print("\n Tuples after Concatenation: ")
# print(Tuple3)


# Slicing of a Tuple

# Slicing of a Tuple with Numbers
# Tuple1 = tuple('GEEKSFORGEEKS')

# # Removing First element
# print("Removal of First Element: ")
# print(Tuple1[1:])

# # Reversing the Tuple
# print("\nTuple after sequence of Element is reversed: ")
# print(Tuple1[::-1])

# # Printing elements of a Range
# print("\nPrinting elements between Range 4-9: ")
# print(Tuple1[4:9])

# Deleting a Tuple

# Tuple = (0, 1, 2, 3, 4)
# del Tuple

# print(Tuple)  # Error Tuple does not support deletion


# Tuple methods
tup = (1, 2, 3, 4, 5, 2)
print(tup.count(2))

print(tup.index(5))
