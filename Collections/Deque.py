# Python code to demonstrate deque

from collections import deque

# Declaring deque
# queue = deque(['name', 'age', 'DOB'])
# print(queue)

# append(), appendleft(), pop(), popleft()

# de = deque([1, 2, 3])

# de.append(4)
# print("The deque after appending at right is : ")
# print(de)

# de.appendleft(6)
# print("The deque after appending at left is : ")
# print(de)

# de.pop()
# print("The deque after deleting from right is : ")
# print(de)

# de.popleft()
# print("The deque after deleting from left is : ")
# print(de)

# insert(), index(), remove(), count()

# de = deque([1, 2, 3, 3, 4, 2, 4])

# print("The number 4 first occurs at a position : ")
# print(de.index(4, 2, 5))

# de.insert(4, 3)
# print("Teh deque after inserting 3 and 5th position is : ")
# print(de)

# print("The count of 3 in deque is : ")
# print(de.count(3))

# de.remove(3)

# print("The deque after deleting first occurance of 3 is : ")
# print(de)


# extend(), extendleft(), rotate(), reverse()

de = deque([1, 2, 3])

de.extend([4, 5, 6])
print("The deque after extending deque at end is : ")
print(de)

de.extendleft([7, 8, 9])

print("The deque after extending deque at begining is : ")
print(de)

de.rotate(-3)
print("The deque after rotating deque is : ")
print(de)

de.reverse()
print("The deque after reversing deque is : ")
print(de)