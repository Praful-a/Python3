# Iterables
# nums = [1, 2, 3]
# for num in nums:
# 	print(num)

# Iterables
# nums = [1, 2, 3, 4]
# i_nums = nums.__iter__()
# print(i_nums)
# print(i_nums.__next__())
# print(i_nums.__next__())
# print(i_nums.__next__())
# print(i_nums.__next__())
# print(i_nums.__next__())
# while True:
# 	try:
# 		print(i_nums.__next__())
# 	except StopIteration:
# 		break 

# Second way 
# nums = [1, 2, 3, 4]
# i_nums = iter(nums)
# print(i_nums)
# for num in i_nums:
# 	print(num)


# Own Iterator class 
class MyRange:

	def __init__(self, start, end):
		self.value = start  
		self.end = end   

	def __iter__(self):
		return self   

	def __next__(self):
		if self.value >= self.end:
			raise StopIteration 
		current = self.value 
		self. value += 1 
		return current 

def my_range(start, end):
	current = start 
	while current < end:
		yield current
		current += 1

# nums = MyRange(1, 10)
# print(nums)
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))
# for num in nums:
# 	print(num)

nums = my_range(1, 10)
print(nums)
for num in nums:
	print(num)