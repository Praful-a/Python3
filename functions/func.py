# Python function to check
# whether x is even or odd

# def evenOdd(x):
# 	"chacking odd even"  # docstring
# 	if (x % 2 == 0):
# 		return "even"
# 	else:
# 		return "odd"

# # Driver code to call the function
# print(evenOdd.__doc__) # print function docstring 
# print(evenOdd(2))
# print(evenOdd(3))

# def square_value(num):
# 	"""This function returns the square
# 	value of the entered number"""
# 	return num**2

# print(square_value(2))
# print(square_value(-4))

# Here x is a new reference to same list lst
# def myFun(x):
# 	x[0] = 20

# # Driver Code (Note that lst is modified)
# # after function call.
# lst = [10, 11, 12, 13, 14, 15]
# myFun(lst)
# print(lst)

# def myFun(x):

# 	# After below line link of x with previous
# 	# object gets broken. A new object is assigned to x.
# 	x = [20, 30, 40]

# # Driver Code (Note th lst is not modified)
# # after function call.
# lst = [10, 11, 12, 13, 14, 15]
# myFun(lst)
# print(lst)

# # Another example
# def myFun(x):
# 	x = 20

# x = 10
# myFun(x)
# print(x)

# def swap(x, y):
# 	temp = x
# 	x = y
# 	y = temp

# x = 2
# y = 3
# swap(x, y)
# print(x)
# print(y)

# Program to demonstrate default arguments

# all the parameters to right must have default
# otherwise it will give an error
# def myFun(x, y=50, c=10):
# 	print('x: ', x)
# 	print('y: ', y)
# 	print('c: ', c)

# myFun(10)

# Program to demonstrate keyword arguments
# def student(firstname, lastname):
	# print((firstname, lastname))

# Keyword arguments
# student(firstname = "Geeks", lastname="Pracitce")
# student(lastname = 'Pracitce', firstname="Geeks")

# Program to illustrate *args for variable number of
# arguments

# def myFun(*argv):
# 	for arg in argv:
# 		print(arg)

# myFun('Hello', 'Welcome', 'to', 'India')

# Program to illustrate *kwargs for variable number 
# of keyword arguments

# def func(**kwargs):
# 	for key, value in kwargs.items():
# 		print("%s == %s" % (key, value))

# func(first = "I", mid="love", last="Python")

# def cube(x) : return x*x*x

# cube_v2 = lambda x : x*x*x

# print(cube(7))
# print(cube_v2(87))

# We cab use empty functions in python 
def mul():
	pass

# If we run below code that will produce an error
# def mul():
