# Program to demonstrate that a function can be 
# defined inside another function and a function 
# can be passed as parameter.

# Adds a welcome message to the string
# def messageWithWelcome(str):

# 	# Nested function
# 	def addWelcome():
# 		return "Welcome to "

# 	# Return concatenation of addWelcome()
# 	# and str.
# 	return addWelcome() + str

# # To get site name to which welcome is added
# def site(site_name):
# 	return site_name

# print(messageWithWelcome(site("GeeksforGeeks")))

# Adds a welcome message to the string
# returned by fun(). Takes fun() as parameter
# and returns welcome().

# def decorate_message(fun):

# 	def addWelcome(site_name):
# 		return "Welcome to " + fun(site_name)

# 	return addWelcome

# # @decorate_message
# def site(site_name):
# 	return site_name

# print(site("GeeksforGeeks"))

# A Python example to demonstrate that decorators
# can be useful attach data

# A decorator function to attach data to func
# def attach_data(func):
# 	func.data = 3
# 	return func

# @attach_data
# def add(x, y):
# 	return x + y

# # Driver code
# # This call is equivalent to attach_data()
# # with add() as parameter
# print(add(2, 3))
# print(add.data)

# functions can be treated as objects
# def shout(text):
# 	return text.upper()

# print(shout('Hello'))

# yell = shout

# print(yell('Hello'))

# Passing the function as argument
# def shout(text):
# 	return text.upper()

# def whisper(text):
# 	return text.lower()

# def greet(func):
# 	# storing the function in a variable
# 	greeting = func("""Hi, I am created by a function passed
# 					as an argument.""")
# 	print(greeting)

# greet(shout)
# greet(whisper)

# Returning functions from another function

# def create_adder(x):
# 	def adder(y):
# 		return x + y
# 	return adder

# add_15 = create_adder(16)
# print(add_15(10))

# defining a decorator
# def hello_decorator(func):
# 	def inner1():
# 		print("Hello, this is before function execution")

# 		func()

# 		print("This is after function execution")
# 	return inner1

# def function_to_be_used():
# 	print("This is inside function !!")

# function_to_be_used = hello_decorator(function_to_be_used)

# function_to_be_used()

# import time
# import math

# def calculate_time(func):
# 	def inner1(*args, **kwargs):
# 		begin = time.time()
# 		func(*args, **kwargs)

# 		end = time.time()
# 		print("Total time taken in : ", func.__name__, end - begin)

# 	return inner1

# @calculate_time
# def factorial(num):
# 	time.sleep(2)
# 	print(math.factorial(num))

# factorial(10)

# def hello_decorator(func):
# 	def inner1(*args, **kwargs):
# 		print("before Execution")

# 		# getting the returned value
# 		returned_value = func(*args, **kwargs)
# 		print("after Execution")

# 		# returning the value to the original frame
# 		return returned_value
# 	return inner1

# @hello_decorator
# def sum_two_numbers(a, b):
# 	print("Inside the function")
# 	return a + b

# a, b = 1, 2

# print("Sum =", sum_two_numbers(a, b))

# Code for testing decorator chaining
# def decor1(func):
# 	def inner():
# 		x = func()
# 		return x * x
# 	return inner

# def decor(func):
# 	def inner():
# 		x = func()
# 		return 2 * x
# 	return inner

# @decor1
# @decor
# def num():
# 	return 10

# print(num())

