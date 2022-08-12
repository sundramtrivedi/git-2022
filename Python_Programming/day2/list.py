# Lists
# List of student names
lst = [1,2,3,4.555,"Sid"]
lst = [1,2,["Sid","xyz"],4.66]
std = ["Tushar","Abhishek","Sundram","Siddhant"]
#        0	1		2	3
#  	-4	-3		-2	-1
# length of list
print(len(std))
# access elements of list
print(std[0])
print(std[3])
print(std[-1])
std[0] = "Aditya"
print(std[0])
# slice
print(std[1:3])
print(std[:3])
print(std[2:])
print(std[1:-1])
# step syntax
print(std[::2])
print(std[-2:0:-1])
# append data to list
std.append("Aman")
print(std)
# delete data from the list
std.pop() # delete data from the end
print(std)
# remove data from the list
std.remove("Siddhant") # remove the data from any index
print(std)
# list concatination
sts = ["Kiran","Vivek","Nancy"]
print(sts)
print(std)
print(sts + std)
# loop on the list
for i in std:
	print("Name :",i)
std.reverse()
print(std)
std.sort()
print(std)
print(std.index("Aditya")) # index of given value
print(std == sts)
print(std != sts)
print(std > sts)
print(std < sts)

