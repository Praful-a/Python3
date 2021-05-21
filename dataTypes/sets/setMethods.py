# set of letters
# GEEK = {'g', 'e', 'k'}

# # adding 's'
# GEEK.add('s')
# print('Letters are:', GEEK)

# # adding 's' again
# GEEK.add('s')
# print('Letters are:',GEEK)

# set of letters
# GEEK = {6, 0, 4}

# # adding 1
# GEEK.add(1)
# print('Letters are:', GEEK)

# # adding 0
# GEEK.add(0)
# print('Letters are:', GEEK)

# Python code to demonstrate addition of tuple to a set.
# s = {'g', 'e', 'e', 'k', 's'}
# t = ('f', 'o')

# # adding tuple t to set s.
# s.add(t)
# print(s)

# def Remove(sets):
# 	sets.discard(20)
# 	print(sets)

# sets = set([10, 20, 26, 41, 54, 20])
# Remove(sets)

# def Remove(sets):
# 	sets.discard(21)
# 	print(sets)

# sets = set([10, 20, 26, 41, 54, 20])
# Remove(sets)

# Function to remove elements using remove()
# def Remove(sets):
# 	sets.remove('aakash')
# 	print(sets)

# sets = set(['ram', 'aakash', 'kaushik', 'anand', 'prashant'])
# Remove(sets)

# if the element is not present in the list
# def Remove(sets):
# 	sets.remove('gaurav')
# 	print(sets)

# sets = set(['ram', 'aakash', 'kaushik', 'anand', 'prashant'])
# Remove(sets)


# set of letters
# GEEK = {'g', 'e', 'e', 'k', 's'}
# print('Geek before clear: ', GEEK)

# clearing vowels
# GEEK.clear()
# print('Geek after clear:', GEEK)


# Program to demonstrate copy() in set

# set1 = {1, 2, 3, 4}
# # function to copy the set
# print(set1)
# set2 = set1.copy()
# set2.add(5)
# print(set2)
# print(set1)

# Code to illustrate pop() method
# s = {'ram', 'rahim', 'ajay', 'rishav', 'aakash'}

# # Popping three elements and printing them
# print(s.pop())
# print(s.pop())
# print(s.pop())

# # The updated set
# print("Updated set is", s)

# Program to demonstrate the use of update() method
# lst1 = [1, 2, 3]
# lst2 = [5, 6, 7]
# lst3 = [10, 11, 12]

# # Lists converted to sets
# set1 = set(lst2)
# set2 = set(lst1)

# # updated Method
# set1.update(set2)

# # Print the updated set
# print(set1)

# # List is passed as an parameter which gets
# # automatically  converted to a set
# set1.update(lst3)
# print(set1)

# Program to demonstrate the use of update() method

# lst1 = [1, 2, 3, 4]
# lst2 = [1, 4, 2, 3, 5]
# alphabet_set = {'a', 'b', 'c'}

# # list converted to sets
# set1 = set(lst2)
# set2 = set(lst1)

# # update method
# set1.update(set2)

# # Print the updated set
# print(set1)

# set1.update(alphabet_set)
# print(set1)

# Program for union() function
# set1 = {2, 4, 5, 6}
# set2 = {4, 6, 7, 8}
# set3 = {7, 8, 9, 10}

# # union of two sets
# print('set1 U set2 : ', set1.union(set2))

# # union of three sets
# print("set1 U set2 U set3 :", set1.union(set2, set3))

# Using difference() between set A and set B

# Driver Code
# A = {10, 20, 30, 40, 80}
# B = {100, 30, 80, 40, 60}
# print(A.difference(B))
# print(B.difference(A))

# A = {10, 20, 30, 40, 80}
# B = {100, 30, 80, 40, 60}
# print(A - B)
# print(B - A)

# If we have equal sets then it will return the null set

# A = {10, 20, 30, 40, 80}
# B = {10, 20, 100, 30, 80, 40, 60}
# print(A - B)


# Using difference_update() between set A and set B

# Driver Code
# A = {10, 20, 30, 40, 80}
# B = {100, 30, 80, 40, 60}

# # Modifies A and return None
# A.difference_update(B)

# # prints the modified set
# print(A)

# Program for intersection() function
# set1 = {2, 4, 5, 6}
# set2 = {4, 6, 7, 8}
# set3 = {4, 6, 8}

# # union of two sets
# print("set1 intersection set2 : ", set1.intersection(set2))

# # union of three sets
# print("set1 intersection set2 intersection set3 :", set1.intersection(set2, set3))

# Program to isdisjoint() function
# set1 = {2, 4, 5, 6}
# set2 = {7, 8, 9, 10}
# set3 = {1, 2}

# # checking of disjoint of two sets
# print("set1 and set2 are disjoint?", set1.isdisjoint(set2))
# print("set1 and set3 are disjoint?", set1.isdisjoint(set3))

# Program to demonstrate working of issubset().
# A = {4, 1, 3, 5}
# B = {6, 0, 4, 1, 5, 0, 3, 5}

# # Returns True
# print(A.issubset(B))

# # Returns False
# # B is not subset of A
# print(B.issubset(A))

# A = {1, 2, 3}
# B = {1, 2, 3, 4, 5}
# C = {1, 2, 4, 5}

# # Returns True
# print(A.issubset(B))

# # Returns False
# # B is not subset of A
# print(B.issubset(A))

# # Returns False
# print(A.issubset(C))

# # Returns True
# print(C.issubset(B))

# Program to demonstrate working of issuperset().
# A = {4, 1, 3, 5}
# B = {6, 0, 4, 1, 5, 0, 3, 5}

# print("A.issuperset(B)", A.issuperset(B))

# # B is superset of A
# print("B.issuperset(A) :", B.issuperset(A))

# Program to demonstrate working of issuperset().
# A = {1, 2, 3}
# B = {1, 2, 3, 4, 5}
# C = {1, 2, 4, 5}

# print("A.issuperset(B : ", A.issuperset(B))
# print("B.issuperset(A) : ", B.issuperset(A))
# print("A.issuperset(C) : ", A.issuperset(C))
# print("C.issuperset(B) : ", C.issuperset(B))

# Python code to find the symmetric_difference 
# Use of symmetric_difference() method
# set_A = {1, 2, 3, 4, 5}
# set_B = {6, 7, 3, 9, 4}
# print(set_A.symmetric_difference(set_B))
# print(set_A ^ set_B)

# Program to demonstrate working of symmetric_difference_update()
# A = {'p', 'a', 'w', 'a', 'n'}
# B = {'r', 'a', 'o', 'n', 'e'}

# # result is always none.
# result = A.symmetric_difference_update(B)

# print('A = ', A)
# print('B = ', B)
# print('result = ', result)

A = {1, 2, 3, 4, 5, 6}
B = [4, 5, 7, 8]

A.symmetric_difference_update(B)
print('A = ', A)

A = {2, 4, 6, 8}
B = (i for i in range(2, 6))
A.symmetric_difference_update(B)
print("A=", A)