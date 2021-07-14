from collections import Counter
l = [2, 3, 4, 5, 6, 8, 6, 5, 18]
counter = Counter(l)
print(counter)
c = 0
s = 0	
for _ in range(6):
	n, p = input().split()
	num = int(n)
	price = int(p)
	if num in counter:
		c += 1
		if (c != counter[num]):
			s += price 
		else:
			s += 0		 
print(s)