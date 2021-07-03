# program to illustrate access modifiers of a class


class Super:

	# public data member
	var1 = None

	# protected data member
	_var2 = None 

	# private data member
	_var3 = None

	# constructor
	def __init__(self, var1, var2, var3):
		self.var1 = var1
		self._var2 = var2
		self.__var3 = var3


	# public member function
	def displayPublicMembers(self):
		print("Public Data Member:", self.var1)

	# protected member function
	def _displayProtected(self):
		print("Protected Data Member:", self._var2)

	# private member function
	def __displayPrivate(self):
		print("Private Data Member:", self.__var3)

	def accessPrivateMembers(self):
		self.__displayPrivate()

class Sub(Super):

	# constructor
	def __init__(self, var1, var2, var3):
		Super.__init__(self, var1, var2, var3)

	def accessProtectedMembers(self):
		self._displayProtected()

obj = Sub("Geeks", 4, "Geeks !!")

obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()

print("Object is accessing protected member:", obj._var2)