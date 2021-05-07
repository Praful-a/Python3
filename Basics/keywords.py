"""
# True: This keyword is used to represent a boolean true. If a 
statement is true, "True" is printed.
# False: This keyword is used to represent a boolean false. If
a statement is false, "False" is printed
"""

# print(False == 1)
# print(True == 1)

# print(True + True + True)
# print(True + False + False)

# Python code to demonstrate
# True, False, None, and, or, not

# showing that None is not equal to 0
# prints False as its false.
# print(None == 0)

# showing objective of None
# two None value equated to None
# here x and y both are null
# hence True
# x = None
# y  = None
# print(x == y)

# Showing logical operation
# and (returns False)
# print(False and True)
# print(3 and 0)
# print(3 and 10)
# print(0 or 3)
# print(3 or 10)

# showing logical operation
# not (returns False)
# print(not True)

## del and assert ##
# a = [1, 2, 3]

# printing list before deleting any value
# print("The list before deleting any value")
# print(a)

# using del to delete 2nd element of list
# del a[1]

# printint list after deleting 2nd element
# print("The list after deleting 2nd element")
# print(a)

# use of assert prints AssertionError
# assert 5 < 3, "5 is not smaller than 3"

# code to demonstrate working of in and is

# using "in" to check
# if 'l' in 'HelloWorld':
# 	print("l is part of HelloWorld")
# else:
# 	print("l is not part of HelloWorld")

# using 'in' to loop through
# for i in "HelloWorld":
# 	print(i, end=" ")

# print('\r');

# using is to check object identity
# string is immutable(cannot be changed once allocated)
# hence occupy same memory location
# print(' ' is ' ')

# using is to check ojbect identity
# dictionary is mutable( can be changed once allocated)
# hence occupy different memory location
# print({} is {})

# global and non local
# a = 10
 
# used to read the variable
# def read():
#     print (a)
 
# changing the value of globally defined variable
# def mod1():
#     global a
#     a = 5
 
# changing value of only local variable
# def mod2():
#     a = 15
 
# reading initial value of a
# prints 10
# read()
 
# calling mod 1 function to modify value
# mod1()

# again prints
# read()

# calling mod 2 function to modify value
# modifies value of local a to 15, doesn't effect global value
# mod2()

# read()

# demonstrating non local
# inner loop changing the value of outer a
# prints 10
# print("Value of a using nonlocal is : ", end="")
# def outer():
# 	a = 5
# 	def inner():
# 		nonlocal a
# 		a = 10
# 	inner()
# 	print(a)

# outer()

# demonstrating without non local
# inner loop not changing the value of outer a
# prints 5
# print("Value of a without using nonlocal is : ", end="")
# def outer():
# 	a = 5
# 	def inner():
# 		a = 10
# 	inner()
# 	print(a)

# outer()
