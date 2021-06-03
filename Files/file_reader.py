# with open('pi_digits.txt') as file_object:
# 	contents = file_object.read()
# 	# print(contents)
# 	print(contents.rstrip())


# Reading line by line
# filename = 'pi_digits.txt'

# with open(filename) as file_object:
# 	for line in file_object:
# 		# print(line)
# 		print(line.rstrip())

# Making a list of lines from a file
# with open(filename) as file_object:
# 	lines = file_object.readlines()

# print(lines)
# for line in lines:
# 	print(line.rstrip())

# Working with file's contents
# pi_string = ''
# for line in lines:
	# pi_string += line.rstrip()
	# pi_string += line

# print(pi_string)
# print(len(pi_string))

# f = open('pi_digits.txt', 'r')
# print(f.name) # name of file
# print(f.mode)
# f.close()  # closing the file

# with open('pi_digits.txt', 'r') as f:
# 	print(f.mode)

# print(f.closed) # this will return True if file closed


# with open('pi_digits.txt', 'r') as f:
	# f_contents = f.read()
	# f_contents = f.readlines()

	# for line in f:
		# print(line, end="")
	# f_contents = f.readline()
	# print(f_contents, end='')

	# f_contents = f.readline()
	# print(f_contents, end='')

	# f_contents = f.read(100) # it will read 100 lines from file
	# print(f_contents, end='')

	# f_contents = f.read(100)
	# print(f_contents, end='')

	# size_to_read = 10

	# f_contents = f.read(size_to_read)
	# print(f_contents, end='')

	# f.seek(0)

	# f_contents = f.read(size_to_read)
	# print(f_contents, end='')

	
	# while len(f_contents) > 0:
	# 	print(f_contents, end='*')
	# 	f_contents = f.read(size_to_read)		


# with open('test2.txt', 'w') as f:
# 	f.write('Test')
# 	f.seek(0)
# 	f.write('R')

with open('test2.txt', 'r') as rf:
	with open('test_copy.txt', 'w') as wf:
		for line in rf:
			wf.write(line)
