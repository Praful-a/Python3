# Program to demonstrate the use of isdecimal()

# s = "12345"
# print(s.isdecimal())

# # contains alphabest
# s = "12geeks34"
# print(s.isdecimal())

# s = "12 34"
# print(s.isdecimal())

# isalnum() method

# string = "abc123"
# print(string.isalnum())

# string = "abc 124"
# print(string.isalnum())

# istitle() method
# s = 'Geeks For Geeks'
# print(s.istitle())

# s = 'geeks For Geeks'
# print(s.istitle())

# s = 'Geeks For GEEKs'
# print(s.istitle())

# s = '6041 Is My Number'
# print(s.istitle())

# s = 'GEEKS'
# print(s.istitle())

# Code 2
# s = "I Love Geeks For Geeks"
# if s.istitle() == True:
# 	print('Titlecased String')
# else:
# 	print("Not a Titlecased String")

# s = "I Love geeks for geeks"
# if s.istitle() == True:
# 	print('Titlecased String')
# else:
# 	print('Not a Titlecased String')

# String partition()

# string = "pawan is a good"
# print(string.partition('is '))

# # 'not' seperator is not found
# print(string.partition('bad '))

# string = 'pawan is a good, isn\'t it'
# print(string.partition('is'))

# Code 2
# string = "python is a good language"

# print(string.partition('is '))

# print(string.partition('bad '))

# string = 'geeks is a good, isn\'t it'
# print(string.partition('is'))


# Code to illustrate the working of isidentifier()
# string = "Geeks for Geeks"
# print(string.isidentifier())

# # A Perfect identifier
# string = "GeeksforGeeks"
# print(string.isidentifier())

# string = "Geeks0for0Geeks"
# print(string.isidentifier())

# # Beginning with an integer
# string = "54Geeks0for0Geeks"
# print(string.isidentifier())

# Program to demonstrate the use or len() method
# string = 'geeks'
# print(len(string))

# string = 'geeks for geeks'
# print(len(string))

# Code to demonstrate working of rindex()
# text = "geeks for geeks"

# result = text.rindex('geeks')
# print("Substring 'geeks':", result)

# quote = "geeks for geeks"
# print(quote.rindex('ge', 2, 13))

# print(quote.rindex('geeks', 0, 16))

# Program to demonstrate the use of max() function

# maximum alphabetical character in "geeks"
# string = "geeks"
# print(max(string))
# print(min(string))
# string = "Python"
# print(max(string))
# print(min(string))

# Code to illustrate splitlines()
# string = "Welcome everyone to\rth world of Geeks\nGeeksforGeeks"

# print(string.splitlines())
# print(string.splitlines(0))
# # True has been passed
# print(string.splitlines(True))

# Code 2
# string = "Cat\nBat\nSat\nMat\nXat\nEat"
# # No parameters has been passed
# print(string.splitlines())
# print("India\nJapan\nUSA\nUK\nCanada\n".splitlines())

# Practical Application
# def Cal_len(string):
# 	li = string.splitlines()
# 	print(li)

# 	l = [len(ele) for ele in li]
# 	return l

# # Driver Code
# string = "Welcome\rto\rGeeksforGeeks"
# print(Cal_len(string))

# Capitalize() method

# name = "i Love Python"
# print(name.capitalize())

# name1 = "the"
# name2 = "royal"
# name3 = "circus"
# print(name1.capitalize() + " " + name2.capitalize() + " " + name3.capitalize())

# paragraph = '''my name is Praful.
# I live in Noida.'''
# print(paragraph.capitalize())

# Python code to demonstrate working of expandtabs
# str = "i\tlove\tgfg"

# print("Modified string using default spacing: ", end="")
# print(str.expandtabs())
# print("\r")

# print("Modified string using less spacing: ", end="")
# print(str.expandtabs(2))

# print("\r")

# # using expandtabs to insert spacing
# print("Modified string using more spacing: ",end="")
# print(str.expandtabs(12))
# print("\r")

# find() 

# word = "I Love Python"

# result = word.find('Love')
# print("Substring 'Love' found at index: ", result)

# result = word.find('Python')
# print("Substring 'Python' found at index:", result)

# # How to use fint()
# if(word.find('java') != -1):
# 	print("contains given substring")
# else:
# 	print("Doesn't contains given substring")

