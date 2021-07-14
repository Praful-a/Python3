from collections import Counter
def sum_of_price(l2, counter):
	sum = 0
	c = 0
	for i in l2:

		sum += i[1]
	return sum


if __name__ == '__main__':
	n = int(input())
	sizes = list(map(int, input().strip().split()))
	c = Counter(sizes)
	size = int(input())
	l2 = []
	for _ in range(size):
		s = list(map(int, input().strip().split()))
		l2.append(s)
	result = sum_of_price(l2, c)
	print(result)
	print(sizes)
	print(l2)
	