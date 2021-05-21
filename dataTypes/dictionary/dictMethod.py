# Program to demonstrate working of dictionary copy
# original = {1: 'geeks', 2: 'for'}

# # copying using copy() function
# new = original.copy()

# # removing all elements from the list
# # Only new list becomes empty as copy()
# # does shallow copy.
# new.clear()

# print('new: ', new)
# print('original: ', original)

# Program to demonstrate difference between = and copy()
# original = {1: 'geeks', 2:'for'}

# # copying using copy() function
# new = original.copy()

# # removing all elements from new list and printing both
# new.clear()
# print("new: ", new)
# print('original: ', original)

# original = {1:'one', 2:'two'}

# # copying using =
# new = original

# # removing all elements from new list
# new.clear()
# print('new: ', new)
# print("original: ", original)

# Code to demonstrate working of pop()

# test_dict = {'Nikhil': 7, 'Akshat': 1, 'Akash': 2}
# print("The dictionary before deletion : " + str(test_dict))

# pop_ele = test_dict.pop("Akash")
# print("Value associated to popped key is : " + str(pop_ele))
# print("dictionary after deletion is : " + str(test_dict))

# working of pop() without key

# test_dict = {'Nikhil' : 7, 'Akshat' : 1, 'Akash' : 2}

# print("The dictionary before deletion : " + str(test_dict))

# pop_ele = test_dict.pop("Manjeet", 4)

# print('Value associated to pepped key is : ' + str(pop_ele))

# pop_ele = test_dict.pop('Manjeet')
# print('Value associated to popped key is : ' + str(pop_ele))

# Code to demonstrate working of popitem()

# test_dict = {'Nikhil': 7, 'Akshat' : 1, 'Akash' : 2}

# print('The dictionary before deletion : ' + str(test_dict))

# res = test_dict.popitem()

# print('The arbitrary pair returned is : ' + str(res))

# print("The dictionary after removal : " + str(test_dict))

# Code to demonstrate application of popitem()

# test_dict = {'Nihil': 7, 'Akshat': 1, 'Akash': 2}
# print('The dictionary before deltion : ' + str(test_dict))

# n = len(test_dict)

# for i in range(0, n):
# 	print("Rank " + str(i + 1) + " " + str(test_dict.popitem()))

# 	print('The dictionary after deletion : ' + str(test_dict))

# Get Method
# dic = {'A': 1, 'B': 2}
# print(dic['A'])
# print(dic['C']) # here we get the key error

# But by using get() we will get None if key is not present
# print(dic.get("A"))
# print(dic.get("C"))
# print(dic.get("C", "Not Found ! "))

# Program to illustration of values() method of dictionary
# dic = {'raj' : 2, 'striver' : 3, 'vikram' : 4}
# print(dic.values())

# # string vlaues
# dic2 = {'geeks' : '5', 'for' : '3', 'Geeks' : '5'}
# print(dic2.values())

# salary = {'raj' : 50000, 'striver' : 60000, 'vikram' : 5000}
# lst1 = salary.values()
# print(sum(lst1))

# Program to show working of update() method in Dictionary
# dic1 = {'A' : 'Geeks', 'B': 'For', }
# dic2 = {'B' : 'Geeks'}

# # Dictionary before Updation
# print("Original Dictionary:")
# print(dic1)

# dic1.update(dic2)
# print(dic1)

# Update with iterable.
# dic1 = {'A' : 'Geeks'}
# print('Original Dictionary : ')
# print(dic1)
# dic1.update(B = 'for', C = 'Geeks')
# print('Dictionary after updation : ')
# print(dic1)

# Program to show working of setdefault() method in dictionary
# dic1 = {'A' : 'Geeks', 'B': 'For', 'C' : 'Geeks'}
# Third_value = dic1.setdefault('C')
# print('Dictionary : ', dic1)
# print('Third_value : ', Third_value)
# # When key is not in dictionary
# Fourth_value = dic1.setdefault('D', 'Python')
# print(dic1)
# print('Fourth_value', Fourth_value)
# Third_value = dic1.setdefault('E')
# print(Third_value)

# Program to show working of keys in Dictionary
# dic1 = {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}
# print(dic1.keys())
# empty_dic1 = {}
# print(empty_dic1.keys())

# Show how updation of dictionary works
# dic1 = {'A' : 'Geeks', 'B' : 'For'}
# keys = dic1.keys()
# print(keys)

# dic1.update({'C' : 'Geeks'})
# print('After dictionary is updated: ')
# print(keys)
# print("Dictionary items: ")
# print(dic1.items())

# items = dic1.items()
# print(items)
# del dic1['C']
# print('Updated Dictionary')
# print(items)

# Program to show working of fromkeys()
# seq = {'a', 'b', 'c', 'd', 'e'}

# res_dict = dict.fromkeys(seq)
# print("The newly created dict with None values : " + str(res_dict))

# res_dict2 = dict.fromkeys(seq, 1)
# print("The newly created dict with 1 as value : " + str(res_dict2))


seq = {'a', 'b', 'c', 'd', 'e'}
lis1 = [2, 3]
res_dict = dict.fromkeys(seq, lis1)
print("The newly created dict list values : " + str(res_dict))

lis1.append(4)
# Notice that append takes place in all values
print('The dict with list values after appending : ' + str(res_dict))

lis1 = [2, 3]
print('\n')
res_dict2 = {key : list(lis1) for key in seq}
print("The newly created dict with list values : " + str(res_dict2))
