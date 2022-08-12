print("[1] Add")
print("[2] Substraction")
print("[3] Multiplication")
print("[4] Division")
print("[5] Modulas")
ch = int(input("Enter the choice :"))
a = int(input("Enter the number a:"))
b = int(input("Enter the number b:"))
if ch == 1:
	print(a+b)
elif ch == 2:
	print(a-b)
elif ch == 3:
	print(a*b)
elif ch == 4:
	print(a/b)
elif ch == 5:
	print(a%b)
else:
	print("Invalid input")
