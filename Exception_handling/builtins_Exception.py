# a = locals()['__builtins__']
# print(a)

# try:
# 	a = 10/0
# 	print(a)
# except ArithmeticError:
# 	print("This statement is raising an arithmetic exception")
# else:
# 	print("Success.")

# try:
# 	a = [1, 2, 3]
# 	print(a[3])
# except LookupError:
# 	print("Index out of bound error.")
# else:
# 	print("Success.")

# EOFError

# while True:
# 	data = input("Enter name : ")
# 	print('Hello ', data)


# import math
# print(math.exp(1000))

# def my_generator():
# 	try:
# 		for i in range(5):
# 			print("Yielding", i)
# 			yield i
# 	except GeneratorExit:
# 		print("Exiting early")

# g = my_generator()
# print(g.__next__())
# g.close()

# array = {'a':1, 'b':2}
# print(array['c'])

# KeyboardInterrupt
# try:
# 	print("Press Return or Z:",)
# 	ignored = input()
# except Exception as err:
# 	print("Caught exception:", err)
# except KeyboardInterrupt as err:
# 	print("Caught KeyboardInterrupt")
# else:
# 	print("No exception")

# def fact(a):
# 	factors = []
# 	for i in range(1, a+1):
# 		if a%i == 0:
# 			factors.append(i)
# 	return factors

# num = 600851475143
# print(fact(num))

# class BaseClass(object):
#     """Defines the interface"""
#     def __init__(self):
#         super(BaseClass, self).__init__()
#     def do_something(self):
#         """The interface, not implemented"""
#         raise NotImplementedError(self.__class__.__name__ + '.do_something')
  
# class SubClass(BaseClass):
#     """Implementes the interface"""
#     def do_something(self):
#         """really does something"""
#         print (self.__class__.__name__ + ' doing something!')
  
# SubClass().do_something()
# BaseClass().do_something()

# import sys
  
# print ('Regular integer: (maxint=%s)' % sys.maxint)
# try:
#     i = sys.maxint * 3
#     print ('No overflow for ', type(i), 'i =', i)
# except OverflowError as err:
#     print ('Overflowed at ', i, err)
  
# print()
# print ('Long integer:')
# for i in range(0, 100, 10):
#     print ('%2d' % i, 2 ** i)
# print()
# print ('Floating point values:')
# try:
#     f = 2.0**i
#     for i in range(100):
#         print (i, f)
#         f = f ** 2
# except OverflowError as err:
#     print ('Overflowed after ', f, err)

# import gc
# import weakref

# class Foo(object):
# 	def __init__(self, name):
# 		self.name = name

# 	def __del__(self):
# 		print("(Deleting %s)" % self.name)

# obj = Foo('obj')
# p = weakref.proxy(obj)

# print("Before:", p.name)
# obj = None
# print('After:', p.name)