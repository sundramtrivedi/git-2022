def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
menu =	{
		"1" : add,
		"2" : sub,
		"3" : mul
	}
while True:
	print("[1] Add")
	print("[2] Sub")
	print("[3] Mul")
	print("[4] Exit")
	ch = input("Enter the choice :")
	if int(ch) == 4:
		break
	else:	
		a = int(input("Enter the number a :"))
		b = int(input("Enter the number b :"))
		print(menu[ch](a,b))
