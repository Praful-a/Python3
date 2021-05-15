# Program to demonstrate userlist

from collections import UserList 

# L = [1, 2, 3, 4]

# # Creating a userList
# userL = UserList(L)
# print(userL.data)

# # Creating empty userlist
# userL = UserList()
# print(userL.data)

# Example 2

class MyList(UserList):

	def remove(self, s = None):
		raise RuntimeError("Deletion not allowed")

	def pop(self, s = None):
		raise RuntimeError("Deletion not allowed")

L = MyList([1, 2, 3, 4])

print("Original List")

L.append(5)
print("After Insertion")
print(L)

L.remove()