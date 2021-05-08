# basic method of input output input N
# n = int(raw_input())

# # input the array
# arr = [int(x) for x in raw_input().split()]

# # initialize variable
# summation = 0

# # calculate sum
# for x in arr:
# 	summation += x

# # print answer
# print(summation)

# import inbuilt standard input output
from sys import stdin, stdout

# suppose a function called main() and all
# the operations are performed
# def main():

# 	# array input similar method
# 	arr = [int(x) for x in stdin.readline().split()]

# 	# initialize variable
# 	summation = 0

# 	# calculate sum
# 	for x in arr:
# 		summation += x

# 	# could use inbuilt summation = sum(arr)

# 	# print answer via write
# 	# write method writes only
# 	# string operations
# 	# so we need to convert any data into string for input
# 	stdout.write(str(summation))

# # call the main method
# if __name__ == "__main__":
# 	main()

# import sys

# def get_ints():
# 	return map(int, sys.stdin.readline().strip().split())

# a, b, c, d = get_ints()
# print("First value : ", a)
# print("Second value : ", b)
# print("Third value : ", c)
# print("Forth value : ", d)

# import sys

# def get_ints():
# 	return list(map(int, sys.stdin.readline().strip().split()))

# arr = get_ints()
# print(arr)

