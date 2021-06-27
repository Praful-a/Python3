def mutate_string(string, position, character):
	return string[:position] + character + string[position:]

if __name__ == "__main__":
	s = "abracdabra"
	i, c = 5, 'k'
	s_new = mutate_string(s, i, c)
	print(s_new)