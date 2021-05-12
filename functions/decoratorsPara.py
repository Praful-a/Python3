# Program to illustrate Decorators basic in Python
# def decorator_fun(func):
# 	print("Inside decorator")

# 	def inner(*args, **kwargs):
# 		print("Inside inner function")
# 		print("Decorated the function")

# 		func()
# 	return inner

# @decorator_fun
# def func_to():
# 	print("Inside actual function")

# func_to()

# Program to illustrate decorators with parameters in Python

# def decorator_fun(func):
# 	print("Inside decorator")

# 	def inner(*args, **kwargs):
# 		print("Inside inner function")
# 		print("Decorated the function")

# 		func()
# 	return inner

# def func_to():
# 	print("Inside actual function")

# # another way of using decorators
# decorator_fun(func_to)()

# Porgram to illustrate decorators with parameters in Python

# def decorator(*args, **kwargs):
# 	print("Inside decorator")

# 	def inner(func):

# 		# code functionality here
# 		print("Inside inner function")
# 		print("I like", kwargs['like'])

# 		func()

# 	# reurning inner function
# 	return inner

# @decorator(like="geeksforgeeks")
# def my_func():
# 	print("Inside actual function")

# Program to illustrate decorators with parameters

# def decorator_func(x, y):
# 	def inner(func):
# 		def wrapper(*args, **kwargs):
# 			print("I like geeksforgeeks")
# 			print("Summation of values - {}".format(x+y))

# 			func(*args, **kwargs)
# 		return wrapper
# 	return inner

# # Not using decorator
# def my_fun(*args):
# 	for ele in args:
# 		print(ele)

# # another way of using decorators
# decorator_func(12, 15)(my_fun)("Geeks", "for", "Geeks")

# Program to illustrate decorators with parameters in Python (Multi-level Decorators)

def decorator(dataType, message1, message2):
	def decorator(fun):
		print(message1)
		def wrapper(*args, **kwargs):
			print(message2)
			if all([type(arg) == dataType for arg in args]):
				return fun(*args, **kwargs)
			return "Invalid Input"
		return wrapper
	return decorator

@decorator(str, "Decorator for 'stringJoin'", "stringJoin started ....")
def stringJoin(*args):
	st = ''
	for i in args:
		st += i
	return st

@decorator(int, "Decorator for 'summation'\n", "summation started ...")
def summation(*args):
	summ = 0
	for arg in args:
		summ += arg
	return summ

print(stringJoin("I ", 'like ', "Geeks", "for", "geeks"))
print()
print(summation(19, 2, 8, 533, 67, 981, 119))
