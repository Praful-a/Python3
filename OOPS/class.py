# creates a class named MyClass
# class MyClass:
# 	# assign the values to the MyClass attributes
# 	number = 0
# 	name = "noname"

# def Main():
# 	# Creating an object of the MyClass.
# 	#Here, 'me' is the object
# 	me = MyClass()

# 	# Accessing the attributes of MyClass
# 	# using the dot(.) operator
# 	me.number = 1377
# 	me.name = "John Wick"

# 	print(me.name + " " + str(me.number))

# if __name__ == '__main__':
# 	Main()

# Program to demonstrate working of class methods

# class Vector2D:
# 	x = 0.0
# 	y = 0.0

# 	# Creating a method named Set
# 	def Set(self, x, y):
# 		self.x = x
# 		self.y = y

# def Main():
# 	# vec is an object of class Vector2D
# 	vec = Vector2D()

# 	# Passing values to the function Set
# 	# by using dot(.) operator
# 	vec.Set(5, 6)
# 	print("X: "+ str(vec.x) + ", Y: " + str(vec.y))

# if __name__ == '__main__':
# 	Main()


# Syntax for inheritance
# class derived-classname(superclass-name)

# A Prorgramt to demonstrate working of inheritance
# class Pet:
# 	# __init__ is an constructor in Python
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# # Class Cat inheriting from class Pet
# class Cat(Pet):
# 	def __init__(self, name, age):
# 		# Calling the super-clss function __init__
# 		# using the super() function
# 		super().__init__(name, age)

# def Main():
# 	thePet = Pet("Pet", 1)
# 	jess = Cat("Jess", 3)

# 	# isinstance() function to check whether a class is
# 	# inherited from another class
# 	print("Is jess a cat? " + str(isinstance(jess, Cat)))
# 	print("Is jess a pet? " +str(isinstance(jess, Pet)))
# 	print("Is the pet a cat?" + str(isinstance(thePet, Cat)))
# 	print("Is thePet a pet?" +str(isinstance(thePet, Pet)))
# 	print(jess.name)

# if __name__ == "__main__":
# 	Main()


# Program will reverse the string that is passed to it
# from the main function
# class Reverse:
# 	def __init__(self, data):
# 		self.data = data
# 		self.index = len(data)

# 	def __iter__(self):
# 		return self

# 	def __next__(self):
# 		if self.index == 0:
# 			raise StopIteration
# 		self.index -= 1
# 		return self.data[self.index]

# def Main():
# 	rev = Reverse("Drapsicle")
# 	for char in rev:
# 		print(char, end="")
# 	print("\r")

# if __name__ == "__main__":
# 	Main()

# A Python program to demonstrate working of Generators
# def Reverse(data):
# 	for index in range(len(data)-1, -1, -1):
# 		yield data[index]

# def Main():
# 	rev = Reverse("Harssh")
# 	for char in rev:
# 		print(char)
# 	data = 'Harssh'
# 	print(list(data[i] for i in range(len(data)-1, -1, -1)))

# if __name__ == "__main__":
# 	Main()


class ThisUse:

	def __init__(self,a, b):
		ThisUse.a = a
		ThisUse.b = b

	def display(self):
		print(ThisUse.a+ThisUse.b);

obj = ThisUse(10,15)
obj.display()