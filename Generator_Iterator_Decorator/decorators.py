# Clousers
# def outer_function():
# 	message = 'Hi'

# 	def inner_function():
# 		print(message)
# 	return inner_function

# my_func = outer_function()
# my_func()
# my_func()
# my_func()

# def outer_function(msg):

# 	def inner_function():
# 		print(msg)
# 	return inner_function

# hi_func = outer_function('Hi')
# bye_func = outer_function('Bye')
# hi_func()
# bye_func()

# Decorators
# def decorator_function(original_function):
# 	def wrapper_function():
# 		print('wrapper executed this before {}'.format(original_function.__name__))
# 		return original_function() 
# 	return wrapper_function 

# def display():
# 	print("display function ran")

# decorated_display = decorator_function(display)
# decorated_display()


# def decorator_function(original_function):
# 	def wrapper_function(*args, **kwargs):
# 		print('wrapper executed this before {}'.format(original_function.__name__))
# 		return original_function(*args, **kwargs) 
# 	return wrapper_function 

# class Decorator_class(object):
# 	def __init__(self, original_function):
# 		self.original_function = original_function

# 	def __call__(self, *args, **kwargs):
# 		print("Call method executed this before {}".format(self.original_function.__name__))
# 		return self.original_function(*args, **kwargs)


# @decorator_function
# def display():
# 	print("display function ran")

# @Decorator_class
# def dispaly_info(name, age):
# 	print('display_info ran with arguments ({}, {})'.format(name, age))

# dispaly_info('John', 25)

def decorator_func(original_func):
	def wrapper(a, b):
		try:
			return a // b 
		except ZeroDivisionError:
			return "No should be positive"
	return wrapper


@decorator_func
def divide(a, b):
	return a // b 


print(divide(10, 0))