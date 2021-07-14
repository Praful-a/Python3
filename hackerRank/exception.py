if __name__ == '__main__':
	T = int(input())
	l = []
	l2 = []
	for _ in range(T):
		a, b = input().split()
		try:
			c = int(a)//int(b)
			l2.append(c)
		except ZeroDivisionError as e:
			l.append(e)
		except ValueError as a:
			l.append(a)
	for i in l:
		print('Error Code:', i)
	for j in l2:
		print(j)