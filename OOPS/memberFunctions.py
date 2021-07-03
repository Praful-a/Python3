# class PostalAddress:
# 	pass 

# cP1 = PostalAddress()
# # Create an Instance for person ABC
# cP1.name = "ABC"
# cP1.street = "Central Street - 1"

# # Create an Instance for person DEF
# cP2 = PostalAddress()
# cP2.name = "DEF"
# cP2.street = "Central Street - 2"

# print(cP1.__dict__)
# print(cP2.__dict__)

# class PostalAddress:
# 	name = None 
# 	street = None

# obj1 = PostalAddress()
# obj1.name = "ABC"
# obj1.street = "Central Street - 1"

# obj2 = PostalAddress()
# obj2.name = "DEF"
# obj2.street = "Central Street - 2"

# print(obj1.__dict__)
# print(obj2.__dict__)
# print(obj1.__dict__['name'])
# print(obj2.__dict__['street'])

# __init__ member function 
# class PostalAddress:
# 	def __init__(self):
# 		self.name = "ABC"
# 		self.street = "Central Street - 1"

# cP1 = PostalAddress()
# print(cP1.__dict__)


# Adding functions to the class
# class PostalAddress:
# 	def __init__(self):
# 		self.name = "ABC"
# 		self.street = "Central Street - 1"

# 	def prnInfo(self):
# 		print("Name => ", self.name, " Street =>", self.street)

# cP1 = PostalAddress()
# cP1.prnInfo()

# class PostalAddress:
# 	def __init__(self, name="Default Name", street="Central Street - 1"):
# 		self.name = name
# 		self.street = street

# cP0 = PostalAddress()
# cP1 = PostalAddress("ABC")
# cP2 = PostalAddress("DEF", "Central Street - 2")

# print(cP0.name)
# print(cP1.name)
# print(cP2.name)

# creating instance variable with functions

# class PostalAddress:
# 	def __init__(self, name = 'Default Name', street = 'Central Street - 1'):
# 		self.name = name
# 		self.street = street

# 	def createMember(self):
# 		self.newMember = "temporary Value"

# cP0 = PostalAddress()
# print(cP0.__dict__)

# cP0.createMember()
# print(cP0.__dict__)


class PostalAddress:
	def __init__(self, name="Default Name", street = "Central Street - 1"):
		self.name = name
		self.street = street
		self.postalcode = 12345

cP0 = PostalAddress()
print(cP0.__dict__)

cP1 = PostalAddress("ABC")
print(cP1.__dict__)
