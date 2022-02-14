import re

text = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
.[{()\^$|?*+

coreyms.com

321-555-4321
123.555.1234
800-555-4321
900.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat 
mat
pat
bat
'''


# first match
# pattern = re.compile(r'abc')
# matches = pattern.finditer(text)

# for match in matches:
# 	print(match)

# print(text[1:4])

# lets match '.' in texts

# pattern = re.compile(r'.')
# only matches '.'
# pattern = re.compile(r'\.')
# matches = pattern.finditer(text)

# for match in matches:
# 	print(match)

# # Matching url 
# pattern = re.compile(r'coreyms\.com')
# matches = pattern.finditer(text)
# for match in matches:
# 	print(match)

# # matching only digits
# pattern = re.compile(r'\d')
# matches = pattern.finditer(text)
# for match in matches:
# 	print(match)

# # Not a Digit
# pattern = re.compile(r'\D')
# matches = pattern.finditer(text)
# for match in matches:
# 	print(match)

# # Word Character
# pattern = re.compile(r'\w')
# matches = pattern.finditer(text)
# for match in matches:
# 	print(match)

# # Not a Word Character
# pattern = re.compile(r'\W')
# matches = pattern.finditer(text)
# for match in matches:
# 	print(match)

# # Whitespace (space, tab, newline)
# pattern = re.compile(r'\s')
# matches = pattern.finditer(text)
# for match in matches:
# 	print(match)


# # Not Whitespace (space, tab, newline)
# pattern = re.compile(r'\S')
# matches = pattern.finditer(text)
# for match in matches:
# 	print(match)


# # Word Boundary
# pattern = re.compile(r'\bHa')
# pattern = re.compile(r'\BHa')
# matches = pattern.finditer(text)
# for match in matches:
# 	print(match)


sentence = 'Start a sentence an then end bring it to an end'

# Beginning of a string
# pattern = re.compile(r'^Start')
# matches = pattern.finditer(sentence)
# for match in matches:
# 	print(match)


# End in a string
# pattern = re.compile(r'end')
# pattern = re.compile(r'end$')
# matches = pattern.finditer(sentence)
# for match in matches:
# 	print(match)


# # Let's match numbers
# 321-555-4321
# 123.555.1234
# pattern = re.compile(r'\d\d\d\.\d\d\d\.\d\d\d\d')
# pattern = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d')
# matches = pattern.finditer(text)
# for match in matches:
	# print(match)

# Matching numbers from file
# with open('data.txt', 'r') as f:
# 	contents = f.read()
# 	matches = pattern.finditer(contents)

# 	for match in matches:
# 		print(match)


# Matching only 1 and 5 in text
# pattern = re.compile(r'[15]')
# matches = pattern.finditer(text)
# for match in matches:
# 	print(match)

# # Match only small alphabets
# pattern = re.compile(r'[a-z]')
# matches = pattern.finditer(text)
# for match in matches:
# 	print(match)

# # Match only small and capital alphabets
# pattern = re.compile(r'[a-zA-Z]')
# pattern = re.compile(r'[^a-zA-Z]')
# matches = pattern.finditer(text)
# for match in matches:
# 	print(match)


# # Let's match all the words end with at except bat
# pattern = re.compile(r'[^b]at')
# matches = pattern.finditer(text)
# for match in matches:
# 	print(match)

# # # Let's use quantifiers
digits = '''
321-555-4321
123.555.1234
123*555*1234
800-555-4321
900.555.1234
'''

# pattern = re.compile(r'\d\d\d\.\d\d\d.\d\d\d\d')
# matches = pattern.finditer(digits)
# for match in matches:
# 	print(match)

# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# matches = pattern.finditer(digits)
# for match in matches:
# 	print(match)


# Matching names starts with Mr.
# pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
# matches = pattern.finditer(text)
# for match in matches:
# 	print(match)


# Matching names starts with Mr and Ms
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
# pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
# matches = pattern.finditer(text)
# for match in matches:
# 	print(match)

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

# pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
# matches = pattern.finditer(emails)
# for match in matches:
# 	print(match)

# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
# matches = pattern.finditer(emails)
# for match in matches:
# 	print(match)


# #### Let's match urls

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# subbed_urls = pattern.sub(r'\2\3', urls)
# print(subbed_urls)

# matches = pattern.finditer(urls)

# for match in matches:
# 	print(match)


# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# matches = pattern.findall(urls)
# for match in matches:
# 	print(match)

# pattern = re.compile(r'sentence')

# matches = pattern.search(sentence)
# print(matches)

# pattern = re.compile(r'start', re.IGNORECASE)
pattern = re.compile(r'start', re.I)

matches = pattern.match(sentence)
# matches = pattern.search(sentence)
print(matches)

