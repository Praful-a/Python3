import sys
# This will show the version of python interpreter
# with some additional information.
# print(sys.version)


# stdin: It can be used to get input from the command 
# line directly. It used is for standard input. It internally
# calls the input() method. It, also, automatically adds 
# '\n' after each sentence.
# for line in sys.stdin:
# 	if 'q' == line.rstrip():
# 		break
# 	print(f'Input : {line}')
# print("Exit")

# sys.stdout.write('Geeks')

# def print_to_stderr(*a):

# 	# Here a is the array holding the objects
# 	# passed as the arguement of the function
# 	print(*a, file = sys.stderr)

# print_to_stderr('Hello World !!')

# sys.exit([arg]) can be used to exit the program. The
# optional argument arg can be an integer giving the exit
# or another type of object. If it is an integer, zero is considered
# "successful termination"

# age = 17

# if age < 18:
# 	sys.exit("Age less than 18")
# else:
# 	print("Age is not less than 18")


# print(sys.path)
# print(sys.modules)

# sys.getrefcount() method is used to get the reference count
# for any given object. This value is used by Python as when 
# this value becomes 0, the memory for that particular value
# is deleted.

# a = 'geeks'
# print(sys.getrefcount(a))

# Program to explain sys.strecursionlimit() method

# Find the current recursion limit
# limit = sys.getrecursionlimit()

# # print the current limit
# print("Before changing, limit of stack =", limit)

# # New limit
# Newlimit = 500

# # set recursion limit
# sys.setrecursionlimit(Newlimit)

# limit = sys.getrecursionlimit()
# print("After changing, limit of stack =", limit)

# program to display the functioning of
# settrace()
from sys import settrace
  
  
# local trace function which returns itself
def my_tracer(frame, event, arg = None):
    # extracts frame code
    code = frame.f_code
  
    # extracts calling function name
    func_name = code.co_name
  
    # extracts the line number
    line_no = frame.f_lineno
  
    print(f"A {event} encountered in \
    {func_name}() at line number {line_no} ")
  
    return my_tracer
  
  
# global trace function is invoked here and
# local trace function is set for fun()
def fun():
    return "GFG"
  
  
# global trace function is invoked here and
# local trace function is set for check()
def check():
    return fun()
  
  
# returns reference to local
# trace function (my_tracer)
settrace(my_tracer)
  
check()