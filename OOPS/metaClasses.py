# num = 23
# print("Type of num is: ", type(num))

# lst = [1, 2, 4]
# print("Type of lst is: ", type(lst))

# name = "Atul"
# print("Type of name is: ", type(name))

# class Student:
# 	pass

# stu_obj = Student()

# # Print type of object of Student class
# print("Type of stu_obj is:", type(stu_obj))


# class Student:
# 	pass

# # Print type of Student class
# print("Type of Student class is:", type(Student))

# class Test:
# 	pass

# # Defining method variables
# Test.x = 45

# # Defining class methods
# Test.foo = lambda self: print("Hello")

# # Creating object
# myobj = Test()

# print(myobj.x)
# myobj.foo()

# def test_method(self):
# 	print("This is Test class method!")

# # creating a base class
# class Base:
# 	def myfun(self):
# 		print("This is inherited method!")

# # Creating Test class dynamically using
# # type() method directly
# Test = type('Test', (Base, ), dict(x='atul', my_method=test_method))

# # Print type of Test
# print("Type of Test class: ", type(Test))

# # Creating instance of Test class
# test_obj = Test()
# print("Type of test_obj: ", type(test_obj))

# # calling inherited method
# test_obj.myfun()

# # calling Test class method
# test_obj.my_method()

# # printing variable
# print(test_obj.x)

# our metaclass
# class MultiBase(type):
# 	# overriding __new__ method
# 	def __new__(cls, clsname, bases, clsdict):
# 		# if no of base classes is greater than 1
# 		# raise error
# 		if len(bases) > 1:
# 			raise TypeError("Inherited multiple base classes!!!")

# 		# else executed __new__ method of super class, ie.
# 		# call __init__ of type class
# 		return super().__new__(cls, clsname, bases, clsdict)

# # metaclass can be specified by 'metaclass' keyword argument
# # now MultiBase class is used for creating classes
# # this will be propagated to all subclasses of Base
# class Base(metaclass=MultiBase):
# 	pass

# # no error is raised
# class A(Base):
# 	pass

# # no error is raised
# class B(Base):
# 	pass

# # This will raise an error!
# class C(A, B):
# 	pass

# from functools import wraps

# def debug(func):

# 	@wraps(func)
# 	def wrapper(*args, **kwargs):
# 		print("Full name of this method:", func.__qualname__)
# 		return func(*args, **kwargs)
# 	return wrapper

# def debugmethods(cls):
# 	'''class decorator make use of debug decorator
# 	to debug class methds'''

# 	# check in class dictionary for any callable(method)
# 	# if exist, replace it with debugged version
# 	for key, val in vars(cls).items():
# 		if callable(val):
# 			setattr(cls, key, debug(val))
# 	return cls

# # Sample class
# @debugmethods
# class Calc:
# 	def add(self, x, y):
# 		return x+y
# 	def mul(self, x, y):
# 		return x*y
# 	def div(self, x, y):
# 		return x/y

# mycal = Calc()
# print(mycal.add(2, 3))
# print(mycal.mul(5, 2))

from functools import wraps

def debug(func):

	@wraps(func)
	def wrapper(*args, **kwargs):
		print("Full name of this method:", func.__qualname__)
		return func(*args, **kwargs)
	return wrapper

def debugmethods(cls):

	for key, val in vars(cls).items():
		if callable(val):
			setattr(cls, key, debug(val))
	return cls

class debugMeta(type):

	def __new__(cls, clsname, bases, clsdict):
		obj = super().__new__(cls, clsname, bases, clsdict)
		obj = debugmethods(obj)
		return obj

class Base(metaclass=debugMeta):
	pass

class Calc(Base):
	def add(self, x, y):
		return x+y

class Calc_adv(Calc):
	def mul(self, x, y):
		return x*y

mycal = Calc_adv()
print(mycal.mul(2, 3))
print(mycal.add(2, 3))