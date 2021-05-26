# ascii_letters returns all ASCII letters (both lower and upper case)
import string
import random
# result = string.ascii_letters
# print(result)

# Code to checks if the string input has only ASCII characters
# def check(value):
# 	for letter in value:
# 		if(letter not in string.ascii_letters):
# 			return False
# 	return True

# input1 = "GeeksForGeeks"
# print(input1, "-->", check(input1))

# input2 = "Geeks for Geeks"
# print(input2, '-->', check(input2))

# input3 = "Geeks_for_geeks"
# print(input3, "--> ", check(input3))


# Generating random password
# def rand_pass(size):
# 	generate_pass = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(size)])
# 	return generate_pass

# password = rand_pass(10)
# print(password)

# Generating random password by given string
# def rand_pass(size, scope = string.ascii_letters + string.digits):
# 	generate_pass = ''.join([random.choice(scope) for n in range(size)])
# 	return generate_pass

# password = rand_pass(10, 'Geeks3F0rgeeks')
# print(password)

# ascii_lowercase returns all the lowercase latters
# result = string.ascii_lowercase
# print(result)

# def check(value):
# 	for letter in value:
# 		if letter not in string.ascii_lowercase:
# 			return False
# 	return True

# input1 = "GeeksForGeeks"
# print(input1, "-->", check(input1))

# input2 = "geek for geeks"
# print(input2, "-->", check(input2))

# input3 = "geeksforgeeks"
# print(input3, "-->", check(input3))

# generating strong passwrod using ascii_lowercase
# def rand_pass(size):
# 	generate_pass = ''.join([random.choice(string.ascii_lowercase +
# 						string.digits) for n in range(size)])

# 	return generate_pass

# password = rand_pass(10)
# print(password)

# ascii_uppercase returns all uppercase letters

# result = string.ascii_uppercase
# print(result)

# def check(value):
# 	for letter in value:
# 		if letter not in string.ascii_uppercase:
# 			return False
# 	return True

# input1 = "GeeksForGeeks"
# print(input1, "-->", check(input1))

# input2 = "GEEKS FOR GEEKS"
# print(input2, "-->", check(input2))

# input3 = "GEEKSFORGEEKS"
# print(input3, "-->", check(input3))

# Generating random password
# def rand_pass(size):
# 	generate_pass = ''.join([random.choice(string.ascii_uppercase + string.digits) for n in range(size)])

# 	return generate_pass

# password = rand_pass(10)
# print(password)

# digits returns 0-9

# result = string.digits
# print(result)

# Checking string contains digits or not

# def check(value):
# 	for letter in value:
# 		if letter not in string.digits:
# 			return False
# 	return True

# input1 = "0123 456 789"
# print(input1, '--> ', check(input1))

# input2 = "12.0124"
# print(input2, "-->", check(input2))

# # input3 = "Python 2322"  # this will return FAlSE
# input3 = "239230200"
# print(input3, "-->", check(input3))

# hexdigits returns all hexadecimal digits

# result = string.hexdigits
# print(result)

# check the substring contains hexadecimal or not
# def check(value):
# 	for letter in value:
# 		if letter not in string.hexdigits:
# 			return False
# 	return True

# input1 = "0123456789abcdef"
# print(input1, "-->", check(input1))

# input2 = "abcdefABCDEF"
# print(input2, "-->", check(input2))

# input3 = "abcdefghGEEK"
# print(input3, "-->", check(input3))

# random password script
# def rand_pass(size):
# 	generate_pass = ''.join([random.choice(string.hexdigits) for n in range(size)])
# 	return generate_pass

# password = rand_pass(10)
# print(password)

# octdigits returns all octal numbers 0-7

# result = string.octdigits
# print(result)

# check whether a sting contains octal digits

# def check(value):
# 	for x in value:
# 		if x not in string.octdigits:
# 			return False
# 	return True

# input1 = "01234567"
# print(input1, '-->', check(input1))

# input2 = "0123  4567"
# print(input2, '-->', check(input2))

# input3 = "abcdef01234567"
# print(input3, '-->', check(input3))

# Script for generating random password

# def rand_pass(size):
# 	generate_pass = ''.join([random.choice(string.octdigits + string.ascii_lowercase) for n in range(size)])
# 	return generate_pass

# password = rand_pass(10)
# print(password)

# punctuation returns all punctuation marks uses in sentences.
# result = string.punctuation
# print(result)

# check if the string having punctuation marks or not

# def check(st):
# 	for value in st:
# 		if value not in string.punctuation:
# 			return False
# 	return True

# input1 = "abcd(*}}]"
# print(input1, '-->', check(input1))

# input2 = "/\\*,;(*}}]"
# print(input2, '-->', check(input2))

# input3 = "abcd(*}}]12123"
# print(input3, '-->', check(input3))

# Application : checking in password having marks or not

# def check_pass(st):
# 	for value in st:
# 		if value in string.punctuation:
# 			return True
# 	return False

# input1 = "Praful*2323"
# print(input1, '-->', check_pass(input1))

# input2 = "Praful2323"
# print(input2, '-->', check_pass(input2))


# input3 = "Praful(2323)"
# print(input3, '-->', check_pass(input3))

# printable returns all symbols and letters which are printable
# result = string.printable
# print(result)

# endswith return True if suffix with string's end part
# text = "geeks for geeks."

# result = text.endswith('for geeks')
# print(result)

# result = text.endswith('geeks.')
# print(result)

# result = text.endswith('for geeks.')
# print(result)

# result	= text.endswith('geeks for geeks.')
# print(result)

# code 2

# text = "geeks for geeks"

# result = text.endswith('geeks', 10)
# print(result)

# result = text.endswith('geeks', 10, 16)
# print(result)

