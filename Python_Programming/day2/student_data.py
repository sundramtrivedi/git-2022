stud = []
while(True):
	print("[1] Add Student Name")
	print("[2] Delete Student Name")
	print("[3] Search Student Name")
	print("[4] Display Student")
	print("[5] Exit")
	ch = int(input("Enter your choice:"))
	if(ch == 1):
		a = str(input("Enter the name of student you want to add :"))
		stud.append(a)
		print(stud)
	elif(ch == 2):
		b = str(input("Enter the name of student you want to delete :"))
		stud.remove(b)
		print(stud)
	elif(ch == 3):
		inp = input("Enter the name of student you want to search :")
		if inp in stud:
			print("Found")
			print(stud)
		else:
			print("Not Found")
	elif(ch == 4):
		print(stud)
	else:
		break
