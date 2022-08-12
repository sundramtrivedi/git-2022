#std = [] 
std =   [	
		{"name" : "Abhishek" , "prn" : 1},
		{"name" : "Abdur" , "prn" : 2},
		{"name" : "Vivek" , "prn" : 3}
	]
print("std[0] :",std[0])	# {"name" : "Abhishek" , "prn" : 1}
print("std[1] :",std[1])	# {"name" : "Abdur" , "prn" : 2}
print("std[1][name] :",std[1]["name"])	# Abdur
print("std[0][prn] :",std[0]["prn"])	# 1
print("std[2][name] :",std[2]["name"])	# Vivek
# "name" in std
s1 =    {
		"name" : "Payal" ,
		"prn" : "22" ,
		"phone" : "7741046470" ,
		"dob" : "28/03/2000" ,
		"address" : 
		{
			"state" : "MH" ,
			"city" : "Satara"
		} ,
		"hobbies" : ["Watching space documentary","Cooking","Video games"]
	}
print("s1[address][state] :",s1["address"]["state"])	# MH
print("s1[hobbies][0] :",s1["hobbies"][0])	# "Watching space documentary"
print("s1[hobbies][0][1:4] :",s1["hobbies"][0][1:4])	# atc
