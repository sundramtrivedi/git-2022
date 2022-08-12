stud = []	#empty
def stud_input():
	stud = {}
	stud["prn"] = int(input("Enter the PRN :"))
	stud["name"] = input("Enter the Name :")
	stud["address"] = {}
	stud["address"]["city"] = input("Enter the City :")
	stud["address"]["state"] = input("Enter the State :")
	return stud
def menu():
	print("[1] Add Student")
	print("[2] Delete Student")
	print("[3] Display Student")
	print("[4] Exit")
def stud_add():
	temp = {}
	temp["prn"] = int(input("Enter the PRN :"))
	temp["name"] = input("Enter the Name :")
	temp["address"] = {}
	temp["address"]["city"] = input("Enter the City :")
	temp["address"]["state"] = input("Enter the State :")
	stud.append(temp)
def stud_delete():
	prn = int(input("Enter the PRN to delete : "))
	for i in stud:
		if i["prn"] == prn:
			stud.remove(i)
def stud_display():
	print(stud)
while True:
	menu()
	ch = int(input("Enter the choice :"))
	if ch == 1:
		stud_add()
	elif ch == 2:
		stud_delete()
	elif ch == 3:
		stud_display();
	elif ch == 4:
		break;
	else:
		print("Wrong choice")
