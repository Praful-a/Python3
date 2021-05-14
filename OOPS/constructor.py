# Example of default constructor

# class Cons:

# 	# default constructor
# 	def __init__(self):
# 		self.geek = "GeekforGeeks"


# 	# a method for printing data members
# 	def print_Geek(self):
# 		print(self.geek)

# # creating object of the class
# obj = Cons()

# # calling the instance method using the object obj
# obj.print_Geek()

# Example of parameterized constructor

# class Addition:
# 	first = 0
# 	second = 0
# 	answer = 0

# 	# parameterized constructor
# 	def __init__(self, f, s):
# 		self.first = f
# 		self.second = s

# 	def display(self):
# 		print("First number = " + str(self.first))
# 		print("Second number = " + str(self.second))
# 		print("Addition of two number = " + str(self.answer))

# 	def calculate(self):
# 		self.answer = self.first + self.second

# # creating object of the class
# # this will invoke parameterized constructor
# obj = Addition(1000, 2000)

# # perform Addition
# obj.calculate()

# # display result
# obj.display()

# Python program to illustrate destructor
# class Employee:

# 	# Initializing 
# 	def __init__(self):
# 		print("Employee created.")

# 	# Deleting (Calling destructor)
# 	def __del__(self):
# 		print("Destructor called, Employee deleted.")

# obj = Employee()
# del obj

# class Employee:

# 	# Initializing
# 	def __init__(self):
# 		print("Employee created")

# 	# Calling destructor
# 	def __del__(self):
# 		print("Destructor called")

# def Create_obj():
# 	print("Making Object...")
# 	obj = Employee()
# 	print("function end...")
# 	return obj

# print("Calling Create_obj() function...")
# obj = Create_obj()
# print("Program End...")

class A:
	def __init__(self, bb):
		self.b = bb

class B:
	def __init__(self):
		self.a = A(self)
	def __del__(self):
		print("die")

def fun():
	b = B()

fun()