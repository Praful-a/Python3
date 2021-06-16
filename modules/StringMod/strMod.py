import string
import re
# s = "The quick brown fox jumped over the lazy dog."
# print(s)
# print(string.capwords(s))

values = {'var': 'for'}

# t = string.Template("""
# 	Variable : $var
# 	Escape : $$
# 	Variable in text: ${var}iable
# 	""")
# print('TEMPLATE:', t.substitute(values))

# s = """
# Variable : %(var)s
# Escape : %%
# Variable in text: %(var)siable"""

# print("Interpolation:", s % values)

# s = """
# Variable : {var}
# Escape : {{}}
# Variable in text: {var}iable"""

# print('Format:', s.format(**values))

# values = {'var' : 'foo'}

# t = string.Template("$var is here but $missing is not provided")
# try:
# 	print('substitute() :', t.substitute(values))
# except KeyError as err:
# 	print("Error:", str(err))
# print('safe_substitute():', t.safe_substitute(values))

"""
Since there is no value for missing in the values dictionary, a KeyError is raised by
substitute(). Instead of raising the error, safe_substitute() catches it and leaves the
variable expression alone in the text."""

# class MyTemplate(string.Template):
# 	delimiter = '%'
# 	idpattern = '[a-z]+_[a-z]+'
# template_text = '''
# Delimiter : %%
# Replaced : %with_underscore
# Ignored : %notunderscored
# '''
# d = {
# 'with_underscore': 'replaced',
# 'notunderscored': 'not replaced',
# }
# t = MyTemplate(template_text)
# print('Modified ID pattern:')
# print(t.safe_substitute(d))

# t = string.Template('$var')
# print(t.pattern.pattern)

class MyTemplate(string.Template):
	delimiter = '{{'
	pattern = r'''
	\{\{(?:
	(?P<escaped>\{\{)|
	(?P<named>[_a-z][_a-z0-9]*)\}\}|
	(?P<braced>[_a-z][_a-z0-9]*)\}\}|
	(?P<invalid>)
	)
	'''
t = MyTemplate('''
{{{{
{{var}}
''')
print('MATCHES:', t.pattern.findall(t.template))
print('SUBSTITUTED:', t.safe_substitute(var='replacement'))
