if __name__ == '__main__':
	n = int(input()) 
	if n % 2 != 0:
		print("Weird")
	elif (n % 2 == 0):
		if (n >= 2 or n <= 5):
			print("Not Weird")
		elif (n >= 6 or n <= 20):
			print("Weird")
		else:
			print("Not Weird")
