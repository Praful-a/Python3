# my_list = ['I', 'Love']
# my_list.append("Python")
# print(my_list)

# my_list = [1, 2, 3, 4]
# my_list.append([1,2,3])
# print(my_list)

# my_list = [1, 2, 3, 4]
# my_list.extend([5, 6, 7, 8])
# print(my_list)

# my_list = [1, 2, 3, 4]
# my_list.extend("geeks")
# print(my_list)

# my_list = [1, 2, 3, 4]
# my_list.append("Geeks")
# print(my_list)


# Code to demonstrate the working of del and pop()

# lst = [2, 1, 3, 4, 5, 6, 8]

# del lst[2 : 5]
# print("List elements after deleting are : ", end="")
# for i in range(0, len(lst)):
# 	print(lst[i], end=" ")

# print("\r")

# lst.pop()
# lst.pop(0)
# pop also return the popped item from list
# popped = lst.pop(0)
# print("The popped item is :", popped)
# print("List elements after popping are :", end="")
# for i in range(0, len(lst)):
# 	print(lst[i], end=" ")


# Python code to demonstrate the working of insert() and remove()

# lst = [2, 1, 3, 4, 5, 8]

# lst.insert(3, 4)

# print("List elements after increating 4 are : ", end="")
# for i in range(0, len(lst)):
# 	print(lst[i], end=" ")

# # removes 3 at pos 2
# lst.remove(3)

# print("List elements after removing are : ", end="")
# for i in range(0, len(lst)):
# 	print(lst[i], end=" ")

# Code to demonstrate the working of sort() and reverse()
# lst = [2, 1, 3, 5, 3, 8]

# lst.sort()

# print("List elements after sorting are : ", end="")
# for i in range(0, len(lst)):
# 	print(lst[i], end=" ")
# print("\r")

# lst.reverse()
# print("List elements after reversing are :", end="")
# for i in range(0, len(lst)):
# 	print(lst[i], end=" ")

# Program to demonstrate of list index() method

# lst = [1, 2, 3, 4, 1, 1, 1, 4, 5]
# print(lst.index(4))

# # lst2 = ['Cat', 'Bat', 'mat', 'cat', 'pet']
# # print(lst2.index('Cat'))

# print(lst.index(4, 4, 8))

# print(lst.index(1, 1, 7))

# lst2 = ['cat', 'bat', 'mat', 'cat',
# 		'get', 'cat', 'sat', 'pet']
# print(lst2.index('cat', 2, 6))

# lst1 = [1, 2, 3, [9, 8, 7], ('cat', 'bat')]
# print(lst1.index([9, 8, 7]))

# # will print the index of tuple ('cat', 'bat') inside list
# print(lst1.index(('cat', 'bat')))


# Program to demonstrate index() with two arguments

# lst = [6, 8, 5, 6, 1, 2]
# print(lst.index(6, 1))

# list1 = [6 , 2 , 14 , 8 , 9 , 10]
 
 
# # Will print index of '4' in sublist as now index '4' is included
# # having index from 1 to 5.
# print(list1.index(9, 1, 5))

# sort() function 
# num = [1, 2, 3, 4]

# num.sort()

# print(num)

# # List of Floating point numbers
# decimalnum = [2.01, 2.00, 3.67, 3.28, 1.68]
# decimalnum.sort()
# print(decimalnum)

# words = ['Geeks', 'For', 'Geeks']
# words.sort()
# print(words)

# numbers = [1, 3, 4, 2]
# numbers.sort(reverse=True)
# print(numbers)

# decimalnum = [2.01, 2.00, 3.67, 3.28, 1.68]
# decimalnum.sort(reverse=True)
# print(decimalnum)

# words = ['Geeks', 'For', 'Geeks']
# print(words)

# function to return the second element of two elements
# passed as the parameter
# def sortSecond(val):
# 	return val[1]

# lst = [(1, 2), [3, 3], [1, 1]]
# lst.sort(key=lambda x : x[1])
# print(lst)

# lst.sort(reverse=True, key=lambda x: x[1])
# print(lst)

# Program to demonstrate working of list.copy()

lst = [1, 2, 3, 4]
lst2 = lst.copy()

print("The new list created is : " + str(lst2))
lst2.append(5)

print("The new list : " + str(lst2))
print("The old list : " + str(lst))