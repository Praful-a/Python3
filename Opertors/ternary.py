# Program to demonstrate conditional operator
# a, b = 10, 20

# # Copy value of a in min if a < b else copy b
# min  = a if a < b else b
# print(a)

# Python program to demosrate ternary operator
# a, b = 10, 20

# Use tuple for selecting an item
# (if_test_false, if_test_true)[test]
# print((b, a) [a < b])

# Use Dictionary for selcting an item
# print({True: a, False: b} [a < b])

# lambda is more efficient than above two methods
# because in lambda we are assure that only one
# expression will be evaluated unlike in tuple and
# Dictionary
# print((lambda: b, lambda: a) [a < b])

# Program to demonstrate nested ternary operator
# a, b = 20, 20
# print("Both a and b are equal" if a == b else "a is greater than b"
# 	if a > b else "b is greater than a")

# Above code can be written as
# a,b = 10, 20

# if a != b:
# 	if(a > b):
# 		print("a is greater than b")
# 	else:
# 		print("b is greater than a")
# else:
# 	print("Both a and b are equal")

# Program to demonstrate conditional operator
a, b = 10, 20

# If a is less than b, then a is assigned
# else b is assigned (Note: it doesn't work
# if a is 0)
min = a < b and a or b
print(min)