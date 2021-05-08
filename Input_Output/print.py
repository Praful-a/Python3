# \n for new line

# print("Hello \n My name is Python.")
# # "" for empty
# print("")

# This line will automatically add a new before the
# next print statement
# print("The wallstreet is the street of rich mans.")
# print("This is the amazing day to learn python", end="**")

# import time

# count_seconds = 3
# for i in reversed(range(count_seconds + 1)):
# 	if i > 0:
# 		# if we use flush
# 		# print(i, end='>>>')
# 		print(i, end=">>>", flush=True)
# 		time.sleep(1)
# 	else:
# 		print('Start')

# b = "love"
# print("I", b, "Python", sep="->")

import io
# declare a dummy file
dummy_file = io.StringIO()

# add message to the dumy file
print("Hello World!!", file=dummy_file)

# get the value from dummy file
dummy_file.getvalue()
