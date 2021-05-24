
def isprime(n):
	for i in range(2, n//2):
		if (n%i == 0):
			break
	return 1

def prime(l, r):
	li = []
	prime = []
	sub = 0
	flag = 0
	for n in range(l, r+1):
		if n > 1:
			for i in range(2, n):
				if(n % i) == 0:
					flag = 1
					break
			else:
				li.append(n)
	for x in li:
		if(isprime(x) == 1):
			prime.append(x)
	print(prime[-1] - prime[0])	

if __name__ == '__main__':
	n = 2
	n2 = 7
	prime(n, n2)

