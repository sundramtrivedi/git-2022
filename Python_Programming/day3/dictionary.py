# dictionary
# --> key must be unique
# empty dictionary
d = {}
# syntax :
#{key:value,key:value,key:value,key:value}
# dictionary
s1 =	{	
		"name" : "Payal" ,
		"prn" : "22" ,
		"phone" : "7741046470" ,
		"dob" : "28/03/2000" ,
		"state" : "MH" ,
		"city" : "Satara" 
	}
# print dictionary
print("----------------------------")
print("\n print dictionary \n")
print(s1)
# length of the dictionary
print("----------------------------")
print("\n length of dictionary \n")
print("Length :",len(s1))	# how many key: value pair 
# access every elements
print("----------------------------")
print("\n access every elements \n")
print(s1["name"])
print(s1["prn"])
print(s1["phone"])
# change value of key
print("----------------------------")
print("\n change value of key \n")
s1["state"] = "Maharashtra"
print(s1)
# add new data
print("----------------------------")
print("\n Add new data in dictionary \n")
s1["email"] = "punekarpayalv@gmail.com"
print(s1)
# remove data from dictionary
print("----------------------------")
print("\n Remove the data from dictionary \n")
s1.pop("city")
print(s1)
del s1["state"]
print(s1)
# loops
print("----------------------------")
print("\n loops \n")
print("----------------------------")
print("\n keys \n")
for i in s1.keys():
	print("keys:",i)
print("----------------------------")
print("\n values \n")
for i in s1.values():
	print("values:",i)
print("----------------------------")
print("\n keys : values \n")
for i,j in s1.items():
	print(i,"=>",j)
#
print("**************")
