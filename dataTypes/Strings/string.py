# Program for Creation of String

# Creating a String with single Quotes
# String1 = 'Welcome to the Geeks World'
# print("String with the use of Single Quotes: ")
# print(String1)

# Creating a String with double Quotes
# String1 = "I'm a Geek"
# print("\nString with the use of Double Quotes: ")
# print(String1)

# # Creating a String with triple Quotes
# String1 = '''I'm a Geek and I live in a world of "Geeks"'''
# print("\nString with the use of Triple Quotes: ")
# print(String1)

# # Creating String with triple Quotes allows multiple line
# String1 = '''I
# 			Love
# 			Python'''
# print("\nCreating a multiline String: ")
# print(String1)

# Program to Access characters of String

# String1 = "GeeksForGeeks"
# print("Initial String: ")
# print(String1)

# # Printing First character
# print("\nFirst character of String is: ")
# print(String1[0])

# # Printing Last character
# print("\nLast character of String is: ")
# print(String1[-1])

# Program to demonstrate String slicing

# Creating a String
# String1 = "GeeksForGeeks"
# print("Initial String: ")
# print(String1)

# # Printing 3rd and 12th character
# print("\nSlicing character from 3-12: ")
# print(String1[3:12])

# # Printing characters between 3rd and 2nd last character
# print("\nSlicing characters between " +
# 	  "3rd and 2nd last character: ")
# print(String1[3:-2])

# Program to Update character of a String

# String1 = "Hello, I'm a Python"
# print("Initial String: ")
# print(String1)

# # Updating a character of the String
# String1[2] = 'p'
# print("\nUpdating character at 2nd Index: ")
# print(String1)

# Program to Update entire String

# String1 = "Hello, I'm a Python"
# print("Initial String: ")
# print(String1)

# # Updating a String
# String1 = "Welcome to the Geek World"
# print("\nUpdated String: ")
# print(String1)


# Porgram to delete entire string

# String1 = "Hello, I'm a Python"
# print("Initial String: ")
# print(String1)

# del String1

# print("\nDeleting entire string: ")
# print(String1)  # this will give an error becase string is deleted

# Program to Escape Sequencing of String

# Initial String
# String1 = '''I'm a "Geek"'''
# print("Initial String with use of Triple Quotes: ")
# print(String1)

# # Escaping Single Quote
# string1 = 'I\'m a "Geeks"'
# print("\nEscapig Single Quote: ")
# print(string1)

# Escaping Double Quotes
# string1 = "I'm a \"Geek\""
# print("\nEscaping Double Quotes: ")
# print(string1)

# # Printing Paths with the use fo Escape Sequence
# string1 = "C:\\Python\\Geeks\\"
# print("\nEscaping Backslashes: ")
# print(string1)


# Printing Geeks in HEX
# string1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
# print('\nPrinting in HEX with the use of Escape Sequence: ')
# print(string1)

# # Using raw String to ignore Escape Sequence
# string1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
# print("\nPrinting Raw String in HEX Format: ")
# print(string1)

# Program for Formatting of Strings

# Default order
# string1 = "{} {} {}".format("I", "Love", "Python")
# print("Print String in default order: ")
# print(string1)

# # Positional Formatting
# string1 = "{1} {0} {2}".format("I", 'Love', 'Java')
# print("\nPrint String in Positional order: ")
# print(string1)

# # Keyword Formatting
# String1 = "{l} {f} {g}".format(g = "Geeks", f = 'For', l = 'Life')
# print("\nPrint String in order of Keywords: ")
# print(String1)

# Formating of Integers
# string1 = "{0:b}".format(16)
# print("\nBinary representation of 16 is ")
# print(string1)

# # Formatting of Floats
# string1 = "{0:e}".format(165.6458)
# print("\nExponent representation of 165.6458 is ")
# print(string1)

# # Rounding off Integers
# string1 = "{0:.2f}".format(1/6)
# print("\none-sxith is : ")
# print(string1)


# String alignment
# String1 = "|{:<10}|{:^10}|{:>10}".format("Geeks", 'for', 'Geeks')
# print("\nLeft, center and right alignment with Formatting: ")
# print(String1)

# # To demonstrate aligning of spaces
# String1 = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2009)
# print(String1)

# Program for Old Style Formatting of Integers

# Integer1 = 12.3456789
# print("Formatting in 3.2f format: ")
# print("The value of Integer1 is %3.2f" % Integer1)
# print("\nFormatting in 3.4f format: ")
# print("The value of Integer1 is %3.4f" %Integer1)

s = 'Python'
a = list(s)[::-1]
a[0] = 'a'
a = a[::-1]
print("".join(a))