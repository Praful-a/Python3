""" python statements are written in such a format that one statement is only
written in a single line. The interpreter considers the ‘new line character’
as the terminator of one instruction. But, writing multiple statements per
line is also possible that you can find below. """

# Example 1
# print("Welcome to America!")

# Example 2
# x = [1, 2, 3, 4]

# x[1:3] means that start from the index
# 1 and go upto the index 2
# print(x[1:3])

""" In the above mentioned format, the first index
is included, but the last index is not included.
"""

# a = 10; b = 20; c = b + a
# print(a); print(b); print(c)

#Bad practice as width of this code is too much.
# x = 10
# y = 20
# z = 30
# no_of_teachers = x
# no_of_male_students = y
# no_of_female_students = z
 
# if (no_of_teachers == 10 and no_of_female_students == 30 and no_of_male_students == 20 and (x + y) == 30):
#     print('The course is valid')

# This couble be done instead:

# x = 10
# y = 20
# z = 30
# no_of_teachers = x
# no_of_male_students = y
# no_of_female_students = z

# if(no_of_teachers == 10 and no_of_female_students
# 	== 30 and no_of_male_students == 20
# 	 and (x + y) == 30):
# 	print("The course is valid")

# The following code is valid
# a = [
# 	[1, 2, 3],
# 	[3, 4, 5],
# 	[5, 6, 7]
# 	]

# print(a)

# The following code is also valid
# person_1 = 18
# person_2 = 20
# person_3 = 12

# if(
# 	person_1 >= 18 and
# 	person_2 >= 18 and
# 	person_3 < 18
# 	):
# 	print('2 Persons should have Id Cards')

# a = 1-2  # Better way is a  = 1 - 2
# print(a)

# Example 2

# x = 10
# flag = (x == 10) and (x < 12)
# print(flag)

