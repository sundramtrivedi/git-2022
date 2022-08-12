a = int(input("Enter the integer :"))
b = a
rev = 0
while(a != 0):
	rem = a % 10
	rev = rev * 10 + rem
	a = a // 10
if(b == rev):
	print("Integer is palindrome")
else:
	print("Integer is not palindrome")
