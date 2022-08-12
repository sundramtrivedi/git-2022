# immutable
# can store any kind of data
t = ("Sid" , "1" , 1 , 324.412) 
# print the tuple
print(t)
# len of tuple
print("Length",len(t))
# access every elements
print("t[0] =>",t[0])
print("t[1] =>",t[1])
# modify value
# t[1] = 12345678	# its immutable thats why we can not assign values
# tuple slicing
print("t[0:1] =>",t[0:1])
print("t[0:2] =>",t[0:2])
print("t[2:] =>",t[2:])
print("t[1:-1] =>",t[1:-1])
#step
print("t[1:-1:2] =>",t[1:-1:2])
print("t[::-1] =>",t[::-1])
print(t)
t[::-1]
for i in t:
	print("value :",i)
if "1" in t:
	print("Found")
else:
	print("Not Found")
# if you want to change tuple redeclare
t = ("Sid" , "1" , 1.5)	
tu = "Siddhant",	# creating tuple
print(tu)
x = "Siddhant" , "Anubhav"
print(x)
