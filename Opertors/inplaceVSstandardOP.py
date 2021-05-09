# Python code to demonstrate difference between Inplace
# and Normal operators in Immutable Targets

# importing operator to handle operator operations
import operator

# initializing values
# x = 5
# y = 6
# a = 5
# b = 6

# using add() to add the arguments passed 
# z = operator.add(a, b)

# using iadd() to add the arguments passed
# p = operator.iadd(x, y)

# printing the modified value
# print("Value after adding using normal operator : ", end="")
# print(z)

# printing value of first argument
# value is unchanged
# print("Value of first argument using normal operator : ", end="")
# print(a)

# printing value of first argument
# value is unchanged
# print('Value of first argument using Inplace operator : ', end="")
# print(x)


# Program to demonstrate difference between Inplace and
# Normal operators in mutable Targets

# Initialzing list
# a = [1, 2, 4, 5]

# using add() to add the arguments passed
# z = operator.add(a, [1, 2,3])

# printing the modified value
# print("Value after adding using normal operator : ", end="")
# print(z)

# Printing value of the first argument
# value is unchanged
# print("Value after adding using normal operator : ", end="")
# print(a)

# using iadd() to add the arguments passed performs
# a += [1, 2, 3]
# p = operator.iadd(a, [1, 2, 3])

# printing the modified value
# print("Value after adding using Inplace opertor : ", end="")
# print(p)

# Printing value of the first argument
# Value is changed now
# print(a)

# Code to demonstrate the working of ixor() and ipow()

# using ixor() to exclusive or and assign vlaue
# a = 10
# b = 5
# x = operator.ixor(a, b)

# # printing the modified value
# print("The value after xoring and assigning : ", end="")
# print(x)

# # Printing value of first argument
# print(a)

# # using ipow() to exponentiate and assign value
# n = 5
# p = 4
# x = operator.ipow(n, p)

# # Printing the modified value
# print("The value after exponentiate and assigning : ",end="")
# print(x)

# # Printing value of first argument
# print(n)

# a = 10
# b = 5
# x = operator.ior(a, b)

# # printing the modified value
# print("The value after oring and assigning : ", end="")
# print(x)

# # Printing value of first argument
# print(a)

# # using ipow() to exponentiate and assign value
# n = 5
# p = 4
# x = operator.iand(n, p)

# # Printing the modified value
# print("The value after anding and assigning : ",end="")
# print(x)

# # Printing value of first argument
# print(n)


# a = 8
# b = 2
# x = operator.ilshift(a, b)

# # printing the modified value
# print("The value after bitwise left shift assigning : ", end="")
# print(x)

# # Printing value of first argument
# print(a)

# # using ipow() to exponentiate and assign value
# n = 8
# p = 2
# x = operator.irshift(n, p)

# # Printing the modified value
# print("The value after bitwise right shift assigning : ",end="")
# print(x)

# # Printing value of first argument
# print(n)


# # Code to demonstrate the working of iadd() and iconcat()

# # using iadd() to add and assign value
# x = operator.iadd(2, 3)

# # printing the modified value
# print("The value after adding and assigning : ", end="")
# print(x)

# # initializing values
# y = "Hello"
# z = "World!"

# # using iconcat() to concat the sequence
# y = operator.iconcat(y, z)

# # using iconcat() to concat sequences
# print('The string after concatination is : ', end="")
# print(y)

# # Code to demonstrate the working of imul() and isub()

# # using isub() to add and assign value
# x = operator.isub(2, 3)

# # printing the modified value
# print("The value after subtracting and assigning : ", end="")
# print(x)

# # using imul() to concat the sequence
# y = operator.imul(2, 3)

# # using imul() to concat sequences
# print('The string after multiplying and assigning : ', end="")
# print(y)

# Code to demonstrate the working of itruediv() and imod(), idiv

# using iturediv() to add and assign value
x = operator.itruediv(10, 2)

# printing the modified value
print("The value after dividing and assigning : ", end="")
print(x)

# using imod() to concat the sequence
y = operator.imod(10, 6)

# using imod() to concat sequences
print('The string after modulus and assigning : ', end="")
print(y)
