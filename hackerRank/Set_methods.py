n = int(input())
s = set(map(int, input().split()))
terms = int(input())
for _ in range(terms):
    comm = input().split()
    for i in range(1, len(comm)):
        comm[i] = int(comm[i])
    if comm[0] == 'pop':
        s.pop()
    if comm[0] == 'remove':
        s.remove(int(comm[1]))
    if comm[0] == 'discard':
        s.discard(comm[1])
sum = 0
for i in s:
    sum += i
if i:
    print(sum)
else:
    print(sum)
