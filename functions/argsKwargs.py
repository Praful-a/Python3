# Program to illustrate
# *args for variable number of arguments
# def myFun(*argv):
# 	for arg in argv:
# 		print(arg)

# myFun('Hello' , 'Welcome', 'to', 'America')

# Program to illusrate *args with first extra argument
# def myFun(arg1, *argv):
# 	print("First argument :", arg1)
# 	for arg in argv:
# 		print("Next argument through *argv :", arg)

# myFun("Hello", "Welcome", "to", "India")

# Program to illusrate **kwargs for variable number
# of keyword arguments

# def myFun(**kwargs):
# 	for key, value in kwargs.items():
# 		print("%s == %s" %(key, value))

# # Driver code
# myFun(first='I', mid='Love', last="Python")

# Python program to illustrate  **kargs for
# variable number of keyword arguments with
# one extra argument.
 
# def myFun(arg1, **kwargs):
#     for key, value in kwargs.items():
#         print ("%s == %s" %(key, value))
 
# # Driver code
# myFun("Hi", first ='Geeks', mid ='for', last='Geeks')


# def myfun(arg1, arg2, arg3):
# 	print("arg1:", arg1)
# 	print("arg2:", arg2)
# 	print("arg3:", arg3)

# # Now we can use *args or **kwargs to pass
# # arguments to this function :
# args = ("I", "Love", "Python")
# myfun(*args)

# kwargs = {"arg1" : "I", "arg2" : "Love", "arg3" : "Python"}
# myfun(**kwargs)

# Using *args and **kwargs in same line to call a function

def myfun(*args, **kwargs):
	print("args: ", args)
	print("kwargs: ", kwargs)

# Now we can use both *args, **kwargs
# to pass arguments to this function
myfun("I", "Love", "Code", first="I", mid="Love", last="Code")
