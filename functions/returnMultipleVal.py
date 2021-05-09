#Program to return values from a method using class

# class Test:
# 	def __init__(self):
# 		self.str = "geeksforgeeks"
# 		self.x = 20

# # This function returns an object of Test
# def fun():
# 	return Test()

# # Driver code to test above method
# t = fun()
# print(t.str)
# print(t.x)

# Program to return multiple values form a method using 
# tuple

# def fun():
# 	str = "geeksforgeeks"
# 	x = 20
# 	return str, x; # Return tuple, we could also
# 					# write(str, x)

# # Driver code test above method
# x = fun() 
# # print(str)
# print(x)

# Multiple values from a method using list

# def fun():
# 	str = 'geeksforgeeks'
# 	x = 20
# 	return [str, x]

# list = fun()
# print(list)

# Multiple values from a method using dictionary
# def fun():
# 	d = dict();
# 	d['str'] = "geeksforgeeks"
# 	d['x'] = 20
# 	return d

# # Driver code to test above method
# d = fun()
# print(d)

from dataclasses import dataclass

@dataclass
class Book_list:
	name: str
	perunit_cost: float
	quantity_available: int = 0

	# function to calculate total cost
	def total_cost(self) -> float:
		return self.perunit_cost * self.quantity_available

book = Book_list("Introduction to programming.", 300, 3)
x = book.total_cost()

# print the total cost of the book
print(x)

# print book details
print(book)

# 900
print(Book_list(name='Python programming',
			perunit_cost = 200,
			quantity_available = 3))