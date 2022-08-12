a = str(input("Enter the string :"))
print(a[::-1])
if(a == a[::-1]):
	print("String is palindrome")
else:
	print("String is not palindrome")
