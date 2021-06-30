def solve(s):
	return " ".join([i.capitalize() for i in s.split()])

if __name__ == '__main__':
	s = "q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M"
	result = solve(s)
	print(result)