# word = "geeks for geeks"

# # Substring is searched in 'eks' for 'geeks'
# print(word.find('ge', 2))

# # Substring is searched in 'eks for geeks'
# print(word.find('geeks', 2))

# # Substring is searched in 's for g'
# print(word.find('g', 4, 10))

# # Substring is searched in 's for g'
# print(word.find('for', 4, 11))

# rfind()

# word = 'geeks for geeks'

# result = word.rfind('geeks')
# print("Substring 'geeks' found at index: ", result)

# restult = word.rfind('for')
# print("Substring 'for' found at index: ", result)

# word = 'CatBatSatMatGate'
# result = word.rfind('ate')
# print("Substring 'ate' found at index :", result)

# Code #2

# word = "geeks for geeks"

# print(word.rfind('ge', 2))

# print(word.rfind('geeks', 2))

# print(word.rfind('eeks', 2))

# print(word.rfind('for', 4, 11))

# Application
# word = 'CatBatSatMatGate'

# if (word.rfind('Ate') != -1):
# 	print("contains given substring")
# else:
# 	print("Doesn't contains given substring")

# count() method without optional parameters
# string = "geeks for geeks"

# print(string.count('geeks'))

# Using optional parameters
# string = "geeks for geeks"
# print(string.count("geeks", 0, 5))
# print(string.count("geeks", 0, 15))

# lower() function
# text = "I Love PYTHON"

# print("Original String: ", end="")
# print(text)

# print("Converted String: ", end="")
# print(text.lower())

# string the alphanumeric characters
# text = "I 1Lo2v3e PYTHON"

# print("Original String: ", end="")
# print(text)

# print("Converted String: ", end="")
# print(text.lower())

# Application for lower method
# text1 = "GEEKS for GEEKS"
# text2 = "gEeKs fOR GeeKs"

# if(text1.lower() == text2.lower()):
# 	print("Strings are same")
# else:
# 	print("Strings are not same")

# text = 'geeks for geeks'

# print(text.split())

# word = 'geeks, for, geeks'

# print(word.split(','))

# word = "geeks:for:geeks"
# print(word.split(":"))

# word = "CatBatSatFatOr"
# print(word.split('t'))

# splict by giving optional parameter maxsplit
# word = "geeks, for, geeks, pawan"
# print(word.split(', ', 0))

# print(word.split(', ', 4))
# print(word.split(', ', 1))

# rsplit()

# word = "geeks, for, geeks, pawan"
# print(word.rsplit(', ', 0))

# print(word.rsplit(', ', 4))
# print(word.rsplit(', ', 1))

# text = 'geeks for geeks'

# print(text.rsplit())

# word = 'geeks, for, geeks'

# print(word.rsplit(','))

# word = "geeks:for:geeks"
# print(word.rsplit(":"))

# word = "CatBatSatFatOr"
# print(word.rsplit('t'))

# rpartition
# string1 = "Geeks@for@Geeks@is@for@geeks"
# string2 = "Ram is not eating but Mohan is eating"

# print(string1.rpartition('@'))

# print(string2.rpartition('is'))

# string = "Sita is going to school"
# print(string.rpartition("not"))

# Code 3: TypeError
# str = "Bruce Waine is Batman"
# print(str.rpartition())
# print(str.rpartition("")) # value Error

# Python program to demonstrate the use of join functoin
# Here 2 is non string so this will give an error
# list1 = ['1', 2, '3', '4'] 
# s = "-"
# s = s.join(list1)
# print(s)

# list2 = ['g', 'e', 'e', 'k', 's']
# print("".join(list2))

# strip()

# string = """    geeks for geeks    """
 
# prints the string without stripping
# print(string)
 
# prints the string by removing leading and trailing whitespaces
# print(string.strip())  
 
# prints the string by removing geeks
# print(string.strip(' geeks'))

# str1 = "geeks for geeks"
# print(str1)

# str2 = "ekgs"
# print(str1.strip(str2))

# Practical application
# string = " the King has the largest army in the entire world the"
# print(string.strip(" the"))

# string = "sssgeekssss"
# print(string.rstrip('s'))

# string = "    for   "
# print("Geeks" + string.rstrip() + "  Geeks  ")

# string = "geeks for geeks"
# print(string.rstrip('ek'))

# string = "geeks for geeks"
# print(string.rstrip('ske'))

