# # Program to illustrate working of And gate

# def AND(a, b):

# 	if a == 1 and b == 1:
# 		return True
# 	else:
# 		return False

# # Driver code
# if __name__ == "__main__":
# 	print(AND(1, 1))

# 	print("+====================+================+")
# 	print("|   AND Truth Table    |         Result    |")
# 	print("| A = False, B = False | A AND B = ", AND(False, False), " | ")
# 	print("| A = False, B = True  | A AND B = ", AND(False, True), " | ")
# 	print("| A = True, B = False  | A AND B = ", AND(True, False), " | ")
# 	print("| A = True, B = True   | A AND B = ", AND(True, True), "  | ")



# Program to illustrate working of And gate

# def NAND(a, b):

# 	if a == 1 and b == 1:
# 		return False
# 	else:
# 		return True

# # Driver code
# if __name__ == "__main__":
# 	print(NAND(1, 1))

# 	print("+====================+================+")
# 	print("|   NAND Truth Table   |         Result    |")
# 	print("| A = False, B = False | A NAND B = ", NAND(False, False), " | ")
# 	print("| A = False, B = True  | A NAND B = ", NAND(False, True), " | ")
# 	print("| A = True, B = False  | A NAND B = ", NAND(True, False), " | ")
# 	print("| A = True, B = True   | A NAND B = ", NAND(True, True), "| ")


# Program to illustrate working of And gate

# def OR(a, b):

# 	if a == 1 or b == 1:
# 		return True
# 	else:
# 		return False

# # Driver code
# if __name__ == "__main__":
# 	print(OR(1, 1))

# 	print("+====================+================+")
# 	print("|    OR Truth Table    |         Result   |")
# 	print("| A = False, B = False | A  OR B = ",  OR(False, False), "| ")
# 	print("| A = False, B = True  | A  OR B = ",  OR(False, True), " | ")
# 	print("| A = True, B = False  | A  OR B = ",  OR(True, False), " | ")
# 	print("| A = True, B = True   | A  OR B = ",  OR(True, True), " | ")


# Program to illustrate working of And gate

# def XOR(a, b):

# 	if a != b:
# 		return 1
# 	else:
# 		return 0

# # Driver code
# if __name__ == "__main__":
# 	print(XOR(5, 5))

# 	print("+====================+================+")
# 	print("|   XOR Truth Table    |         Result|")
# 	print("| A = False, B = False | A XOR B = ", XOR(False, False), " | ")
# 	print("| A = False, B = True  | A XOR B = ", XOR(False, True), " | ")
# 	print("| A = True, B = False  | A XOR B = ", XOR(True, False), " | ")
# 	print("| A = True, B = True   | A XOR B = ", XOR(True, True), " | ")


# Program to illustrate working of And gate

# def NOT(a):
# 	return not a

# # Driver code
# if __name__ == "__main__":
# 	print(NOT(1))

# 	print("+====================+================+")
# 	print("|   NOT Truth Table    |         Result  |")
# 	print("| A = False            | NOT A = ", NOT(False), "  | ")
# 	print("| A = True             |  NOT A = ", NOT(True), "| ")
# 	

# Program to illustrate working of And gate

# def NOR(a, b):

# 	if a == 0 and b == 0:
# 		return 1
# 	else:
# 		return 0

# # Driver code
# if __name__ == "__main__":
# 	print(NOR(1, 1))

# 	print("+====================+================+")
# 	print("|   NOR Truth Table    |         Result|")
# 	print("| A = False, B = False | A NOR B = ", NOR(False, False), " | ")
# 	print("| A = False, B = True  | A NOR B = ", NOR(False, True), " | ")
# 	print("| A = True, B = False  | A NOR B = ", NOR(True, False), " | ")
# 	print("| A = True, B = True   | A NOR B = ", NOR(True, True), " | ")


def XNOR(a, b):

	if a == b:
		return 1
	else:
		return 0

# Driver code
if __name__ == "__main__":
	print(XNOR(1, 1))

	print("+====================+================+")
	print("|   XNOR Truth Table   |         Result |")
	print("| A = False, B = False | A XNOR B = ", XNOR(False, False), " | ")
	print("| A = False, B = True  | A XNOR B = ", XNOR(False, True), " | ")
	print("| A = True, B = False  | A XNOR B = ", XNOR(True, False), " | ")
	print("| A = True, B = True   | A XNOR B = ", XNOR(True, True), " | ")