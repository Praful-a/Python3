# Program to demonstrate iterator module

# import operator
# import time

# # Defining lists
# l1 = [1, 2, 3]
# l2 = [2, 3, 4]

# # Starting time before map
# # function
# t1 = time.time()

# # Calculating result
# a, b, c = map(operator.mul, l1, l2)

# # Ending time after map function
# t2 = time.time()

# # Time taken by map function
# print("Result : ", a, b, c)
# print("Time taken by map function : %.6f" %(t2 - t1))

# # Starting time before naive method
# t1 = time.time()

# # Calculating result using for loop
# print("Result:", end=" ")
# for i in range(3):
# 	print(l1[i] * l2[i], end=" ")

# # Ending time after naive method
# t2 = time.time()
# print("\n Time taken by for loop: %.6f" %(t2 - t1))


# Program to demonstrate infinite iterators
# import itertools

# for in loop
# for i in itertools.count(5, 5):
# 	if i == 35:
# 		break
# 	else:
# 		print(i, end=" ")

# count = 0
# for i in itertools.cycle('AB'):
# 	if count > 7:
# 		break
# 	else:
# 		print(i, end=" ")
# 		count += 1

# using next function
# l = ['I', 'Love', 'Python']

# iterators = itertools.cycle(l)

# for i in range(6):
# 	print(next(iterators), end=" ")

# repeat()

# print("Printing the numbers repeatedly : ")
# print(list(itertools.repeat(25, 4)))

# import the product function from itertools module
# from itertools import product

# print("The cartesian product using repeat: ")
# print(list(product([1, 2], repeat = 2)))
# print()

# print("The cartesian product of the containers:") 
# print(list(product(['geeks', 'for', 'geeks'], '2'))) 
# print() 

# print("The cartesian product of the containers:")
# print(list(product('AB', [3, 4])))

# Program to make permutations

# print("All the permutations of the given list is:")
# print(list(itertools.permutations([1, 'geeks'], 2)))

# print("All the permutations of the given string is:")
# print(list(itertools.permutations('AB')))

# print("All the permutations of the given container is:")
# print(list(itertools.permutations(range(3), 2)))


# from itertools import *

# print("All the combination of list in sorted order(without replacement) is:")
# print(list(combinations(['A', 2], 2)))
# print()

# print("All the combinations of string in sorted order(without replacement) is:")
# print(list(combinations('AB', 2)))
# print()

# print("All the combination of list in sorted order(without replacement) is:")
# print(list(combinations(range(4), 2)))

# import combinations from itertools module
# print("All the combination of string in sorted order(with replacement) is:")
# print(list(combinations_with_replacement("AB", 2)))
# print()

# print("All the combination of list in sorted order(with replacement) is:")
# print(list(combinations_with_replacement([1, 2], 2)))
# print()

# print("All the combination of container in sorted order(with replacement) is:")
# print(list(combinations_with_replacement(range(2), 1)))


# accumulate()

import itertools
import operator

# initializing list 1
# li1 = [1, 4, 5, 7]

# using accumlate()
# prints the successive summation of elements
# print("The sum after each iteration is : ", end="")
# print(list(itertools.accumulate(li1)))

# using accumulate()
# prints the successive multiplication of elements
# print('The product after each iteration is : ', end="")
# print(list(itertools.accumulate(li1, operator.mul)))

# using accumulate()
# prints the successive summation of elements
# print("the sum after each iteration is : ", end="")
# print(list(itertools.accumulate(li1)))

# using accumulate() 
# prints the successive multiplication of elements 
# print ("The product after each iteration is : ", end ="") 
# print (list(itertools.accumulate(li1, operator.mul)))

# Workgin of chain()

# li1 = [1, 4, 5, 7]
# li2 = [1, 6, 5, 9]
# li3 = [8, 10, 5, 4]

# print("All values in mentioned chain are : ", end="")
# print(list(itertools.chain(li1, li2, li3)))

# li1 = [1, 4, 5, 7] 
    
# # initializing list 2 
# li2 = [1, 6, 5, 9] 
    
# # initializing list 3 
# li3 = [8, 10, 5, 4] 
    
# # intializing list of list 
# li4 = [li1, li2, li3] 
  
# # using chain.from_iterable() to print all elements of lists 
# print ("All values in mentioned chain are : ", end ="") 
# print (list(itertools.chain.from_iterable(li4)))

# Working of compress()
# print("The compressed values in string are : ", end="")
# print(list(itertools.compress('GEEKSFORGEEKS', [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0])))

# Working of dropwhile
# li = [2, 4, 5, 7, 8]

# print("The values after condition returns false : ", end="")
# print(list(itertools.dropwhile(lambda x: x % 2 == 0, li)))

# li = [2, 4, 5, 7, 8]

# print("The Values that returns false to function are : ",end="")
# print(list(itertools.filterfalse(lambda x: x % 2 == 0, li)))

# Working of islice()
# li = [2, 4, 5, 7, 8, 10, 20]

# # using islice() to slice the list acc. to need
# # starts printing from 2nd index till 6th skipping 2
# print("the sliced list values are : ", end="")
# print(list(itertools.islice(li, 1, 6, 2)))

# Working of starmap()

# # li = [(1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10, 1)]
# li = [[1, 10, 5], [8, 4, 1], [5, 4, 9], [11, 10, 1]]

# # using starmap() for selection value acc. to function
# # selects min of all tuple values
# print("The values acc. to function are : ", end="")
# print(list(itertools.starmap(min, li)))


# Python code to demonstrate the working of  
# takewhile()
    
  
# import itertools 
    
# # initializing list  
# li = [2, 4, 6, 7, 8, 10, 20] 
    
# # using takewhile() to print values till condition is false. 
# print ("The list values till 1st false value are : ", end ="") 
# print (list(itertools.takewhile(lambda x : x % 2 == 0, li )))

# initializing list  
# li = [2, 4, 6, 7, 8, 10, 20] 
    
# # storing list in iterator 
# iti = iter(li)  
    
# # using tee() to make a list of iterators 
# # makes list of 3 iterators having same values. 
# it = itertools.tee(iti, 3) 
    
# # printing the values of iterators 
# print ("The iterators are : ") 
# for i in range (0, 3): 
#     print (list(it[i])) 

# Working of zip_longest()

# print("The combined values of iterables is :")
# print(*(itertools.zip_longest('GesoGes', 'ekfrek', fillvalue='_')))

