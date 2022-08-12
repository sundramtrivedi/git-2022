a = int(input("Enter the number a :"))
b = int(input("Enter the number b :"))
c = int(input("Enter the number c :"))
d = int(input("Enter the number d :"))
if(a>b and a>c and a>d):
	print("a is greater than b , c and d")
elif(b>c and b>d):
	print("b is greater than a , c and d")
elif(c>d):
	print("c is greater than a , b and d")
else:
	print("d is greater than a , b and c")
