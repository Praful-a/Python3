# Implicit type conversion

# x = 10
# print("x is of type: ", type(x))

# y = 10.6
# print("y is of type: ", type(y))

# x = x + y
# print(x)
# print("x is of type: ", type(x))

# Explicit type conversion

# initializing string
# s = "10010"

# # printing string converting to int base 2
# c = int(s, 2)
# print("After converting to integer base 2 : ", end="")
# print(c)

# # printing string converting to float
# e = float(s)
# print("After converting to float : ", end="")
# print(e)

# Python code to deomstrate type conversion
# using ord(), hex(), oct()

# s = '4'

# c = ord(s)
# print("After converting character to integer : ", end="")
# print(c)

# c = hex(56)
# print("After converting 56 to hexadecimal string : ", end="")
# print(c)

# c = oct(56)
# print("After converting 56 to octal string : ", end="")
# print(c)

# using of tuple(), set(), list()

# s = 'geeks'

# c = tuple(s)
# print("After converting string to tuple : ", end="")
# print(c)

# c = set(s)
# print("After converting string to set : ", end="")
# print(c)

# c = list(s)
# print("After converting string to list : ", end="")
# print(c)


# a = 1
# b = 2

# tup = (('a', 1), ('f', 2), ('g', 3))

# c = complex(1,2)
# print("After converting integer to complex number : ", end="")
# print(c)

# c = str(a)
# print("After converting integer to string : ", end="")
# print(c)
# print(type(c))

# c = dict(tup)
# print("After converting tuple to dictionary : ", end="")
# print(c)

# Convert ASCII value to characters
a = chr(76)
b = chr(77)

print(a)
print(b)