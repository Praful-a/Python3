# In python 2 division
# print 7 / 5
# print -7 / 5

# Output in Python 2.x
# 1
# -2
# to get same output as python 3.x then put 7.0 instead 7 
# in above code

# In Python3.x versions
# print(7/5)
# print(-7/5)

# ouput in Python 3.x :
# 1.4
# -1.4

#### Print Function  ####
# print 'Hello, Praful'   # Python 2 

# output in python 2 :
# Hello, Praful

# ouput in python 3 :
# print 'Hello, Praful'   # Python 2         ^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print('Hello, Praful'   # Python 2)?

# print("Hope You like these facts")  # Python 3.x


				#### Unicode #####
"""In Python 2, an implicit str type is ASCII.
But in Python 3.x implicit str type in Unicode"""

# print(type('default string'))
# print(type(b'string with b'))

''' Output in Python 2.x (Bytes is same as str)
<type 'str'>
<type 'str'>
 
Output in Python 3.x (Bytes and str are different)
<class 'str'>
<class 'bytes'> '''

# Python 2.x also supports Unicode
# print(type('default string'))
# print(type(u'string with b'))

''' Output in Python 2.x (Unicode and str are different)
<type 'str'> 
<type 'unicode'>

Output in Python 3.x (Unicode and str are same)
<class 'str'>
<class 'str'>'''

				#### xrange ######

"""xrange of python 2.x doesn't exist in Python 3.x. In Python 2.x, range
returns list i.e. range(3) returns [0, 1, 2] while xrange returns a xrange
object i.e., xrange(3) return iterator object which works similar to java
iterator and generates number when needed.
# If we need to iterate over the same sequence multiple times, we prefer range()
as range provides a static list.
# xrange() reconstructs the sequence every time.
# xrange() doesn't support slices and other list methods.
# advantage of xrange() is, it saves memory when the task is to iterate over a 
large range.

In Python 3.x, the range function now does what xrange does in Python 2.x, so to keep our code portable
"""

# for x in xrange(1, 5):
# 	print(x)

''' Output in Python 2.x 
1 2 3 4 1 2 3 4

Output in Python 3.x
NameError: name 'xrange' is not defined
'''

# for x in range(1, 5):
# 	print(x)
"""
ouput :
1
2
3
4	"""


			#### Error Handling ####

# try:
#     trying_to_check_error
# except NameError, err:
#     print err, 'Error Caused'   # Would not work in Python 3.x
 
''' Output in Python 2.x 
name 'trying_to_check_error' is not defined Error Caused

Output in Python 3.x :
File "a.py", line 3
    except NameError, err:
                    ^
SyntaxError: invalid syntax
'''

## To run above code in python 3.x

# try:
# 	trying_to_check_error
# except NameError as err:  # 'as' is need Python 3.x
# 	print(err, 'Error Caused')