# result = text.endswith('geeks', 10, 15)
# print(result)

# Python code to demonstrate working of startswith()

# text = "geeks for geeks"

# result = text.startswith('for geeks')
# print(result)

# result = text.startswith('geeks')
# print(result)

# result = text.startswith('for geeks.')
# print(result)

# result = text.startswith('geeks for geeks')
# print(result)

# is digit() method returns True if all characters in the
# string are digits 0-9

# string = '15450'
# print(string.isdigit())

# string = "153ayush80"
# print(string.isdigit())

# Programt to illustrate application of isdigit()
# initializing Empty string

# newString = ""

# count = 0

# for a in range(53):
# 	b = chr(a)
# 	if b.isdigit() == True:
# 		count += 1
# 		newString += b;
# print("Total digits in range :", count)
# print("Digits :", newString)


# s = '23455'
# print(s.isdigit())

# s = '\u00B23455'
# print(s)
# print(s.isdigit())

# s = "\u00BD"
# print(s)
# print(s.isdigit())

# isalpha() returns True if string contains only alphabets

# s = "aplsd"
# print(s.isalpha())

# Program to demonstrate the use of isdecimal()
# s = "12345"
# print(s.isdecimal())

# s = "12geeks34"
# print(s.isdecimal())

# s = "12 34"
# print(s.isdecimal())

# Program to demonstrate the str.format() method

# using format option in a simple string
# print("{}, A computer science portal for geeks.".format("GeekforGeeks"))

# # using format option for a value stored in a variable
# str = "This article is written in {}"
# print(str.format("Python"))

# print("Hello, I am {} years old !".format(18))

# Program to demonstrating Index Error
# Number of placeholders are four but there are
# only three values passed

# my_string = "{}, is a {} {} science portal for {}"
# print(my_string.format("GeeksForGeeks", "computer", "geeks"))

# Formatters with miltiple placeholders

# my_string = "{}, is {} science portal for {}"
# print(my_string.format("GeeksforGeeks", "computer", "geeks"))

# print("Hi ! My name is {} and I am {} years old.".format("User", 19))
# print("This is {} {} {} {}".format("one", "two", "three", "four"))

# Formatters with positional key arguments.

# print("{0} love {1}!!".format("GeeksforGeeks", "Geeks"))

# print("{1} love {0}!!".format("GeeksforGeeks", "Geeks"))

# print("Every {} should know the use of {} {} programming and {}"
# 			.format("prorammer", "Open", "Source", "Operating Systems"))

# Use the index numbersof the values to change 
# the order that they appear in the string
# print("Every {3} should know the use of {2} {1} programming and {0}"
# 	.format("prorammer", "Open", "Source", "Operating Systems"))

# Keyword arguments are called by their keyword name
# print("{gfg} is a {0} science portal for {1}".format("computer", "geeks", gfg = "GeeksforGeeks"))

# Demonstrating ValueError while doing forced type-conversion
# print("The temperature today is {0:d} degrees outside !".format(35.567))

# Convert base-10 decimal integers to floating point numeric
# constants

# print("This site is {0:f}% securely {1}!!".format(100, "encrypted"))

# # To limit the precision
# print("My average of this {0} was {1:.2f}%".format("semester", 78.234876))

# # For no decimal places
# print("My average of this {0} was {1:.0f}%".format("semester", 78.2347876))

# # Convert an integer to its binary or 
# # with other different converted bases.
# print("The {0} of 100 is {1:b}".format("binary", 100))
# print("The {0} of 100 is {1:o}".format("octal", 100))

# To demonstrate spacing when strings are passed as 
# parameters
# print("{0:4}, is the computer science portal for {1:8}!".format("GeeksforGeeks", "geeks"))

# # To demonstrate spacing when numeric constant are
# # passed as parameters.
# print("It is {0:5} degrees outside!".format(40))

# # To demonstrate both string and numeric constants
# # passed as parameters
# print("{0:4} was founded in {1:16}!".format("GeeksforGeeks", 2009))

# # To demonstrate aligning of spaces
# print("{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2009))
# print("{:*^26s}".format("Geeks"))

# which prints out i, i ^ 2, i ^ 3
# i ^ 4 in the given range

# Function prints out values in an unorganized manner
# def unorganized(a, b):
# 	for i in range(a, b):
# 		print(i, i**2, i**3, i**4)

# # Function prints the organized set of values
# def organized(a, b):
# 	for i in range(a, b):

# 		# Using formatters to give 6
# 		# spaces to each set of values
# 		print("{:6d} {:6d} {:6d} {:6d}".format(i, i**2, i**3, i**4))

# n1 = int(input("Enter lower range :-\n"))
# n2 = int(input("Enter upper range :-\n"))

# print("---------Before Using Formatters--------")
# unorganized(n1, n2)

# print()
# print("--------After Using Formatters-------")
# print()

# organized(n1, n2)

# print("{:>6s} {:^3s} {:<6s}".format("Geeks", "For", "Geeks"))

# Code to demonstrate the working of index()

# initializing target string
# ch = "geeksforgeeks"
# ch1 = "geeks"

# pos = ch.index(ch1,2)

# print("The first position of geeks after 2nd Index : ", end="")
# print(pos)

# This will give an error
# ch1 = "gfg"
# pos = ch.index(ch1)
# print('The first position of gfg is : ', end="")
# print(pos)

# Application 
voltages = ["001101 AC", "0011100 DC", "0011100 AC", "001 DC"]
type = "AC"

sum_bits = 0
for i in voltages:
	ch = i
	if (ch[len(ch)-2]!='D'):
		bit_len = ch.index(type) -1
		sum_bits = sum_bits + bit_len

print("The total bit length of AC is : ", end="")
print(sum_bits)