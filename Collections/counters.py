# A program to show different ways to create counter
from collections import Counter

# # With sequence of items
# print(Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C']))

# # with dictionary
# print(Counter({'A':3, 'B': 5, 'C': 2}))

# # with keyword arguments
# print(Counter(A=3, B=5, C=2))

# coun = Counter()

# coun.update([1, 2, 3, 1, 2, 1, 1, 2])
# print(coun)

# coun.update([1, 2, 4])
# print(coun)

# c1 = Counter(A=4, B=3, C=10)
# c2 = Counter(A=10, B=3, C=4)

# c1.subtract(c2)
# print(c1)

# A Program where different list items are counted
# using counter
z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']

print(Counter(z))