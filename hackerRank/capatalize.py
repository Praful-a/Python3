def solve(s):
	str = s.split()
	return " ".join([i.capitalize() for i in str])

if __name__ == '__main__':
	s = "chris alan lol"
	result = solve(s)
	print(result)