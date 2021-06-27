n = 5
arr = [2, 3, 6, 6, 5]
lst = list(set(arr))
m = lst[0]
sec = lst[1]
for i in range(n):
	if(arr[i] > m):
		sec = m	
		m = arr[i]
	elif(arr[i] > sec and arr[i] < m):
		sec = arr[i]

print(sec)