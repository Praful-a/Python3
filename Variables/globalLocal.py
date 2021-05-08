# This function uses global variable s
# def f():
# 	print(s)

# # Gloabal scope
# s = "I love GeeksforGeeks"
# f()

# This function has a variable with name same as s.
# def f():
# 	s = "Me too."
# 	print(s)

# # Global scope
# s = "I love GeeksforGeeks"
# f()
# print(s)

# def f():
# 	global s
# 	print(s)

# 	# This program will not show error
# 	# if we comment below line.
# 	s = "Me too."

# 	print(s)

# # Global scope
# s = "I Love Python"
# f()
# print(s)

a = 1

# Uses global because there is no local 'a'
# def f():
# 	print("Inside f() : ", a)

# # Variable 'a' is redefined as a local
# def g():
# 	a = 2
# 	print("Inside g() : ", a)

# # Uses global keyword to modify global 'a'
# def h():
# 	global a
# 	a = 3
# 	print("Inside h() : ", a)

# # Global scope
# print("Global : ", a)
# f()
# print("Global : ", a)
# g()
# print("Global : ", a)
# h()
# print("Global : ", a)