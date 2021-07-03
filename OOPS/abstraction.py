# from abc import ABC
# class Type_shape():
# 	def area(self):
# 		# abstract method
# 		pass

# class Rectangle(Type_shape):
# 	length = 6
# 	breadth = 4 
# 	def area(self):
# 		return self.length * self.breadth

# class Circle(Type_shape):
# 	radius = 7
# 	def area(self):
# 		return 3.14 * self.radius * self.radius

# class Square(Type_shape):
# 	length = 4
# 	def area(self):
# 		return self.length*self.length

# class Triangle:
# 	length = 5
# 	width = 4 
# 	def area(self):
# 		return 0.5 * self.length * self.width

# r = Rectangle()
# c = Circle()
# s = Square()
# t = Triangle()
# print("Area of Rectangle:", r.area())
# print("Area of a circle:", c.area())
# print("Area of a square:", s.area())
# print("Area of a Triangle:", t.area())


# class Robot:
# 	def __init__(self, name = None):
# 		self.name = name

# 	def say_hi(self):
# 		if self.name:
# 			print("Hi, I am " + self.name)
# 		else:
# 			print("Hi, I am a robit with about a name")

# 	def set_name(self, name):
# 		self.name = name 

# 	def get_name(self):
# 		return self.name 

# x = Robot()
# x.set_name('Henry')
# x.say_hi()
# y = Robot()
# y.set_name(x.get_name())
# print(y.get_name())

class Robot:
	def __init__(self, name= None, build_year= None):
		self.name = name
		self.build_year = build_year

	def say_hi(self):
		if self.name:
			print("Hi, I am " + self.name)
		else:
			print("Hi, I am a robot without a name")

		if self.build_year:
			print("I was built in " + str(self.build_year))
		else:
			print("It's not known, when I was created!")

	def set_name(self, name):
		self.name = name 

	def get_name(self):
		return self.name 

	def set_build_year(self, by):
		self.build_year = by 

	def get_build_year(self):
		return self.build_year

x = Robot("Henry", 2008)
y = Robot()
y.set_name('Marvin')
x.say_hi()
y.say_hi()
