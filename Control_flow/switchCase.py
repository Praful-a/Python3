# function to convert number into string
# Switcher is dictionary data type here

def number_to_strings(argument):
	Switcher = {
		0: "Zero",
		1: "one",
		2: "two",
	}
	# get() method of dictionary data type returns
	# value of passed argument if it is present
	# in dictionary otherwise second argument will
	# be assigned as default value of passed argument
	return Switcher.get(argument, "nothing")

# Driver program
if __name__ == "__main__":
	argument = 3
	print(number_to_strings(argument))
