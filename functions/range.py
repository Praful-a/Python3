# Python program to understand range this creates a list
# of 0 to 5 integers

# demo = range(6)

# # print the demo
# print(demo)

# # it will generate error
# print(next(demo))

### Above program will give an error####
# beacause range is iterable not iterator

# demo = iter(range(6))
# print(demo)
# print(next(demo))
# print(next(demo))


# Program to understand range

# creates a demo range
demo = range(1, 31, 2)

# print the range
print(demo)

# print the start of range
print(demo.start)

# print step of range
print(demo.step)

# print the index of element 23
print(demo.index(23))

# since 30 is not prsent it will give error
print(demo.index(30))