# Function to demonstrate printing pattern
# def pypart(n):

# 	for i in range(0, n):
# 		for j in range(0, i+1):
# 			print("* ", end="")
# 		print("\r")

# n = 5
# pypart(n)

# def pypart2(n):

# 	k = 2*n - 2

# 	for i in range(0, n):
# 		for j in range(0, k):
# 			print(end=" ")
# 		k = k - 2

# 		for j in range(0, i+1):
# 			print("* ", end="")
# 		print("\r")
		 
# n = 5
# pypart2(n)

# def triangle(n):

# 	k = n - 1

# 	for i in range(0, n):
# 		for j in range(0, k):
# 			print(end=" ")
# 		k = k - 1

# 		for j in range(0, i+1):
# 			print("* ", end="")
# 		print()
# n = 5
# triangle(n)

# Number pattern

# def numpat(n):

# 	for i in range(1, n+1):

# 		for j in range(1, i+1):

# 			print(j, end=" ")
			
# 		print()

# n = 5
# numpat(n)

# Numbers without reassigning
# def contnum(n):
# 	num = 1
# 	for i in range(1, n+1):
# 		for j in range(1, i+1):
# 			print(num, end=" ")
# 			num = num + 1
# 		print("\r")

# n = 5
# contnum(n)


# Character Pattern

# def alphapat(n):

# 	num = 65
# 	for i in range(1, n+1):
# 		for j in range(1, i+1):
# 			# explicitely converting to char
# 			ch = chr(num)
# 			print(ch, end=" ")
# 		num = num + 1
# 		print("\r")

# n = 5
# alphapat(n)

# Continuous Character pattern

# def contalpha(n):

# 	num = 65
# 	for i in range(0, n):
# 		for j in range(0, i+1):
# 			ch = chr(num)
# 			print(ch, end=" ")
# 			num += 1
# 		print("\r")

# n = 5
# contalpha(n)

## Printing patterns using single loops

def pypat(n):

	for i in range(0, n+1):
		print("* "*i, end="\n")

n = 5
pypat(n)