# Write Python code here
# class sampleClass:
# 	count = 0  # class attribute

# 	def increase(self):
# 		sampleClass.count += 1

# # Calling increase() on an object
# s1 = sampleClass()
# s1.increase()
# print(s1.count)

# # Calling increase on one more
# # object
# s2 = sampleClass()
# s2.increase()
# print(s2.count)

# print(sampleClass.count)

# Program to demonstrate
# instance attributes.

# class emp:
#     def __init__(self):
#         self.name = 'xyz'
#         self.salary = 4000
  
#     def show(self):
#         print(self.name)
#         print(self.salary)
  
# e1 = emp()
# print("Dictionary form :", vars(e1))
# print(dir(e1))


# Python program to illustrate reflection
# def reverse(sequence):
# 	sequence_type = type(sequence)
# 	empty_sequence = sequence_type()

# 	if sequence == empty_sequence:
# 		return empty_sequence

# 	rest = reverse(sequence[1:])
# 	first_sequence = sequence[0:1]

# 	# Combine the result
# 	final_result = rest + first_sequence

# 	return final_result

# # Driver code
# print(reverse([10, 20, 30, 40]))
# print(reverse("GeeksForGeeks"))

# x = 5

# def testFunction():
# 	print("Test")

# y = testFunction

# if(callable(x)):
# 	print("x is callable")
# else:
# 	print('x is not callable')

# if(callable(y)):
# 	print('y is callable')
# else:
# 	print('y is not callable')

class Employee:
	salary = 25000
	company_name = "GeeksForGeeks"

employee = Employee()
print("The salary is:", getattr(employee, "salary"))
print('The salary is:', employee.salary)
