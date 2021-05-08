# Program to demonstrate need of packing and unpacking

# A sample function that takes 4 arguments
# and prints them.
# def fun(a, b, c, d):
# 	print(a, b, c, d)

# # Driver code
# my_list = [1, 2, 3, 4]

# # This doesn't work
# fun(*my_list)

# Error when len(args) != no of actual arguments
# required by the function

# args = [0, 1, 4, 9]
# # this is gonna give error to fix make another varibale d
# def func(a, b, c, d):

# 	return a + b + c + d

# # calling function with unpacking args
# func(*args)

# Program to demonstrate use of packing

# This function uses packing to sum unknown number
# of arguments
# def mySum(*args):
# 	return sum(args)

# print(mySum(1, 2, 3, 4, 5))
# print(mySum(10, 20))

# Packing and unpacking
# def fun1(a, b, c):
# 	print(a, b, c)

# def fun2(*args):
# 	args = list(args)

# 	args[0] = 'GeeksforGeeks'
# 	args[1] = 'awesome'
# 	fun1(*args)

# fun2('Hello', 'beautiful', 'World!')

# dictionary items using **
# def fun(a, b, c):
# 	print(a, b, c)

# # a call with unpacking of dictionary
# d = {'a': 2, 'b': 4, 'c': 10}
# fun(**d)

# Program to demonstrate packing of dictionary items
# using **
def fun(**kwargs):

	# kwargs is a dict
	print(type(kwargs))

	# Printing dictionary items
	for key in kwargs:
		print("%s = %s" % (key, kwargs[key]))

# Driver code
fun(name = "geeks", Id = "101", language="Python")