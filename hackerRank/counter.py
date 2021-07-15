from collections import Counter
if __name__ == '__main__':
	x = int(input())
	l = list(map(int, input().split()))
	counter = Counter(l)
	print(counter)
	N = int(input())
	s = 0	
	for _ in range(N):
		n, p = input().split()
		num = int(n)
		price = int(p)
		if counter[num]:
			counter[num] -= 1 
			s = s + price
	print(s)