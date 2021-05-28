# Code to demonstrate working of reduce()

import functools
# importing operator for operator functions
import operator
import itertools
# lis = [1, 3, 5, 6, 2]

# # using reduce to compute sum of list
# print("The sum of the list elements is : ", end="")
# print(functools.reduce(lambda a, b : a+b, lis))

# # using reduce to compute maximum element from list
# print("The maximum element of the list is : ", end="")
# print(functools.reduce(lambda a, b: a if a > b else b, lis))

# lis = [1, 3, 5, 6, 2]

# # using reduce to compute sum of list using operator functions
# print("The sum of the list elements is : ", end="")
# print(functools.reduce(operator.add, lis))

# # using reduce and operator functions to mul
# print('The product of the list elements is : ', end="")
# print(functools.reduce(operator.mul, lis))

# # using reduce to concatenate string
# print("The concatenated product is : ", end="")
# print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))

# difference of reduce() and accumulate() functions

# lis = [1, 3, 4, 10, 4]

# # printing summation using accumulate()
# print("The summation of list using accumulate is :", end="")
# print(list(itertools.accumulate(lis, lambda x, y : x+y)))

# # printin summation using reduce()
# print("The summation of list using reduce is :", end="")
# print(functools.reduce(lambda x, y: x+y, lis))

# Python program to illustrate sum of two numbers;

# def reduce(function, iterable, initializer=None):
# 	it = iter(iterable)
# 	if initializer is None:
# 		value = next(it)
# 	else:
# 		value = initializer
# 	for element in it:
# 		value = function(value, element)
# 	return value

# # Note that the initalizer, when not None, is used as 
# # the first value instead of the first value from iterable,
# # and after the whole iterable.

# tup = (2, 1, 0, 2, 2, 0, 0, 2)
# # Here the third argument 6 prints when tuple is empty.
# print(reduce(lambda x, y: x+y, tup, 6))

# Code to demonstrate the working of sum()
# take two arguments iterable : it can be anything, tuples, list, dictionary
# start : this start is added to the sum of number in the iterable
# numbers = [1, 2, 3, 4, 5, 1, 4, 5]

# # start parameter is not provided
# Sum = sum(numbers)
# print(Sum)

# Sum = sum(numbers, 10)
# print(Sum)

# Error and Exceptions
# TypeError: This error is raised in the case when there
# is anything other then numbers in the list

# arr = ['a']

# start parameter is not provided
# Sum = sum(arr)
# print(Sum)

# start = 10
# Sum = sum(arr, 10)
# print(Sum)

# Application: we require sum to be caluclated to finding out
# the average of numbers.

# Code to demonstrate the practical application of sum()
# numbers = [1, 2, 3, 4, 5, 1, 4, 5]

# # start = 10
# Sum = sum(numbers)
# average = Sum/len(numbers)
# print(average)

# dictionary = {1: 10, 2: 20}
# Sum = sum(dictionary.values())
# print(Sum)

# ord()

# integer representing the Unicode code
# value = ord("A")

# # writing in ' ' gives the same result
# value1 = ord('A')

# print(value, value1)

# # A TypeError is raised when the length of the string is 
# # not equal to 1 as shown below:
# # inbuilt function return an
# # integer representing the Unicode code demonstrating exception

# # Raises Exception
# value1 = ord('AB')

# print(value1)

# chr() function

# Program to illustrate chr() function 
# print(chr(71), chr(101),
# chr(101), chr(107),
# chr(115), chr(32),
# chr(102), chr(111),
# chr(114), chr(32),
# chr(71), chr(101),
# chr(101), chr(107),
# chr(115))

# Another example:
# numbers = [17, 38, 79]
# for number in numbers:
# 	# Convert ASCII-based number to character.
# 	letter = chr(number)
# 	print("Character of ASCII value", number, "is", letter)

# Code to demonstrate the working of cmp() and min().

# using integers
# list1 = [1, 2, 4, 3]
# print(max(list1))
# print(min(list1))

# using alphabets
# list1 = ['T', 'W', 'Z', 'A']
# print(max(list1))
# print(min(list1))

# Any() method
# print(any([False, False, False, False]))

# Here the method will short-circuit at the second
# item (True) and will return True.
# print(any([False, True, False, False]))

