import copy

# lst1 = [1, 2, [3, 6], 5]

# # using copy for deep copy
# lst2 = copy.deepcopy(lst1)

# print("The original elements before deep copying")
# for i in range(0, len(lst1)):
# 	print(lst1[i], end=" ")
# print("\r");

# lst2[2][0] = 7

# print("The new list of elements after deep copying ")
# for i in range(0, len(lst1)):
# 	print(lst2[i], end=" ")
# print("\r");

# print("The original elements after deep copying")
# for i in range(0, len(lst1)):
# 	print(lst1[i], end=" ");


# lst1 = [1, 2, [3, 6], 5]

# # using copy for deep copy
# lst2 = copy.copy(lst1)

# print("The original elements before shallow copying")
# for i in range(0, len(lst1)):
# 	print(lst1[i], end=" ")
# print("\r");

# lst2[2][0] = 7

# print("The new list of elements after shallow copying ")
# for i in range(0, len(lst1)):
# 	print(lst2[i], end=" ")
# print("\r");

# print("The original elements after shallow copying")
# for i in range(0, len(lst1)):
# 	print(lst1[i], end=" ");

lst1 = [1, 2, [3, 6], 5]

# using copy for deep copy
lst2 = lst1

print("The original elements before '=' copying")
for i in range(0, len(lst1)):
	print(lst1[i], end=" ")
print("\r");

lst2[2][0] = 7

print("The new list of elements after '=' copying ")
for i in range(0, len(lst1)):
	print(lst2[i], end=" ")
print("\r");

print("The original elements after '=' copying")
for i in range(0, len(lst1)):
	print(lst1[i], end=" ");
