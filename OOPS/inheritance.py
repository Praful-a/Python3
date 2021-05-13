# Program to demonstrate iheritance
# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "Class Person" is
# equivalent to "class Person(object)"

# class Person(object):

# 	# Constructor
# 	def __init__(self, name):
# 		self.name = name

# 	# To get name
# 	def getName(self):
# 		return self.name

# 	# To check if this person is employee
# 	def isEmployee(self):
# 		return False

# # Inherited or Sub class (Note Person in bracket)
# class Employee(Person):

# 	# Here we return true
# 	def isEmployee(self):
# 		return True

# # Driver code
# emp = Person("Geek1") # An Object of Person
# print(emp.getName(), emp.isEmployee())

# emp = Employee('Geek2') # An Object of Employee
# print(emp.getName(), emp.isEmployee())

# Program to check if a class is subclass of another
# class Base(object):
# 	pass

# class Derived(Base):
# 	pass

# # Driver Code
# print(issubclass(Derived, Base))
# print(issubclass(Base, Derived))

# d = Derived()
# b = Base()

# # b is not an instance of Derived
# print(isinstance(b, Derived))

# # But d is an instance of Base
# print(isinstance(d, Base))

# Program to show working of multiple inheritance
# class Base1(object):
# 	def __init__(self):
# 		self.str1 = "Geek1"
# 		print("Base1")

# class Base2(object):
# 	def __init__(self):
# 		self.str2 = "Geek2"
# 		print("Base2")

# class Derived(Base1, Base2):
# 	def __init__(self):

# 		# Calling constructors of Base1
# 		# and Base2 classes
# 		Base1.__init__(self)
# 		Base2.__init__(self)
# 		print("Derived")

# 	def printStrs(self):
# 		print(self.str1, self.str2)

# ob = Derived()
# ob.printStrs()

# Python example to show that base 
# class memeber can be accessed in derived class
# using base class name
# class Base(object):

# 	# Constructor
# 	def __init__(self, x):
# 		self.x = x

# class Derived(Base):

# 	# Constructor
# 	def __init__(self, x, y):
# 		Base.x = x
# 		self.y = y

# 	def printXY(self):
# 		print(Base.x, self.y)

# # Driver code
# d = Derived(10, 20)
# d.printXY()

# Class members can be accessed in derived class
# using super()
# class Base(object):

# 	# Constructor
# 	def __init__(self, x):
# 		self.x = x

# class Derived(Base):

# 	# Constructor
# 	def __init__(self, x, y):
# 		'''super(Derived, self).__init__(x)
# 		and below line are same'''
# 		super().__init__(x)
# 		self.y = y

# 	def printXY(self):
# 		print(self.x, self.y)

# # Driver Code
# d = Derived(10, 20)
# d.printXY()

# Predict the output of following programs

# class X(object):
# 	def __init__(self, a):
# 		self.num = a

# 	def doubleup(self):
# 		self.num *= 2

# class Y(X):
# 	def __init__(self, a):
# 		X.__init__(self, a)

# 	def tripleup(self):
# 		self.num *= 3

# obj = Y(4)
# print(obj.num)

# obj.doubleup()
# print(obj.num)

# obj.tripleup()
# print(obj.num)

# 2. Base or Super class

class Person(object):
	def __init__(self, name):
		self.name = name

	def getName(self):
		return self.name

	def isEmployee(self):
		return False

# Inherited or Subclass (Note Person in bracket)
class Employee(Person):
	def __init__(self, name, eid):

		super().__init__(name)
		self.empId = eid

	def isEmployee(self):
		return True

	def getId(self):
		return self.empId

emp = Employee("Geek1", "E101")
print(emp.getName(), emp.isEmployee(), emp.getId())