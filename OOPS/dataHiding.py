# class MyClass:

# 	# Hidden member of MyClass
# 	__hiddenVariable = 0

# 	# A member method that changes
# 	# __hiddenVariable
# 	def add(self, increment):
# 		self.__hiddenVariable += increment
# 		print(self.__hiddenVariable)

# # Driver Code
# myObject = MyClass()
# myObject.add(2)
# myObject.add(5)
# print("\r")
# # This line causes error
# print(myObject.__hiddenVariable)

# Program to demonstrate that hidden member can be
# accessed outside a class
# class MyClass:

# 	# Hidden member of MyClass
# 	__hiddenVariable = 10

# # Driver code
# myObject = MyClass()
# print(myObject._MyClass__hiddenVariable)

# Printing Objects

# class Test:
# 	def __init__(self, a, b):
# 		self.a = a
# 		self.b = b

# 	def __repr__(self):
# 		return "Test a:%s b:%s" % (self.a, self.b)

# 	def __str__(self):
# 		return "From str method of Test: a is %s," \
#               " b is %s" % (self.a, self.b)

# # Driver Code
# t = Test(1234, 5648)
# print(t) # This calls __str__()
# print([t]) # This calls __repr__()

# If no __str__ method is defined, print t (or print str(t))
# uses __repr__

# class Test:
# 	def __init__(self, a, b):
# 		self.a = a
# 		self.b = b

# 	def __repr__(self):
# 		return "Test a:%s b:%s" % (self.a, self.b)

# # Driver Code
# t = Test(1234, 5678)
# # print(str(t)) # we can use this
# print(t) # either this

# If no __repr__ method is defined then the default
# is used.

class Test:
	def __init__(self, a, b):
		self.a = a
		self.b = b

# Driver Code
t = Test(1234, 5677)
print(t)