# formatted string

print("-"*80)
print("e.g : 1")
a = 10
s = "This is a data a = {}".format(a)
print("s :",s)

print("-"*80)
print("e.g : 2")
name = "Siddhant"
a = 10
s = "This is a data name = {} and a = {}".format(name,a)
print("s :",s)

print("-"*80)
print("e.g : 3")
s = "This is a data name = {1} and a = {0}".format(name,a)
print("s :",s)

print("-"*80)
print("e.g : 4")
s = "This is a data name = {x} and a = {y}".format(x=name,y=a)
print("s :",s)

print("-"*80)
print("e.g : 5")
s = "This is a data name = "+ name + " and a = " + str(a) 
print("s :",s)

print("-"*80)
print("e.g : 6")
s = "This is a data"+ str(a)
s = f"This is data {a} and name = {name}"
print("s :",s)

print("-"*80)
print("e.g : 7")
name = "Siddhant"
x = 100
string = "My name is :"+ name + "and my salary is :" + str(x)
print("string",string)

print("-"*80)
print("e.g : 8")
string = "My name is : {} and my salary is {}".format(name,x)
print("string",string)

print("-"*80)
print("e.g : 9")
string = "My name is : {1} and my salary is {0}".format(name,x)
print("string",string)

print("-"*80)
print("e.g : 10")
string = "My name is : {a} and my salary is : {b}".format(a=name,b=x)	# we cannot indexing
print("string",string)
