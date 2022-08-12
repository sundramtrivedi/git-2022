# sets
# it will hold only unique elements
# set is unorderd
print("-"*80)
print("e.g : 1")
s = {"Siddhant","Tushar","Abdur","Abhishek","Siddhant"}
# print
print(s)
# convert objects to set
set()

print("-"*80)
print("e.g : 2")
string = "A computer is a machine that can be programmed to carry out sequences of arithmetic or logical operations automatically. Modern computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. A computer system is a complete computer that includes the hardware operating system main software  and peripheral equipment needed and used for full operation. This term may also refer to a group of computers that are linked and function together"
print("string",string)
lst = list(set(map(lambda i : i[0] , string.split())))

print("*"*10)
print("lst :",lst)

print("-"*80)
print("e.g : 3")
t = {"Siddhant","Kiran","Aditya","Ganesh"}
x = {"Nancy","Payal","Snehal","Vinita"}
y = {"Snehal" , "Vinita"}
print("t :",t)
print("x :",x)
print("y :",y)

print("*"*10)
print("e.g : 4")
print("t.intersection(s) :",t.intersection(s))

print("*"*10)
print("e.g : 5")
print("t.union(s) :",t.union(s))

print("*"*10)
print("e.g : 6")
print("t.difference(s) :",t.difference(s))

print("*"*10)
print("e.g : 7")
print("t.symmetric_difference(s) :",t.symmetric_difference(s))

print("*"*10)
print("e.g : 8")
print("t.issubset(x) :",t.issubset(x))

print("*"*10)
print("e.g : 9")
print("x.issuperset(y) :",x.issuperset(y))

print("*"*10)
print("e.g : 10")
print("x.isdisjoint(s) :",x.isdisjoint(s))

print("*"*10)
print("e.g : 11")
print("s.remove(\"Abhishek\") :",s.remove("Abhishek"))	# it is not returning removed element

print("*"*10)
print("e.g : 12")
print("s.pop() :",s.pop())	# it is returning removed element

print("*"*10)
print("e.g : 13")
print("s :",s)

print("*"*10)
print("e.g : 14")
z = t.symmetric_difference(s)	# returns separate set
t.symmetric_difference_update(s)
print("t :",t)

print("*"*10)
print("e.g : 15")
print("s :",s)

print("*"*10)
print("e.g : 16")
t = {"Siddhant","Kiran","Aditya","Ganesh"}
t.difference_update(s)
print("t :",t)

print("*"*10)
print("e.g : 17")
print("s :",s)

print("*"*10)
print("e.g : 18")
t = {"Siddhant","Kiran","Aditya","Ganesh"}
print("t :",t)

print("*"*10)
print("e.g : 19")
print("s :",s)

print("*"*10)
print("e.g : 20")
t.intersection_update(s)
print("t :",t)

print("*"*10)
print("e.g : 21")
s = {"Siddhant","Tushar","Abdur","Siddhant"}
t = {"Siddhant","Kiran","Aditya","Ganesh"}
print("s :",s)
print("*"*10)
print("t :",t)


# loop
print("*"*10)
print("e.g : 22")
for i in s:
	print("i :",i)

print("*"*10)
print("e.g : 23")
print("Tushar" in s)

print("*"*10)
print("e.g : 24")
print(len(s))
# print(s + t)

print("*"*10)
print("e.g : 25")
print("s > t :",s > t)	# by length

print("*"*10)
print("e.g : 26")
print("s < t :",s < t)

# add data to the set
print("*"*10)
print("e.g : 27")
t.add("Sid")
print("t :",t)

print("*"*10)
print("e.g : 28")
s = {}	# empty dictionary
s = set()	# empty set
# list in set :
s = {["10","20"],["30","40"],["50","123"]}
print("s :",s)
