m = 7
n = 21

for i in range(m):
	for j in range(n):
		if (j == n // 2):
			print("|", end="")
		else:
			print('-', end="")
	print()