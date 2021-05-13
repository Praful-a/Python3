# Python program to show that variables with a value
# assigned in class declaration, are class variable

# Class for Computer Science Student
class CSStudent:
	stream = 'cse'  # class Variable
	
	def __init__(self, name, roll):
		self.name = name    # Instance Variable
		self.roll = roll 	# Instance Variable

# Objects of CSStudent class
a = CSStudent('Geek', 1)
b = CSStudent('Nerb', 2)

print(a.stream)
print(b.stream)
print(a.name)
print(b.name)
print(a.roll)
print(b.roll)

# Class Variables can be accesed using class name
print(CSStudent.stream)

# Now if we change the stream for just a it won't be changed for b
a.stream = 'ece'
print(a.stream)
print(b.stream)

CSStudent.stream = 'mech'

print(a.stream)
print(b.stream)

