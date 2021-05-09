# Program to illustrate
# Finding common member in list
# using 'in' operator

# lst1 = [1, 2, 3, 4, 5]
# lst2 = [6, 2, 8, 9]

# for item in lst1:
# 	if item in lst2:
# 		print("overlapping")
# else:
# 	print("not overlapping")

# Same example without using in operator
# def overlapping(lst1, lst2):

# 	c = 0
# 	d = 0
# 	for i in lst1:
# 		c += 1
# 	for i in lst2:
# 		d += 1
# 	for i in range(0, c):
# 		for j in range(0, d):
# 			if(lst1[i] == lst2[j]):
# 				return 1
# 	return 0

# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9]
# if(overlapping(list1, list2)):
# 	print("overlapping")
# else:
# 	print("not overlapping")

# Program to illustrate not 'in' operator
# x = 24
# y = 20
# lst = [10, 20, 30, 40, 50]

# if(x not in lst):
# 	print("x is NOT present in given list")
# else:
# 	print('x is present in given list')

# if (y in lst):
# 	print("y is present in given list")
# else:
# 	print("y in NOT present in given list")

# Python program to illustrate the use
# of 'is' identity operator
x = 5
b = 10.2
if (type(x) is int):
	print("true")
else:
	print("false")

if(type(b) is type(x)):
	print("true")
else:
	print("false")
