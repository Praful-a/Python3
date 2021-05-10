# demonstrating basic use of iter()

# listA = ['a', 'e', 'i', 'o', 'u']
# iter_listA = iter(listA)
# try:
# 	print(next(iter_listA))
# 	print(next(iter_listA))
# 	print(next(iter_listA))
# 	print(next(iter_listA))
# 	print(next(iter_listA))
# 	print(next(iter_listA)) # StopIteration exception
# except StopIteration :
# 	print("Error")

# Code to demonstrate basic use of iter()

# lst = [11, 2, 33, 4, 55]

# iter_lst = iter(lst)
# while True:
# 	try:
# 		print(iter_lst.__next__())
# 	except:
# 		break

# Example 2
# lstB = ['Cat', 'Bat', 'Sat', 'Mat']

# iter_listB = lstB.__iter__()

# try:
# 	print(iter_listB.__next__())
# 	print(iter_listB.__next__())
# 	print(iter_listB.__next__())
# 	print(iter_listB.__next__())
# 	print(iter_listB.__next__()) # Stopiteration exception
	
# except:
# 	print("\n Throwing 'StopIteration' ",
# 			"I cannot count more.")


# Example 3

# Python code showing use of iter() using OOPs
  
# class Counter:
#     def __init__(self, start, end):
#         self.num = start
#         self.end = end
  
#     def __iter__(self):
#         return self
  
#     def __next__(self): 
#         if self.num > self.end:
#             raise StopIteration
#         else:
#             self.num += 1
#             return self.num - 1
              
              
# # Driver code
# if __name__ == '__main__' :
      
#     a, b = 2, 5
      
#     c1 = Counter(a, b)
#     c2 = Counter(a, b)
      
#     # Way 1-to print the range without iter()
#     print ("Print the range without iter()")
      
#     for i in c1:
#         print ("Eating more Pizzas, couting ", i, end ="\n")
      
#     print ("\nPrint the range using iter()\n")
      
#     # Way 2- using iter()
#     obj = iter(c2)
#     try:
#         while True: # Print till error raised
#             print ("Eating more Pizzas, couting ", next(obj))
#     except: 
#         # when StopIteration raised, Print custom message
#         print ("\nDead on overfood, GAME OVER") 

# Function to check object is iterable of not
# def iterable(obj):
# 	try:
# 		iter(obj)
# 		return True
# 	except TypeError:
# 		return False

# # Driver Code
# for element in [34, [4, 5], (4, 5), {"a":4}, "dfsdf", 4.5]:
# 	print(element, " is iterable : ", iterable(element))

# A simple generator for Fibonacci Numbers
def fib(limit):
	a, b = 0, 1
	while(a < limit):
		yield a
		a, b = b, a+b

x = fib(5)

print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())

# Iterating over the generator object using for
# in loop
print("\nUsing for in loop")
for i in fib(5):
	print(i)