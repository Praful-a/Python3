from itertools import combinations_with_replacement
s = 'HACK'
k = 2
l = list(combinations_with_replacement(s, k))
l2 = []
for i in l:
	m = sorted(i, key=lambda x : x)
	l2.append(m)
l2.sort(key=lambda x : x)
for j in l2:
	print(''.join(j))