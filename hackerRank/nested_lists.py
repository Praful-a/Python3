# if __name__ == '__main__':
# 	li = []
# 	for _ in range(int(input())):
# 		name = input()
# 		score = float(input())
# 		li.append([name, score])
	
	
# 	print(sort)

li = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
li.sort(key = lambda x : x[1])
li.sort(key = lambda x : x)
m = li[0][1]
second = li[1][1]
for i in range(len(li)):	
	if (li[i][1] > m):
		m = li[i][1]
		second = m
	elif (li[i][1] > second):
		second = li[i][1]

print(second)