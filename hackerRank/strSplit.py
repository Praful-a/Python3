def split_and_join(line):
	return "-".join(line.split())


if __name__ == "__main__":
	line = "this is a string"
	result = split_and_join(line)
	print(result)