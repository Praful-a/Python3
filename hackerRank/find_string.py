def count_substring(string, sub_string):
	count = 0
	ml = len(string)
	sl = len(sub_string)
	for i in range(ml-sl+1):
		if (string[i:(i+sl)] == sub_string):
			count += 1 
	return count


if __name__ == '__main__':
	string = "ABCDCDC"
	sub_string = "CDC"
	result = count_substring(string, sub_string)
	print(result)
	