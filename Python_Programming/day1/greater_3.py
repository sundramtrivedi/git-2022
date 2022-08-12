# greater number program

a = int(input("Enter the number a :"))
b = int(input("Enter the number b :"))
c = int(input("Enter the number c :"))
if(a>b):
	if(a>c):
		print("a is greater than b and c")
	else:
		print("c is greater than a and b")
else:
	if(b>c):
		print("b is greater than a and c")
	else:
		print("c is greater than a and b")

# && and || logic

if(a>b) and (a>c):
		print("a is greater than b and c")
else:
	if(b>c):
		print("b is greater than a and c")
else:
	print("c is greater than a and b")

if(a>b) or if(a>c):
		print("a is greater than b and c")
else:
	if(b>c):
		print("b is greater than a and c")
else:
	print("c is greater than a and b")

