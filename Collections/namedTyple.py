# Code to demonstrate namedtuple()

# from collections import namedtuple

# Student = namedtuple('Student', ['name', 'age', 'DOB'])

# s = Student('Nandini', '19', '2541997')

# print("The Student age using index is : ", end="")
# print(s[1])

# print("The Student name using keyname is : ", end="")
# print(s.name)

# Code to demonstrate namedtuple() and Access by
# name, index and getattr()

# importing "collections" for namedtuple()
# import collections

# Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])

# S = Student('Nandini', '19', '2541997')

# print("The Student age using index is : ", end="")
# print(S[1])

# print("The Student name using keyname is : ", end="")
# print(S.name)

# print("The Student DOB using getattr() is : ", end="")
# print(getattr(S, 'DOB'))

# Python code to demonstrate namedtuple() and 
# _make(), _sdict() and "**" operator

# import collections
# # Declaring namedtuple()
# Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])

# S = Student('Nandini', '19', '2451997')

# li = ['Manjeet', '19', '411997']

# di = {'name': 'NIkhil', 'age': '19', 'DOB' : '1391997'}

# print("The namedtuple instance using iterable is : ")
# print(Student._make(li))
# print("\r")
# print("The OrderedDict instance using namedtuple is : ")
# print(S._asdict())
# print()
# print("The namedtuple instance from dict is : ")
# print(Student(**di))

# _fields and _replace()

import collections

Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])

S = Student("Nandini", '19', '2541997')

print("All fields of Student are : ")
print(S._fields)

print("The modified namedtuple is : ")
print(S._replace(name = 'Manjeet'))