# Here the method will shor-circuit at the 
# first(True) and will return True.
# print(any([True, False, False, False]))

# Here all the iterables are True so all will
# return True and the same will be printed
# print(all([True, True, True, True]))

# Here the method will short-circuit at the first
# item (False) and will return False.
# print(all([False, True, True, False]))

# This statement will return False, as no 
# True is found in the iterables
# print(all([False, False, False]))


# Practical Example of any
# list1 = []
# list2 = []

# for i in range(1, 11):
# 	list1.append(4*i)

# for i in range(0, 10):
# 	list2.append(list1[i]%5 == 0)

# print("See whether at least one number is divisible by 5 in list 1=>")
# print(any(list2))

# Illustration of 'all' function in python 3

# list1 = []
# list2 = []

# for i in range(1, 21):
# 	list1.append(4*i-3)

# for i in range(0, 20):
# 	list2.append(list1[i]%2 == 1)

# print("See whether all numbers in list1 are odd =>")
# print(all(list2))

# len function returns the length of any iterable
# lst = [1, 2, 3, 4]
# print(len(lst))

# string = "Hello"
# print(len(string))

# tup = (2, 3, 4, 5)
# print(len(tup))

# dic = {1: 2, 2: 3, 4: 5}
# print(len(dic))

# Program to illustrate enumerate function
# l1 = ["eat", "sleep", "repeat"]
# s1 = "geek"

# obj1 = enumerate(l1)
# obj2 = enumerate(s1)

# print("Return type:", type(obj1))
# print(list(enumerate(l1)))

# print(list(enumerate(s1,2)))

# # Program to illustrate enumerate function in loops
# l1 = ["eat", "sleep", "repeat"]

# # printing the tuples in object directly
# for ele in enumerate(l1):
# 	print(ele)
# print()

# for count, ele in enumerate(l1, 100):
# 	print(count, ele)

# function that filters vowels
# def fun(var):
# 	letters = ['a', 'e', 'i', 'o', 'u']
# 	if(var in letters):
# 		return True
# 	else:
# 		return False

# seq = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
# filtered = filter(fun, seq)

# print("The filtered letters are: ")
# for s in filtered:
# 	print(s)

# Application

# a list contians, both eve and odd numbers.
# seq = [0, 1, 2, 3, 5, 8, 13]

# # result contains odd numbers of the list
# result = filter(lambda x: x % 2 != 0, seq)
# print(list(result))

# # result contains even numbers of the list
# result = filter(lambda x: x % 2 == 0, seq)
# print(list(result))

# map() returns map object after applying given function

# def addition(n):
# 	return n + n

# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))

# Code 2

# Double all numbers using map and lambda
# numbers = (1, 2, 3, 4)
# result = map(lambda x: x + x, numbers)
# print(list(result))

# Code 3

# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 60]

# result = map(lambda x, y: x + y, numbers1, numbers2)
# print(list(result))

# List of Strings
# l = ['sat', 'bat', 'cat', 'mat']

# # map() can listify the list of strings individually
# test = list(map(list, l))
# print(test)

# Python code to illustrate cube of a number
# showing difference between def() and lambda().

# def cube(y):
# 	return y*y*y 

# lambda_cube = lambda y: y*y*y 

# # using the normally
# # defined function
# print(cube(5))

# # using the lambda function
# print(lambda_cube(5))

# Code to return odd numbers from list

# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

# final_list = list(filter(lambda x: (x%2 != 0), li))
# print(final_list)

# Code to peole above 18 yrs
# ages = [13, 90, 17, 59, 21, 60, 5]

# adults = list(filter(lambda age: age>18, ages))
# print(adults)

# using lambda with map to convert int to char of lst items.

# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

# result = map(lambda x: str(x), li)
# print(list(result))

# Convert all lowercase items in uppercase of list
# animals = ["cat", 'mat', 'rat', 'parrot']

# uppered_name = list(map(lambda animal: str.upper(animal), animals))
# print(uppered_name)

# from functools import reduce
# li = [5, 8, 10, 20, 50, 100]
# sum = reduce((lambda x, y: x + y), li)
# print (sum)

# zip()

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)
print(dict(x))