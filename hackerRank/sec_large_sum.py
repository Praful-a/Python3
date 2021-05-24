import os
import sys
def even_odd_index_no(li, size):
	li2 = []
	li3 = []
	if(size <= 3):
		return 0
	for x in range(size):
		if x % 2 == 0:
			li2.append(li[x])
		else:
			li3.append(li[x])
	li4 = [li2, li3]
	s = 0
	for l in li4:
		m = l[0]
		second_large = l[1]
		for i in range(len(l)):
			if(l[i] > m):
				second_large = m
				m = l[i]
			elif l[i] > second_large and m != l[i]:
				second_large = l[i]
		s += second_large
	print(s)


if __name__ == '__main__':
	size = int(input())
	lst = list(map(int, input().rstrip().split()))

	even_odd_index_no(lst, size)


