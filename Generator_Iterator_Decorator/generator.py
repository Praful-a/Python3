# Iteration
# def square_numbers(nums):
# 	result = []
# 	for i in nums:
# 		result.append(i*i)
# 	return result 

# my_nums = square_numbers([1, 2, 3, 4, 5])
# print(my_nums)

# Generators 
# def square_numbers(nums):
# 	for i in nums:
# 		yield (i*i) 

# my_nums = square_numbers([1, 2, 3, 4, 5])
# print(my_nums)
# while True:
# 	try:
# 		print(next(my_nums))
# 	except StopIteration:
# 		break 

# second way to use generators
my_nums = (x*x for x in [1, 2, 3, 4, 5])
print(my_nums)

for num in my_nums:
	print(num)