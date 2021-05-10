# for i in range(1, 4):
# 	print(i)
# else: # Executed because no break in for
# 	print("No Break")

# Else block is Not executed in below example
# for i in range(1, 4):
# 	print(i)
# 	break
# else: # Not executed as there is a break
# 	print("No Break")

# Program to check even numbers in array
def contains_even_no(l):
	for ele in l:
		if ele % 2 == 0:
			print("List contains an even number")
			break
	# This else executes only if break is Never
	# reached and loop terminated after all iterations.
	else:
		print("list does not contain an even number")

# Driver code
print("For List 1:")
contains_even_no([1, 9, 8])
print("\n For list 2:")
contains_even_no([1, 3, 5])

# Pridict the output
count = 0
while (count < 1):    
    count = count+1
    print(count)
    break
else:
    print("No Break")