# Program to demonstrate the use of swapcase() method
# string  = "gEEksFORgeeks"
# print(string.swapcase())
# string = "striver"
# print(string.swapcase())

# Program to translations without maketrans()
# table = {119 : 103, 121 : 102, 117 : None}
# trg = "weeksyourweeks"
# print("The string before translating is : ", end="")
# print(trg)

# print("The string after translating is : ", end="")
# print(trg.translate(table))

# firstString = "gee"
# secondString = "eks"
# thirdString = "ge"
# string = "geeks"
# print("Original string:", string)
# translation = string.maketrans(firstString,
# 							   secondString,
# 							   thirdString)
# print("Translated string:", string.translate(translation))

# upper()

# text = "geeKs For geEkS"
# print("Original String: ")
# print(text)

# print("\nConverted String: ")
# print(text.upper())

# Application
# text1 = "geeks fOr geeks"
# text2 = "gEeKs fOR GeeKs"
# if(text1.upper() == text2.upper()):
# 	print("Strings are same")
# else:
# 	print("Strings are not same")

# Program to demonstrate working of rjust()
# string = "geeks"
# length = 8
# print(string.rjust(length))

# example with fillchar
# string = "geeks"
# length = 8
# fillchar = "*"
# print(string.rjust(length, fillchar))

# string = "geeks"
# # length = 8

# # print(string.ljust(length))
# length = 8
# fillchar = "*"
# print(string.ljust(length, fillchar))

# Program to illustrate string center() in python
# string = "geeks for geeks"
# new_string = string.center(24)
# print("After padding String is: ", new_string)

# with fillchar
# string = "geeks for geeks"
# new_string = string.center(24, "*")
# print("After padding String is: ", new_string)

# zfill()
# text = "geeks for geeks"
# print(text.zfill(25))
# print(text.zfill(20))
# print(text.zfill(10))

# Code 2
# number = "6041"
# print(number.zfill(8))
# number = "+6041"
# print(number.zfill(8))
# text = "+--anything%(&%(%)*^"
# print(text.zfill(21))

# def replaceABwithC(input, pattern, replaceWith):
# 	return input.replace(pattern, replaceWith)

# # Driver program
# if __name__ == "__main__":
# 	input = "helloABworld"
# 	pattern = "AB"
# 	replaceWith = 'C'
# 	print(replaceABwithC(input, pattern, replaceWith))

# def replaceABwithC(input, pattern, replaceWith, Maxcount):
# 	return input.replace(pattern, replaceWith, maxcount)

# # Driver Code
# if __name__ == "__main__":
# 	input = "helloABworldAB"
# 	pattern = 'AB'
# 	replaceWith = 'C'
# 	maxcount = 1
# 	print(replaceABwithC(input, pattern, replaceWith, maxcount))

# casefold()
# string = "GEEKSFoRGEEKS"
# print(" lowercase string: ", string.casefold())

# Program to check if a string is palindrome or not
# str = 'geeksforgeeks'
  
# # make it suitable for caseless comparison
# str = str.casefold()
# # reverse the string
# rev_str = reversed(str)
  
# # check if the string is equal to its reverse
# if str == rev_str:
#       print("palindrome")
# else:
#       print(" not palindrome")

# Count vowels in string
# v = 'aeiou'
# str = "Hello, have you try geeksforgeeks?"
# str = str.casefold()

# c = {}.fromkeys(v, 0)
# for char in str:
# 	if char in c:
# 		c[char] += 1
# print(c)

# Python code to print all encodings available
# from encodings.aliases import aliases
# print("The available encodings are : ")
# print(aliases.keys())

# str = "geeksforgeeks"
# print("The encoded string in utf8 format is : ", )
# print(str.encode('utf8', 'ignore'))

# Code to demonstrate translations using maketrans() and translate()
# str1 = "wy"
# str2 = "gf"
# str3 = "u"
# trg = "weeksyourweeks"
# table = trg.maketrans(str1, str2, str3)

# print("The string before translating is : ", end ="")
# print(trg)

# print("The string after translating is : ", end="")
# print(trg.translate(table))

# Without maketrans()
table = {119: 103, 121: 102, 117: None}
trg = "weeksyourweeks"
print("The string before translating is : ", end="")
print(trg)

print("The string after translating is : ", end="")
print(trg.translate(table))


