# Python program to show use of
# + operator for different purposes.

# print(1 + 2)
# concatenate two strings
# print("Geeks" + "For")

# Product two numbers
# print(3 * 4)

# Repeat the string
# print("Geeks"*4)

# Merge two lists
# l1 = [1, 2, 3]
# l2 = [3, 4, 5]
# print(l1 + l2)

# Program illustrate how to overload an binary + operator

# class A:
# 	def __init__(self, a):
# 		self.a = a

# 	# adding two objects
# 	def __add__(self, o):
# 		return self.a + o.a
# obj1 = A(1)
# obj2 = A(2)
# obj3 = A("Geeks")
# obj4 = A("For")

# print(obj1 + obj2)
# print(obj3 + obj4)

# Program to perform addition of two complex numbers using binary
# + operator overloading.

# class complex:
# 	def __init__(self, a, b):
# 		self.a = a
# 		self.b = b

# 	# adding two objects
# 	def __add__(self, other):
# 		return self.a + other.a, self.b + other.b

# 	def __str__(self):
# 		return self.a, self.b

# obj1 = complex(1, 2)
# obj2 = complex(2, 3)
# obj3 = obj1 + obj2
# print(obj3)

# Program to overload a comparison operators

# class A:
# 	def __init__(self, a):
# 		self.a = a

# 	def __gt__(self, other):
# 		if (self.a>other.a):
# 			return True
# 		else:
# 			return False
# ob1 = A(12)
# ob2 = A(3)
# if(ob1 > ob2):
# 	print("ob1 is greater than ob2")
# else:
# 	print('ob2 is greater than ob1')

# Program to overload equality and less than operators

class A:
	def __init__(self, a):
		self.a = a
	def __lt__(self, other):
		if(self.a<other.a):
			return "ob1 is lessthan ob2"
		else:
			return "ob2 is less than ob1"
	def __eq__(self, other):
		if(self.a == other.a):
			return "Both are equal"
		else:
			return "Not equal"
ob1 = A(2)
ob2 = A(3)
print(ob1 < ob2)

ob3 = A(4)
ob4 = A(4)
print(ob3 == ob4)