# Program to convert a number to a list of digits

# n = 123456

# # Stores the list of digits
# lis = list(map(int, str(n)))

# print(lis)

# Converting setence into a list of words
 
# sentence = "GeeksForGeeks is the computer science portal for geeks"

# # Convert the setence into a list of words
# lis = list(sentence.split())

# print(lis)

# Program to take newline-separated input in the form
# of a list

# n = int(input())

# lis = [int(input()) for x in range(n)]

# print(lis)

# Program to demonstrate gcd() function
# import math
# a  = 8
# b = 24

# print(math.gcd(a, b))

# Program to print all permutations using library function
# from itertools import permutations

# # Get all permutations of [1, 2, 3]
# perm = permutations([1, 2, 3])

# # print the obtained permutations
# for i in list(perm):
# 	print(i)

# Program to print a string given number of times

# s = "India"
# print(s * 2)

# Program to print a list with spaces without loop
# li = [1, 2, 3, 4, 5]
# print(*li)

# Program to convert a binary string to its decimal equivalent
# using int() function

# binary = "1010"
# # Print decimal equivalent
# print(int(binary, 2))

# Print a sorted list with spaces using sorted() function
# li = [6, 2, 7, 3, 4]

# # Print the sorted sequence
# print(*sorted(li))

# Program to print common elements in both the 
# list using intersection() function
array1 = [4, 5, 6, 7, 8]
array2 = [3, 4, 5, 1, 72]

# Print the common elements
print(set(array1).intersection(set(array2)))

