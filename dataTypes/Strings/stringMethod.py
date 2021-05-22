# Program to demonstrate the use of isdecimal()

# s = "12345"
# print(s.isdecimal())

# # contains alphabest
# s = "12geeks34"
# print(s.isdecimal())

# s = "12 34"
# print(s.isdecimal())

# isalnum() method

# string = "abc123"
# print(string.isalnum())

# string = "abc 124"
# print(string.isalnum())

# istitle() method
# s = 'Geeks For Geeks'
# print(s.istitle())

# s = 'geeks For Geeks'
# print(s.istitle())

# s = 'Geeks For GEEKs'
# print(s.istitle())

# s = '6041 Is My Number'
# print(s.istitle())

# s = 'GEEKS'
# print(s.istitle())

# Code 2
# s = "I Love Geeks For Geeks"
# if s.istitle() == True:
# 	print('Titlecased String')
# else:
# 	print("Not a Titlecased String")

# s = "I Love geeks for geeks"
# if s.istitle() == True:
# 	print('Titlecased String')
# else:
# 	print('Not a Titlecased String')

# String partition()

# string = "pawan is a good"
# print(string.partition('is '))

# # 'not' seperator is not found
# print(string.partition('bad '))

# string = 'pawan is a good, isn\'t it'
# print(string.partition('is'))

# Code 2
# string = "python is a good language"

# print(string.partition('is '))

# print(string.partition('bad '))

# string = 'geeks is a good, isn\'t it'
# print(string.partition('is'))


# Code to illustrate the working of isidentifier()
# string = "Geeks for Geeks"
# print(string.isidentifier())

# # A Perfect identifier
# string = "GeeksforGeeks"
# print(string.isidentifier())

# string = "Geeks0for0Geeks"
# print(string.isidentifier())

# # Beginning with an integer
# string = "54Geeks0for0Geeks"
# print(string.isidentifier())

# Program to demonstrate the use or len() method
# string = 'geeks'
# print(len(string))

# string = 'geeks for geeks'
# print(len(string))

# Code to demonstrate working of rindex()
# text = "geeks for geeks"

# result = text.rindex('geeks')
# print("Substring 'geeks':", result)

# quote = "geeks for geeks"
# print(quote.rindex('ge', 2, 13))

# print(quote.rindex('geeks', 0, 16))

# Program to demonstrate the use of max() function

# maximum alphabetical character in "geeks"
# string = "geeks"
# print(max(string))
# print(min(string))
# string = "Python"
# print(max(string))
# print(min(string))

# Code to illustrate splitlines()
# string = "Welcome everyone to\rth world of Geeks\nGeeksforGeeks"

# print(string.splitlines())
# print(string.splitlines(0))
# # True has been passed
# print(string.splitlines(True))

# Code 2
# string = "Cat\nBat\nSat\nMat\nXat\nEat"
# # No parameters has been passed
# print(string.splitlines())
# print("India\nJapan\nUSA\nUK\nCanada\n".splitlines())

# Practical Application
def Cal_len(string):
	li = string.splitlines()
	print(li)

	l = [len(ele) for ele in li]
	return l

# Driver Code
string = "Welcome\rto\rGeeksforGeeks"
print(Cal_len(string))