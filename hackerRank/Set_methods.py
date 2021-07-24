if __name__ == '__main__':
	n = int(input())
	s = set(map(int, input().split()))
	N = int(input())
	for _ in range(N):
		name = input().split()
		if name[0] == 'pop':
			s.pop()
		elif name[0] == 'remove':
			s.remove(int(name[1]))
		elif name[0] == 'discard':
			s.discard(int(name[1]))
	print(s)
