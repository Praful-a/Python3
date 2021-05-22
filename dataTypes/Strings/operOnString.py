# Logical Opearators on String

# str1 = ''
# str2 = 'python'

# # repr is used to print the string along with quotes

# #Returns str1
# print(repr(str1 and str2))

# # Returns str2 
# print(repr(str1 or str2))

# print(repr(str2 or str1))

# str1 = 'for'

# # Returns str2
# print(repr(str1 and str2))

# # Returns str1
# print(repr(str2 and str1))

# # returns str1
# print(repr(str1 or str2))
# # returns str2
# print(repr(str2 or str1))

# str1 = 'geeks'
# print(repr(not str1))

# str1 = ''
# # Return True
# print(repr(not str1))

# String Formatting in Python using %

# 1) Using %
# 2) Using {}
# 3) Using Template Strings

'''Python program to demonstrate the use of formatting using %'''

# variable = '15'
# string = "variable as string = %s" %(variable)
# print(string)

# # printing a raw data
# print("variable as raw data = %r" %(variable))

# # Convert variable to integer
# variable = int(variable)
# string = "variable as integer = %d" %(variable)
# print(string)
# print("variable as float = %f" %(variable))

# # Printing as any string or char after a mark
# print("variable as printing with special char = %cmaaynak" %(variable))
# print("variable as hexadecimal = %x" %(variable))
# print("variable as octal = %o" %(variable))

 
# A Simple Python template example
from string import Template
# t = Template('x is $x')

# Substitute value of x in above template
# print(t.substitute({'x': 1}))

# Program to demonstrate the working of the string template
# Student = [('Ram', 90), ('Ankit', 78), ('Bob', 92)]

# t = Template("Hi $name, you have got $marks marks")
# for i in Student:
# 	print(t.substitute(name = i[0], marks = i[1]))

# template = Template('$name is the $job of $company')
# string = template.safe_substitute(name='Raju kumar', job='TCE')
# print(string)

# t = Template('I am $name from $city')
# print("Template String =", t.template)

# The $$ can be used to escape $ and treat as part of 
# the string

# template = Template('$$ is the symbol for $name')
# string = template.substitute(name='Dollar')
# print(string)

# template = Template('That $noun looks ${noun}y')
# string = template.substitute(noun='Fish')
# print(string)

# Find duplicate string
# def find_dup_char(input):
# 	dic = {}
# 	for s in input:
# 		if s not in dic:
# 			dic[s] = 1
# 		else:
# 			dic[s] += 1
# 	for c in dic:
# 		if dic[c] > 1:
# 			print(c, end="")
# 	print()

# if __name__ == '__main__':
# 	input = 'geeksforgeeks'
# 	find_dup_char(input)

# Reversing string using five different ways
'''Using loops'''
# def reverse(s):
# 	str = ""
# 	for i in s:
# 		str = i + str
# 	return str

# s = "geeksforgeeks"

# print("The original string is : ", end="")
# print(s)
# print("The reversed string(using loops) is : ", end="")
# print(reverse(s))


# Using recursion
# def reverse(s):
# 	if len(s) == 0:
# 		return s
# 	else:
# 		return reverse(s[1:]) + s[0]

# s = "geeksforgeeks"

# print("The original string is : ", end="")
# print(s)
# print("The reversed string(using loops) is : ", end="")
# print(reverse(s))

# Using extended slice syntax
# def reverse(s):
# 	s = s[::-1]
# 	return s

# s = "geeksforgeeks"

# print("The original string is : ", end="")
# print(s)
# print("The reversed string(using loops) is : ", end="")
# print(reverse(s))

# Using reversed
# def reverse(s):
# 	string = "".join(reversed(s))
# 	return string
	
# s = "geeksforgeeks"

# print("The original string is : ", end="")
# print(s)
# print("The reversed string(using loops) is : ", end="")
# print(reverse(s))

# Using Stack
# Python code to reverse a string using stack
# Function to create an empty stack. It initalizes size of 
# stack as 0
# def createStack():
# 	stack = []
# 	return stack

# # Function to determine the size of the stack
# def size(stack):
# 	return len(stack)

# # Stack is empty if the size is 0
# def isEmpty(stack):
# 	if size(stack) == 0:
# 		return True

# # Function to add an item to stack. It increases size 
# # by 1
# def push(stack, item):
# 	stack.append(item)

# # Function to remove an item from stack. 
# # It decreases size by 1
# def pop(stack):
# 	if isEmpty(stack): return
# 	return stack.pop()

# # A stack based function to reverse a string
# def reverse(string):
# 	n = len(string)

# 	stack = createStack()

# 	for i in range(0, n, 1):
# 		push(stack, string[i])

# 	string = ""

# 	for i in range(0, n, 1):
# 		string += pop(stack)

# 	return string

# s = 'Geeksforgeeks'
# print("The original string is : ", end="")
# print(s)
# print("The reversed string(using stack) is : ", end="")
# print(reverse(s))

# Check the string palindrome or not
# def ispalindrome(s):
# 	return s == s[::-1]

# # Driver Code
# s = 'Malayalam'
# ans = ispalindrome(s)

# if ans:
# 	print("Yes")
# else:
# 	print("No")

# Iterative Method

def ispalindrome(str):
	for i in range(0, int(len(str)/2)):
		if str[i] != str[len(str)-i-1]:
			return False
	return True

s = 'malayalam'
ans = ispalindrome(s)

if (ans):
	print("Yes")
else:
	print("No")