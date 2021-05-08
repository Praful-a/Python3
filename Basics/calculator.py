"""Program for making calculator"""

def add(n1, n2):
	return n1 + n2

def sub(n1, n2):
	return n1 - n2

def mul(n1, n2):
	return n1 * n2

def div(n1, n2):
	return n1 / n2


print("Please select operation -\n \
	   1. Add\n \
	   2. Subtraction\n \
	   3. Multiply\n \
	   4. Divide\n")
select = int(input("Enter your choice: "))

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

if select == 1:
	print("The addition : ", add(num_1, num_2))
elif select == 2:
	print("The Subtraction : ", sub(num_1, num_2))
elif select == 3: 
	print("The Multipliction : ", mul(num_1, num_2))
elif select == 4:
	print("The division : ", div(num_1, num_2))
else:
	print("Invalid Input .. ")