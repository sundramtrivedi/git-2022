# string operations
name = "Siddhant"
#	01234567
# length of string
print("Lenth of string")
print(len(name))
# access string index
print("access string index")
print(name[0])	#s
print(name[1])	#i
print(name[5])	#a
#name[0] = 'A' #invalid operation
# cannot modify the index value
# string is read only(immutable)
# string slicing
print("string slicing")
print(name[2:4])
# variable(start_index : end_index)
# end_index is excluded
print("Positive indexing")
print(name[2:6])
print(name[:3])
print(name[5:])
print("Negative indexing")
print(name[:-5])
print(name[-3:])
print(name[1:7:2])
#print(name[1:7:0]) #error
print(name[1:7:-1]) #blank
print(name[5:1:-1])
print(name[5:1:-2])
print(name[1:5:-2]) #blank
print(name[-4:-7:-1])
