# Program to demonstrate working of yield

# A generator function that yields 1 for the first time,
# 2 second time and 3 third time
# def generator():
# 	yield 1 
# 	yield 2 
# 	yield 3

# Driver code to check above generator function
# for value in generator():
# 	print(value)

# We can also call function to print
# print(generator()) # This will return a generator object

# if we use print(generator().__next__()) every time this 
# will print same value not change it 

# a = generator()
# print(a.__next__()) # We have to use to iterate it
# print(a.__next__())
# print(a.__next__())
# print(a.__next__()) # Stop iteration error

# Program to generate squares from 1 to 100 using 
# yield and therefore generator

# An infinite generator function that prints next square
# number. It starts with 1
def nextSquare():
	i = 1;

	# An Inifinite loop to generate squares
	while True:
		yield i*i
		i += 1 # Next execution resumes
				# from this point

# Driver code to test above generator
# function
for num in nextSquare():
	if num > 100:
		break
	print(num) 