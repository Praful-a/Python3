from itertools import combinations
if __name__ == '__main__':
	s, k = input().split()
	l = []
	l3 = []
	for m in range(1, int(k)+1):
		l2 = list(combinations(s, m))
		for i in l2:
			l.append(i)
	for i in l:
		s = sorted(i, key=lambda x:x)
		l3.append(s)
	l3.sort(key=lambda x:x)
	sorted_list = sorted(l3, key=len)
	for j in sorted_list:
		print(''.join(j))