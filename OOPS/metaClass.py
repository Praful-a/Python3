# class TestClass():
# 	pass

# my_test_class = TestClass()
# print(my_test_class)
# print(type(TestClass))

# Creating class using type
class DataCamp():
	pass

# DataCampClass = type('DataCamp', (), {})
# print(DataCampClass)
# print(DataCamp())

PythonClass = type('PythonClass', (), {'start_date': 'August 2018', 'instructor': 'John Doe'} )
print(PythonClass.start_date, PythonClass.instructor)
print(PythonClass)