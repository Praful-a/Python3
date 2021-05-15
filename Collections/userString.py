# Python program to demonstrate string

# Creating a String
# with single Quotes
# String1 = 'Welcome to the Geeks World'
# print("String with the use of Single Quotes: ")
# print(String1)

# # Creating a String 
# # with double Quotes
# String1 = "I'm a Geek"
# print("\nString with the use of Double Quotes: ")
# print(String1)

# UserString

from collections import UserString

# d = 12344

# userS = UserString(d)
# print(userS.data)

# userS = UserString("")
# print(userS.data)

class Mystring(UserString):

	def append(self, s):
		self.data += s

	def remove(self, s):
		self.data = self.data.replace(s, "")

s1 = Mystring("Geeks")
print("Original String:", s1.data)

s1.append('s')
print("String After Appending:", s1.data)

s1.remove("e")
print("String after Removing:", s1.data)