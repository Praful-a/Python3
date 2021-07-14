from collections import OrderedDict
ordered_dict = OrderedDict()
N = int(input())
for _ in range(N):
	item_name, net_price = input().rsplit(' ', 1)
	if item_name not in ordered_dict:
		ordered_dict[item_name] = int(net_price)
	else:
		ordered_dict[item_name] += int(net_price)
for i in ordered_dict:
	print(f"{i} {ordered_dict[i]}")

# s = 'Hello World I'
# print(s.rsplit(' ',1))