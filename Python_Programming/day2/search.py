std = []
data = input("Enter name :")
std.append(data)	# adding data to the list
print(std)	# display
data = input("Enter name :")
std.remove(data)	#removing data element from the list
std = std + ["payal","punekar"]
print(std)
inp = input("Search name :")
print(std)
if inp in std:
	print("Present in this list")
