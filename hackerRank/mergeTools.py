def merge_the_tools(string, k):
	c = 0
	s = ''
	for i in string:
		if i not in s:
			s = s + i
		c += 1 
		if (c == k):
			print(s)
			c = 0
			s = ''

string = 'AABCAAADA'
k = 3 
merge_the_tools(string, k)