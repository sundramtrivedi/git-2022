emp = []
def emp_input():
	emp = {}
	emp["empID"] = int(input("Enter the empID :"))
	emp["name"] = input("Enter the Name :")
	emp["age"] = int(input("Enter the Age :"))
	emp["gender"] = input("Enter the Gender :")
	emp["address"] = {}
	emp["address"]["city"] = input("Enter the City :")
	emp["address"]["state"] = input("Enter the State :")
	emp["salary"] = int(input("Enter the Salary :"))
	emp["company"] = input("Enter the Previouse Company :")
	return emp
def emp_add():
	temp = {}
	temp["empID"] = int(input("Enter the empID :"))
	temp["name"] = input("Enter the Name :")
	temp["age"] = int(input("Enter the Age :"))
	temp["gender"] = input("Enter the Gender :")
	temp["address"] = {}
	temp["address"]["city"] = input("Enter the City :")
	temp["address"]["state"] = input("Enter the State :")
	temp["salary"] = int(input("Enter the Salary :"))
	temp["company"] = input("Enter the Previouse Company :")
	emp.append(temp)
def emp_delete():
	name = input("Enter the Name to delete : ")
	for i in emp:
		if i["name"] == name:
			emp.remove(i)
def emp_display():
	print(emp)
def search_name():
	name = input("Enter the Name to search : ")
	for i in emp:
		if i["name"] == name:
			print(i)
def search_gender():
	gender = input("Enter the gender to search : ")
	for i in emp:
		if i["gender"] == gender:
			print(i)
def menu():
	print("[1] Add Employee")
	print("[2] Delete Employee")
	print("[3] Display Employee")
	print("[4] Search by Name")
	print("[5] Search by Gender")
	print("[6] Exit")
while True:
	menu()
	ch = int(input("Enter the choice :"))
	if ch == 1:
		emp_add()
	elif ch == 2:
		emp_delete()
	elif ch == 3:
		emp_display()
	elif ch == 4:
		search_name()
	elif ch == 5:
		search_gender()
	elif ch == 6:
		break;
	else:
		print("Wrong choice")
