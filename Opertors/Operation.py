# Examples of Arithmetic Operator

# a = 9
# b = 4

# # Addition of numbers
# add = a + b

# # Subtraction of numbers
# sub = a - b

# # Multiplication of number
# mul = a * b

# # Division(float) of number
# div1 = a / b

# # Division(floor) of number
# div2 = a // b

# # Modulo of both number
# mod = a % b

# # Power 
# p = a ** b

# # print results
# print(add)
# print(sub)
# print(mul)
# print(div1)
# print(div2)
# print(mod)
# print(p)

# Examples of relational Operators
# a = 13
# b = 33

# # a > b is False
# print(a > b)

# # a < b is True
# print(a < b)

# print(a == b)
# print(a >= b)
# print(a <= b)

# Examples of Logical Operator
# a = True
# b = False

# print(a and b)

# print(a or b)
# print(not a)

# Examples of Bitwise operators
# a = 10
# b = 4

# # Print bitwise And Operation
# print(a & b)

# print(~a)

# # print bitwise XOR operation
# print( a ^ b)

# print(a >> 2)

# print(a << 2)

# Examples of Identity operators
# a1 = 3
# b1 = 3
# a2 = 'GeeksforGeeks'
# b2 = "GeeksforGeeks"
# a3 = [1, 2, 3]
# b3 = [1,2, 3]

# print(a1 is not b1)

# print(a2 is b2)

# print(a3 is b3)

# x = 'Geeks for Geeks'
# y = {3: 'a', 4: 'b'}

# print('G' in x)
# print('geeks' not in x)
# print('Geeks' not in x)
# print(3 in y)
# print('b' in y)

# Precedence of '+' & '*'
# expr = 10 + 20 * 30
# print(expr)

# # precedence of 'or' & 'and'
# name = "Alex"
# age = 0

# if (name == "Alex" or name == "John") and age >= 2:
# 	print("Hello! Welcome.")
# else:
# 	print("Good Bye!!")

# Examples of Operator Associativity
  
# Left-right associativity 
# 100 / 10 * 10 is calculated as  
# (100 / 10) * 10 and not  
# as 100 / (10 * 10) 
print(100 / 10 * 10) 
    
# Left-right associativity 
# 5 - 2 + 3 is calculated as  
# (5 - 2) + 3 and not  
# as 5 - (2 + 3) 
print(5 - 2 + 3) 
    
# left-right associativity 
print(5 - (2 + 3)) 
    
# right-left associativity 
# 2 ** 3 ** 2 is calculated as  
# 2 ** (3 ** 2) and not  
# as (2 ** 3) ** 2 
print(2 ** 3 ** 2)