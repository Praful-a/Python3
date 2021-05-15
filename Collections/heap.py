# heapify(), heappush() and heappop()

import heapq

# li = [5, 6, 9, 1, 3]

# heapq.heapify(li)

# print("The created heap is : ", end="")
# print(li)

# heapq.heappush(li, 4)
# print("The modified heap after push is : ", end="")
# print(list(li))

# print("The popped and smallest element is : ", end="")
# print(heapq.heappop(li))


# heappushpop() and heappreplace()

# li1 = [5, 7, 9, 4, 3]

# li2 = [5, 7, 9, 4, 3]

# heapq.heapify(li1)
# heapq.heapify(li2)

# print("The popped item using heappushpop() is : ", end="")
# print(heapq.heappushpop(li1, 2))

# print("The popped item using heapreplace() is : ", end="")
# print(heapq.heapreplace(li2, 2))

li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]

heapq.heapify(li1)

print("The 3 largest numbers in list are : ", end="")
print(heapq.nlargest(2, li1))

print("The 3 smallest numbers in list are : ", end="")
print(heapq.nsmallest(3, li1))
