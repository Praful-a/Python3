""" Public modifiers """
class Geek:

	# constructor
	def __init__(self, name, age):

		# public data members
		self.geekName = name
		self.geekAge = age

	# public member function
	def displayAge(self):

		# accessing pubic data member
		print("Age: ", self.geekAge)

obj = Geek('R2J', 20)

# accessing public data member
print("Name: ", obj.geekName)

obj.displayAge()
